'''
Created on Dec 28, 2015

@author: eRiC
'''
from PySide import QtCore, QtGui
import a2ctrl
import ahk
from a2ctrl import hotkey_edit_ui
from a2ctrl import scopeDialog_ui
import logging
from functools import partial
from os.path import join
import subprocess

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Draw(QtGui.QWidget):
    """
    User ui for a Hotkey control.
    shows: label, checkbox if disablable, shortcut(s), controls to add, remove
        additional shortcuts, controls to change scope if that's enabled...
    
    cfg['label'] == 'Hotkeytest with a MsgBox'
    cfg['typ'] == 'hotkey':
    cfg['name'] == 'modnameHotkey1'
    cfg['enabled'] = True
    cfg['disablable'] = True
    cfg['key'] = 'Win+G'
    cfg['keyChange'] = True
    cfg['multiple'] = True
    cfg['scope'] = ''
    cfg['scopeChange'] = True
    # mode can be: ahk, file, key: to execute code, open up sth, send keystroke
    cfg['mode'] = 'ahk'
    """
    def __init__(self, cfg, mod):
        super(Draw, self).__init__()
        self.cfg = cfg
        self.mod = mod
        self._setupUi()
    
    def _setupUi(self):
        userCfg = self.mod.db.get(self.cfg['name'], self.mod.name)
        self.ctrllayout = QtGui.QHBoxLayout(self)
        # left, top, right, bottom
        self.ctrllayout.setContentsMargins(0, 0, 0, 0)
        self.labelBoxLayout = QtGui.QVBoxLayout()
        self.labelBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.labelLayout = QtGui.QHBoxLayout()
        if self.cfg['disablable']:
            state = self.mod.getCfgValue(self.cfg, userCfg, 'enabled')
            self.check = QtGui.QCheckBox(self)
            cbSize = 27
            self.check.setMinimumSize(QtCore.QSize(cbSize, cbSize))
            self.check.setMaximumSize(QtCore.QSize(cbSize, cbSize))
            self.check.setChecked(state)
            self.check.clicked.connect(self.hotkeyCheck)
            self.labelLayout.addWidget(self.check)
        self.label = QtGui.QLabel(self.cfg.get('label') or '', self)
        self.label.setWordWrap(True)
        self.label.setMinimumHeight(a2ctrl.lenM)
        self.labelLayout.addWidget(self.label)
        self.labelBoxLayout.addLayout(self.labelLayout)
        self.labelBoxLayout.addItem(QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))
        self.ctrllayout.addLayout(self.labelBoxLayout)
        
        self.hotkeyListLayout = QtGui.QVBoxLayout()
        self.hotkeyLayout = QtGui.QHBoxLayout()
        #self.hotkeyButton = QtGui.QPushButton(self.data.get('key') or '')
        self.hotkeyButton = HotKey(self.mod.getCfgValue(self.cfg, userCfg, 'key'),
                                   self.hotkeyChange)
        self.hotkeyOption = QtGui.QPushButton()
        self.hotkeyOption.setMaximumSize(QtCore.QSize(a2ctrl.lenM, a2ctrl.lenM))
        self.hotkeyOption.setMinimumSize(QtCore.QSize(a2ctrl.lenM, a2ctrl.lenM))
        self.hotkeyOption.setFlat(True)
        self.hotkeyOption.setText('...')
        self.hotkeyLayout.addWidget(self.hotkeyButton)
        self.hotkeyLayout.addWidget(self.hotkeyOption)
        self.hotkeyButton.setEnabled(self.cfg['keyChange'])
        
#         self.hotkeyLayout.addItem(QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding,
#                                                     QtGui.QSizePolicy.Minimum))
        self.hotkeyListLayout.addLayout(self.hotkeyLayout)
        self.hotkeyListLayout.addItem(QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum,
                                                        QtGui.QSizePolicy.Expanding))
        self.ctrllayout.addLayout(self.hotkeyListLayout)
        self.ctrllayout.setStretch(2, 1)
        self.setLayout(self.ctrllayout)
        
    def hotkeyCheck(self):
        state = self.check.isChecked()
        self.mod.setUserCfg(self.cfg, 'enabled', state)
        self.mod.change()
    
    def hotkeyChange(self, newKey):
        log.info('cfg key: %s' % self.cfg['key'])
        log.info('newKey: %s' % newKey)
        self.mod.setUserCfg(self.cfg, 'key', newKey)
        self.mod.change()


