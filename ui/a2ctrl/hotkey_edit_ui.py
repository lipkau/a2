# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2ctrl\hotkey_edit.ui'
#
# Created: Wed Feb 24 15:21:34 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_hotkey_edit(object):
    def setupUi(self, hotkey_edit):
        hotkey_edit.setObjectName("hotkey_edit")
        hotkey_edit.resize(785, 425)
        self.verticalLayout_2 = QtGui.QVBoxLayout(hotkey_edit)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setContentsMargins(10, 5, 0, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.internalNameLayout = QtGui.QHBoxLayout()
        self.internalNameLayout.setSpacing(10)
        self.internalNameLayout.setObjectName("internalNameLayout")
        self.internalNameLabel = QtGui.QLabel(hotkey_edit)
        self.internalNameLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.internalNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.internalNameLabel.setObjectName("internalNameLabel")
        self.internalNameLayout.addWidget(self.internalNameLabel)
        self.cfg_name = QtGui.QLineEdit(hotkey_edit)
        self.cfg_name.setObjectName("cfg_name")
        self.internalNameLayout.addWidget(self.cfg_name)
        self.verticalLayout_2.addLayout(self.internalNameLayout)
        self.displayLabelLayout = QtGui.QHBoxLayout()
        self.displayLabelLayout.setSpacing(10)
        self.displayLabelLayout.setObjectName("displayLabelLayout")
        self.displayLabelLabel = QtGui.QLabel(hotkey_edit)
        self.displayLabelLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.displayLabelLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.displayLabelLabel.setObjectName("displayLabelLabel")
        self.displayLabelLayout.addWidget(self.displayLabelLabel)
        self.cfg_label = QtGui.QLineEdit(hotkey_edit)
        self.cfg_label.setObjectName("cfg_label")
        self.displayLabelLayout.addWidget(self.cfg_label)
        self.verticalLayout_2.addLayout(self.displayLabelLayout)
        self.hotkeyLayout = QtGui.QHBoxLayout()
        self.hotkeyLayout.setSpacing(10)
        self.hotkeyLayout.setContentsMargins(-1, -1, -1, 10)
        self.hotkeyLayout.setObjectName("hotkeyLayout")
        self.hotkeyLabelLayout = QtGui.QVBoxLayout()
        self.hotkeyLabelLayout.setObjectName("hotkeyLabelLayout")
        self.hotkeyLabel = QtGui.QLabel(hotkey_edit)
        self.hotkeyLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.hotkeyLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.hotkeyLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hotkeyLabel.setObjectName("hotkeyLabel")
        self.hotkeyLabelLayout.addWidget(self.hotkeyLabel)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.hotkeyLabelLayout.addItem(spacerItem)
        self.hotkeyLayout.addLayout(self.hotkeyLabelLayout)
        self.hotkeyKeyLayout = QtGui.QVBoxLayout()
        self.hotkeyKeyLayout.setSpacing(0)
        self.hotkeyKeyLayout.setObjectName("hotkeyKeyLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.cfg_enabled = QtGui.QCheckBox(hotkey_edit)
        self.cfg_enabled.setChecked(True)
        self.cfg_enabled.setObjectName("cfg_enabled")
        self.gridLayout.addWidget(self.cfg_enabled, 0, 0, 1, 1)
        self.cfg_disablable = QtGui.QCheckBox(hotkey_edit)
        self.cfg_disablable.setChecked(True)
        self.cfg_disablable.setObjectName("cfg_disablable")
        self.gridLayout.addWidget(self.cfg_disablable, 3, 0, 1, 1)
        self.cfg_keyChange = QtGui.QCheckBox(hotkey_edit)
        self.cfg_keyChange.setChecked(True)
        self.cfg_keyChange.setObjectName("cfg_keyChange")
        self.gridLayout.addWidget(self.cfg_keyChange, 0, 1, 1, 1)
        self.cfg_multiple = QtGui.QCheckBox(hotkey_edit)
        self.cfg_multiple.setChecked(True)
        self.cfg_multiple.setObjectName("cfg_multiple")
        self.gridLayout.addWidget(self.cfg_multiple, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.hotkeyKeyLayout.addLayout(self.gridLayout)
        self.hotkeyLayout.addLayout(self.hotkeyKeyLayout)
        self.hotkeyLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.hotkeyLayout)
        self.functionLayout = QtGui.QHBoxLayout()
        self.functionLayout.setSpacing(10)
        self.functionLayout.setContentsMargins(-1, -1, -1, 10)
        self.functionLayout.setObjectName("functionLayout")
        self.functionLabelLayout = QtGui.QVBoxLayout()
        self.functionLabelLayout.setObjectName("functionLabelLayout")
        self.functionLabel = QtGui.QLabel(hotkey_edit)
        self.functionLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.functionLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.functionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.functionLabel.setObjectName("functionLabel")
        self.functionLabelLayout.addWidget(self.functionLabel)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.functionLabelLayout.addItem(spacerItem1)
        self.functionLayout.addLayout(self.functionLabelLayout)
        self.functionCtrlLayout = QtGui.QVBoxLayout()
        self.functionCtrlLayout.setSpacing(6)
        self.functionCtrlLayout.setContentsMargins(-1, -1, -1, 0)
        self.functionCtrlLayout.setObjectName("functionCtrlLayout")
        self.functionRowLayout = QtGui.QHBoxLayout()
        self.functionRowLayout.setContentsMargins(-1, 0, -1, -1)
        self.functionRowLayout.setObjectName("functionRowLayout")
        self.cfg_functionMode = QtGui.QComboBox(hotkey_edit)
        self.cfg_functionMode.setObjectName("cfg_functionMode")
        self.cfg_functionMode.addItem("")
        self.cfg_functionMode.addItem("")
        self.cfg_functionMode.addItem("")
        self.functionRowLayout.addWidget(self.cfg_functionMode)
        self.functionButton = QtGui.QPushButton(hotkey_edit)
        self.functionButton.setMaximumSize(QtCore.QSize(50, 35))
        self.functionButton.setObjectName("functionButton")
        self.functionRowLayout.addWidget(self.functionButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.functionRowLayout.addItem(spacerItem2)
        self.functionCtrlLayout.addLayout(self.functionRowLayout)
        self.functionText = QtGui.QLineEdit(hotkey_edit)
        self.functionText.setObjectName("functionText")
        self.functionCtrlLayout.addWidget(self.functionText)
        self.functionLayout.addLayout(self.functionCtrlLayout)
        self.functionLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.functionLayout)
        self.scopeLayout = QtGui.QHBoxLayout()
        self.scopeLayout.setSpacing(10)
        self.scopeLayout.setContentsMargins(-1, -1, -1, 10)
        self.scopeLayout.setObjectName("scopeLayout")
        self.scopeLabelLayout = QtGui.QVBoxLayout()
        self.scopeLabelLayout.setObjectName("scopeLabelLayout")
        self.scopeLabel = QtGui.QLabel(hotkey_edit)
        self.scopeLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.scopeLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.scopeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scopeLabel.setObjectName("scopeLabel")
        self.scopeLabelLayout.addWidget(self.scopeLabel)
        spacerItem3 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.scopeLabelLayout.addItem(spacerItem3)
        self.scopeLayout.addLayout(self.scopeLabelLayout)
        self.scopeCtrlLayout = QtGui.QVBoxLayout()
        self.scopeCtrlLayout.setSpacing(5)
        self.scopeCtrlLayout.setContentsMargins(-1, -1, -1, 5)
        self.scopeCtrlLayout.setObjectName("scopeCtrlLayout")
        self.scopeRowLayout = QtGui.QHBoxLayout()
        self.scopeRowLayout.setSpacing(9)
        self.scopeRowLayout.setContentsMargins(-1, 0, -1, -1)
        self.scopeRowLayout.setObjectName("scopeRowLayout")
        self.cfg_scopeMode = QtGui.QComboBox(hotkey_edit)
        self.cfg_scopeMode.setObjectName("cfg_scopeMode")
        self.cfg_scopeMode.addItem("")
        self.cfg_scopeMode.addItem("")
        self.cfg_scopeMode.addItem("")
        self.scopeRowLayout.addWidget(self.cfg_scopeMode)
        self.scopePlus = QtGui.QPushButton(hotkey_edit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scopePlus.sizePolicy().hasHeightForWidth())
        self.scopePlus.setSizePolicy(sizePolicy)
        self.scopePlus.setMaximumSize(QtCore.QSize(50, 35))
        self.scopePlus.setObjectName("scopePlus")
        self.scopeRowLayout.addWidget(self.scopePlus)
        self.scopeMinus = QtGui.QPushButton(hotkey_edit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scopeMinus.sizePolicy().hasHeightForWidth())
        self.scopeMinus.setSizePolicy(sizePolicy)
        self.scopeMinus.setMaximumSize(QtCore.QSize(50, 35))
        self.scopeMinus.setObjectName("scopeMinus")
        self.scopeRowLayout.addWidget(self.scopeMinus)
        self.cfg_scopeChange = QtGui.QCheckBox(hotkey_edit)
        self.cfg_scopeChange.setChecked(True)
        self.cfg_scopeChange.setObjectName("cfg_scopeChange")
        self.scopeRowLayout.addWidget(self.cfg_scopeChange)
        spacerItem4 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.scopeRowLayout.addItem(spacerItem4)
        self.scopeCtrlLayout.addLayout(self.scopeRowLayout)
        self.cfg_scope = QtGui.QListWidget(hotkey_edit)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cfg_scope.sizePolicy().hasHeightForWidth())
        self.cfg_scope.setSizePolicy(sizePolicy)
        self.cfg_scope.setMinimumSize(QtCore.QSize(0, 40))
        self.cfg_scope.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cfg_scope.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cfg_scope.setObjectName("cfg_scope")
        self.scopeCtrlLayout.addWidget(self.cfg_scope)
        self.scopeLayout.addLayout(self.scopeCtrlLayout)
        self.scopeLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.scopeLayout)

        self.retranslateUi(hotkey_edit)
        QtCore.QMetaObject.connectSlotsByName(hotkey_edit)

    def retranslateUi(self, hotkey_edit):
        hotkey_edit.setWindowTitle(QtGui.QApplication.translate("hotkey_edit", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.internalNameLabel.setText(QtGui.QApplication.translate("hotkey_edit", "internal name:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_name.setText(QtGui.QApplication.translate("hotkey_edit", "extensionX_hotkey1", None, QtGui.QApplication.UnicodeUTF8))
        self.displayLabelLabel.setText(QtGui.QApplication.translate("hotkey_edit", "display label:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_label.setText(QtGui.QApplication.translate("hotkey_edit", "make some awesome stuff", None, QtGui.QApplication.UnicodeUTF8))
        self.hotkeyLabel.setText(QtGui.QApplication.translate("hotkey_edit", "hotkey:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_enabled.setText(QtGui.QApplication.translate("hotkey_edit", "enabled by default", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_disablable.setText(QtGui.QApplication.translate("hotkey_edit", "can be disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_keyChange.setText(QtGui.QApplication.translate("hotkey_edit", "can be changed", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_multiple.setText(QtGui.QApplication.translate("hotkey_edit", "allow multiple hotkeys", None, QtGui.QApplication.UnicodeUTF8))
        self.functionLabel.setText(QtGui.QApplication.translate("hotkey_edit", "function:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_functionMode.setItemText(0, QtGui.QApplication.translate("hotkey_edit", "run code", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_functionMode.setItemText(1, QtGui.QApplication.translate("hotkey_edit", "open file/url", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_functionMode.setItemText(2, QtGui.QApplication.translate("hotkey_edit", "send keystroke", None, QtGui.QApplication.UnicodeUTF8))
        self.functionButton.setText(QtGui.QApplication.translate("hotkey_edit", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeLabel.setText(QtGui.QApplication.translate("hotkey_edit", "scope:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeMode.setItemText(0, QtGui.QApplication.translate("hotkey_edit", "global", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeMode.setItemText(1, QtGui.QApplication.translate("hotkey_edit", "only in:", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeMode.setItemText(2, QtGui.QApplication.translate("hotkey_edit", "not in:", None, QtGui.QApplication.UnicodeUTF8))
        self.scopePlus.setText(QtGui.QApplication.translate("hotkey_edit", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.scopeMinus.setText(QtGui.QApplication.translate("hotkey_edit", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.cfg_scopeChange.setText(QtGui.QApplication.translate("hotkey_edit", "can be changed", None, QtGui.QApplication.UnicodeUTF8))