class Edit(a2ctrl.EditCtrl):
    """
    TODO: Oh boy... this has so many implications but it has to be done. Let's do it!
    First: Have the edit ctrl, then the display one, Then we need checks when a mod
    config change is about to be comitted. The change will not be able to be OKed as long
    as there are conflicts with hotkeys, or missing includes or ...

    elif cfg['typ'] == 'hotkey':
        cfg['enabled'] = True
        cfg['disablable'] = True
        cfg['key'] = 'Win+G'
        cfg['keyChange'] = True
        cfg['multiple'] = True
        cfg['scope'] = ''
        cfg['scopeChange'] = True
        # mode can be: ahk, file, key
        # to execute code, open up sth, send keystroke
        cfg['mode'] = 'ahk',
        cfg['name'] = 'someModule_hotkey1',
        cfg['label'] = 'do awesome stuff on:'
    """
    def __init__(self, cfg, main):
        self.ctrlType = 'Hotkey'
        super(Edit, self).__init__(cfg, main, addLayout=False)
        self.main = main
        self.helpUrl = self.main.urls.helpHotkey
        self.cfg = cfg
        self.ui = hotkey_edit_ui.Ui_hotkey_edit()
        self.ui.setupUi(self.mainWidget)

        for label in [self.ui.internalNameLabel, self.ui.displayLabelLabel, self.ui.hotkeyLabel,
                      self.ui.functionLabel, self.ui.scopeLabel]:
            label.setMinimumWidth(a2ctrl.labelW)
        
        self.ui.hotkeyButton = HotKey(cfg.get('key') or '', self.hotkeyChange)
        self.ui.hotkeyKeyLayout.insertWidget(0, self.ui.hotkeyButton)
        self.mainWidget.setLayout(self.ui.verticalLayout_2)

        self.functions = ['functionCode', 'functionURL', 'functionSend']
        self.ui.cfg_functionMode.currentIndexChanged.connect(self.functionSetText)
        self.functionMenu = QtGui.QMenu(self.ui.functionButton)
        self.functionMenu.aboutToShow.connect(self.functionMenuBuild)
        self.ui.functionButton.setMenu(self.functionMenu)
        self.functionSetText()
        self.ui.functionText.textChanged.connect(self.functionChanged)
        
        self.ui.cfg_scopeMode.currentIndexChanged.connect(self.scopeModeChanged)
        self.scopeModeChanged()
        
        self.ui.scopePlus.mousePressEvent = self.scopePopup
        self.ui.scopeMinus.clicked.connect(self.scopeDelete)
        self.ui.cfg_scope.mouseDoubleClickEvent = partial(self.scopePopup, change=True)
        self.ui.cfg_scope.setFont(a2ctrl.fontL)
        self.connectCfgCtrls(self.ui)
        self.scopeUpdate()
        self.disablableCheck()
        self.ui.cfg_disablable.clicked.connect(self.disablableCheck)
    
    def functionMenuBuild(self):
        self.functionMenu.clear()
        index = self.ui.cfg_functionMode.currentIndex()
        if index == 0:
            fsubmenu1 = self.functionMenu.addMenu('local functions')
            _fsubmenu2 = self.functionMenu.addMenu('built-in functions')
        elif index == 1:
            for x in [('browse...', self.functionBrowse),
                      ('explore to...', self.functionExplore)]:
                action = QtGui.QAction(self.functionMenu)
                action.setText(x[0])
                action.triggered.connect(x[1])
                self.functionMenu.addAction(action)
        else:
            fsubmenu1 = self.functionMenu.addMenu('Send Mode')
            for x in ['Send', 'SendInput', 'SendRaw']:
                action = QtGui.QAction(fsubmenu1)
                action.setText(x)
                action.triggered.connect(partial(self.functionSendMode, x))
                fsubmenu1.addAction(action)
            #fsubmenu2 = self.functionMenu.addMenu('built-in variables')
            for x in [('Help on Send', self.functionSendHelp)]:
                action = QtGui.QAction(self.functionMenu)
                action.setText(x[0])
                action.triggered.connect(x[1])
                self.functionMenu.addAction(action)
    
    def functionSendMode(self, mode):
        self.cfg['sendmode'] = mode
    
    def functionBrowse(self):
        """TODO"""
        log.info('open a browser and all that ...')
        self.functionSetText(1, 'C:\asasasdf\asdfasdf')

    def functionExplore(self):
        """TODO: verify"""
        text = self.ui.functionText.text()
        subprocess.Popen(['explorer.exe', text])
    
    def functionSendHelp(self):
        self.main.surfTo(self.main.urls.ahksend)
    
    def functionChanged(self, text=None):
        #text = self.ui.functionText.text()
        index = self.ui.cfg_functionMode.currentIndex()
        self.cfg[self.functions[index]] = text
    
    def functionSetText(self, index=None, text=None):
        if index is None:
            index = self.ui.cfg_functionMode.currentIndex()
        if text is None:
            text = self.cfg.get(self.functions[index]) or ''
        self.ui.functionText.setText(text)
        # show include thingy
        #self.ui.scopePlus.setVisible(index == 0)
    
    def scopeModeChanged(self, index=None):
        if index is None:
            index = self.ui.cfg_scopeMode.currentIndex()
        state = index != 0
        self.ui.cfg_scope.setVisible(state)
        self.ui.scopePlus.setVisible(state)
        self.ui.scopeMinus.setVisible(state)

    def disablableCheck(self):
        """would be useless if hotkey is off by default and cannot be changed"""
        state = self.ui.cfg_disablable.isChecked()
        self.ui.cfg_enabled.setEnabled(state)
        self.ui.cfg_enabled.setChecked(True)
    
    def hotkeyChange(self, newKey):
        log.info('newKey: %s' % newKey)
        self.cfg['key'] = newKey

    def scopePopup(self, event, change=False):
        # to create new and change scope items from the list
        selItem = None
        text = ''
        if change:
            selItem = self.ui.cfg_scope.selectedItems()
            if not selItem:
                return
            text = selItem[0].text()

        self.scopePop = ScopeDialog(text, event.globalX(), event.globalY(),
                                    self.main, self.scopePopOK)
        self.scopePop.show()

    def scopePopOK(self):
        text = self.scopePop.ui.scopeText.text()
        if self.scopePop.edit:
            selItem = self.ui.cfg_scope.selectedItems()[0]
            selItem.setText(text)
        else:
            item = QtGui.QListWidgetItem(text)
            self.ui.cfg_scope.addItem(item)
            item.setSelected(True)
        self.scopePop.close()
        self.scopeUpdate()

    def scopeDelete(self):
        selIndex = [mi.row() for mi in self.ui.cfg_scope.selectedIndexes()][0]
        self.ui.cfg_scope.takeItem(selIndex)
        self.scopeUpdate()

    def scopeUpdate(self):
        allItems = a2ctrl.list_getAllItems_asText(self.ui.cfg_scope)
        p = a2ctrl.fontL.pointSize()
        h = ((max(1, len(allItems)) * p * a2ctrl.uiScale) + 20) * a2ctrl.uiScale
        self.ui.cfg_scope.setMinimumHeight(h)
        self.cfg['scope'] = allItems
    
    def getCfg(self):
        return self.cfg


class HotKey(QtGui.QPushButton):
    def __init__(self, key, func, parent=None):
        super(HotKey, self).__init__()
        
        self.setMinimumHeight(a2ctrl.lenM)
        self.setMaximumHeight(a2ctrl.lenM)
        self.setStyleSheet('QPushButton {background-color:#FFC23E}')
        self.key = key
        self.tempKey = key
        self.tempOK = True
        self.func = func
        self.setFont(a2ctrl.fontXL)
        #self.main = main
        self.setText(key)
        if parent is not None:
            parent.addWidget(self)
    
    def mousePressEvent(self, event):
        self.buildPopup(event.globalX(), event.globalY())

    def buildPopup(self, x, y):
        self.popup = a2ctrl.Popup(x, y, self)
        self.popup.textEdit = QtGui.QLineEdit(self.popup)
        self.popup.textEdit.setFont(a2ctrl.fontXL)
        self.popup.textEdit.setText(self.key)
        self.popup.textEdit.textChanged.connect(self.validateHotkey)
        self.popup.textEdit.returnPressed.connect(self.ok)
        
        self.popup.buttonLyt = QtGui.QHBoxLayout()
        self.popup.okButton = QtGui.QPushButton("OK")
        self.popup.okButton.clicked.connect(self.ok)
        self.popup.closeButton = QtGui.QPushButton("&Cancel")
        self.popup.closeButton.clicked.connect(self.popup.close)
        self.popup.buttonLyt.addWidget(self.popup.okButton)
        self.popup.buttonLyt.addWidget(self.popup.closeButton)
        
        self.popup.layout = QtGui.QVBoxLayout()
        self.popup.layout.addWidget(self.popup.textEdit)
        self.popup.layout.addLayout(self.popup.buttonLyt)
        self.popup.setLayout(self.popup.layout)
        self.validateHotkey(self.key)
        
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Enter), self.popup, self.ok)
        
        self.popup.show()
        self.popup.placeAtCursor()

    def ok(self):
        log.info('key: %s' % self.tempKey)
        log.info('ok: %s' % self.tempOK)
        if self.tempOK:
            self.key = self.tempKey
            self.popup.close()
            self.setText(self.key)
            self.func(self.key)

    def validateHotkey(self, hkstring):
        """
        first implementation: checks for valid modifyers + a single key
        TODO: handle F1-F12, Del, Home..., handle single keys when in scope, check availability ...
        """
        styleBad = '* {color:#F00}'
        styleGood = '* {color:#0F0}'
        good = False
        hkparts = hkstring.split('+')
        key = hkparts[-1].strip().lower()
        modifier = []
        tilde = ''
        # TODO: implement check for joystick keys and scancodes: 2joy4, SCnnn
        # http://www.autohotkey.com/docs/KeyList.htm#SpecialKeys
        if len(key) != 1 and key not in ahk.keys:
            msg = 'Invalid key! (%s)' % key
        elif len(hkparts) == 1:
            good = True
        else:
            modifier = [k.strip().lower() for k in hkparts[:-1]]
            if modifier[0].startswith('~'):
                tilde = '~'
                modifier[0] = modifier[0][1:]
            badModifier = [k for k in modifier if k not in ahk.modifiers]
            if badModifier:
                msg = ('Modifyer not one of Win, Ctrl, Alt or Shift! (%s)' % ', '.join(badModifier))
            else:
                good = True
        
        if not good:
            self.popup.textEdit.setStyleSheet(styleBad)
            log.error(msg)
        else:
            modifier = [k.title() for k in modifier]
            key = key.title()
            self.tempKey = tilde + '+'.join(modifier + [key])
            log.info('tempKey %s:' % self.tempKey)
            self.popup.textEdit.setStyleSheet(styleGood)
        
        self.tempOK = good


class ScopeDialog(QtGui.QDialog):
    def __init__(self, text, x, y, main, okFunc, *args):
        super(ScopeDialog, self).__init__(main)
        self.ui = scopeDialog_ui.Ui_ScopeDialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.okFunc = okFunc
        self.setWindowTitle('setup scope')
        self.main = main
        self.edit = text != ''

        self.getScopeNfo()
        self.setupUi(x, y)
        self.setScopeText(text)

    def setupUi(self, x, y):
        self.resize(self.width() * a2ctrl.uiScale, self.minimumSizeHint().height())
        pos = self.pos()
        pos.setX(x - (self.width() / 2))
        pos.setY(y - (self.height() / 2))
        self.move(pos)
        self.ui.scopeText.setStyleSheet('* {background-color:#E0E0E0}')
        for ui in [self.ui.scopeText, self.ui.okButton, self.ui.cancelButton]:
            ui.setFont(a2ctrl.fontXL)
        #for ui in [self.ui.helpButton, self.ui.titleButton, self.ui.classButton, self.ui.exeButton]:
        #    ui.setMinimumWidth(labelW)
        self.ui.okButton.clicked.connect(self.okFunc)
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.scopeTitle.setFocus()

        for ctrl in [self.ui.scopeTitle, self.ui.scopeClass, self.ui.scopeExe]:
            ctrl.textChanged.connect(self.textChange)
        # put menus to the different buttons
        for i, lst, ctrl in [(1, self.titles, self.ui.titleButton),
                             (2, self.classes, self.ui.classButton),
                             (3, self.processes, self.ui.exeButton),
                             (None, None, self.ui.helpButton)]:
            if lst:
                menu = QtGui.QMenu(self)
                usedmenu = QtGui.QMenu(menu)
                usedmenu.setTitle('all in use...')
                submenu = QtGui.QMenu(menu)
                submenu.setTitle('all available...')
                menu.addMenu(submenu)
                for item in sorted(lst, key=lambda s: s.lower()):
                    action = QtGui.QAction(item, submenu, triggered=partial(self.setScope, i, item))
                    submenu.addAction(action)
                ctrl.setMenu(menu)
            ctrl.setMinimumWidth(a2ctrl.labelW)

        menu = QtGui.QMenu(self)
        submenu = QtGui.QMenu(menu)
        submenu.setTitle('all in use...')
        for scope in sorted(self.main.getUsedScopes(), key=lambda s: s.lower()):
            action = QtGui.QAction(scope, submenu, triggered=partial(self.setScopeText, scope))
            submenu.addAction(action)
        menu.addMenu(submenu)
        for title, url in [('Help on Scope Setup', self.main.urls.helpScopes),
                           ('Help on AHK WinActive', self.main.urls.ahkWinActive),
                           ('Help on AHK WinTitle', self.main.urls.ahkWinTitle)]:
            action = QtGui.QAction(title, menu, triggered=partial(self.main.surfTo, url))
            menu.addAction(action)
        self.ui.helpButton.setMenu(menu)

    def setScopeText(self, text, *args):
        self.ui.scopeText.setText(text)
        # from given text fill the line edits already
        if text:
            for typ, ctrl in [('ahk_exe', self.ui.scopeExe), ('ahk_class', self.ui.scopeClass)]:
                found = text.find(typ)
                if found != -1:
                    ctrl.setText(text[found + len(typ):].strip())
                    text = text[:found]
            self.ui.scopeTitle.setText(text.strip())

    def textChange(self):
        texts = [self.ui.scopeTitle.text()]
        winclass = self.ui.scopeClass.text()
        if winclass:
            texts.append('ahk_class ' + winclass)
        winexe = self.ui.scopeExe.text()
        if winexe:
            texts.append('ahk_exe ' + winexe)
        self.ui.scopeText.setText(' '.join(texts).strip())

    def setScope(self, index, text):
        ctrls = [self.ui.scopeText, self.ui.scopeTitle, self.ui.scopeClass, self.ui.scopeExe]
        ctrls[index].setText(text)

    def getScopeNfo(self):
        # call AHK script to get all window classes, titles and executables
        scrpt = join(self.main.a2libdir, 'cmds', 'getScopeNfo.ahk')
        proc = subprocess.Popen([self.main.ahkexe, scrpt], shell=True, stdout=subprocess.PIPE)
        scopeNfo = str(proc.communicate()[0])
        # if ' were present in any title the quote sign will change
        scopeNfo = scopeNfo.strip()
        quoteChar = scopeNfo[-1]
        # cut away first & last quote char and linebreak
        scopeNfo = scopeNfo[scopeNfo.find(quoteChar) + 1:scopeNfo.rfind(quoteChar) - 2]
        scopeNfo = scopeNfo.split('\\n')
        self.titles = set()
        self.classes = set()
        self.processes = set()
        if not scopeNfo:
            log.error('Error getting scopeNfo!! scopeNfo: %s' % scopeNfo)
            return
        for i in range(0, len(scopeNfo), 3):
            if scopeNfo[i]:
                self.titles.add(scopeNfo[i])
            if scopeNfo[i + 1]:
                self.classes.add(scopeNfo[i + 1])
            if scopeNfo[i + 2]:
                self.processes.add(scopeNfo[i + 2])