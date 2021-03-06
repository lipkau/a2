'''
Created on Apr 1, 2016

@author: eRiC
'''
import a2ctrl.qlist
from PySide import QtGui, QtCore
from a2element import combo_edit_ui, DrawCtrl, EditCtrl


class Draw(DrawCtrl):
    def __init__(self, main, cfg, mod):
        super(Draw, self).__init__(main, cfg, mod)
        self.value = self.get_user_value(str)
        self.user_edit = self.cfg.get('user_edit', False)
        self._setupUi()

    def _setupUi(self):
        self.layout = QtGui.QHBoxLayout(self)
        self.label_text = self.cfg.get('label', '')
        self.label = QtGui.QLabel(self.label_text, self)
        self.layout.addWidget(self.label)

        self.value_ctrl = QtGui.QComboBox()
        if self.user_edit:
            items = self.get_user_value(list, 'items')
            self.value_ctrl.setEditable(True)
            self.value_ctrl.editTextChanged.connect(self.check_user_items)
        else:
            items = self.cfg.get('items', [])
        self.value_ctrl.addItems(items)
        self.value_ctrl.currentIndexChanged[str].connect(self.delayed_check)
        self.layout.addWidget(self.value_ctrl)

        if self.value in items:
            index = items.index(self.value)
            self.value_ctrl.setCurrentIndex(index)

    def check(self, value=None):
        if value is None:
            value = self.value_ctrl.currentText()

        # prevent being called double
        if self.value == value:
            return

        if self.user_edit:
            items = [self.value_ctrl.itemText(i) for i in range(self.value_ctrl.count())]
            self.set_user_value(items, 'items')

        self.value = value
        self.set_user_value(value, 'value')
        self.change('variables')
        super(Draw, self).check()

    def check_user_items(self, *args):
        raise NotImplementedError('Ohoh! I thought this was done already! :(')


class Edit(EditCtrl):
    """
    Checkbox to control boolean values for the a2 runtime.
    We might put them to the db and get and fetch from there or first: just write them into
    code directly and start with the variables include.
    """
    def __init__(self, cfg, main, parentCfg):
        super(Edit, self).__init__(cfg, main, parentCfg, add_layout=False)
        self.helpUrl = self.a2.urls.help_number

        self.ui = combo_edit_ui.Ui_edit()
        self.ui.setupUi(self.mainWidget)

        self.ui.plus_button.clicked.connect(self.add_item)
        self.ui.minus_button.clicked.connect(self.delete_item)

        self.check_new_name()
        a2ctrl.connect.cfg_controls(self.cfg, self.ui)

        for item in a2ctrl.qlist.get_all_items(self.ui.cfg_items):
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable |
                          QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)

        self.ui.cfg_items.itemChanged.connect(self.update_items)

    def add_item(self):
        current_items = a2ctrl.qlist.get_items_as_text(self.ui.cfg_items)
        new_item_name = 'new_item'
        item = QtGui.QListWidgetItem(new_item_name)
        current_items.append(new_item_name)
        self.update_items(items=current_items)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable |
                      QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)
        self.ui.cfg_items.addItem(item)
        self.ui.cfg_items.editItem(item)

    def delete_item(self):
        item_objs = self.ui.cfg_items.selectedItems()
        sel_items = [i.text() for i in item_objs]
        new_items = [i for i in self.cfg.get('items', []) if i not in sel_items]
        self.update_items(items=new_items)
        for item in item_objs:
            # doesnt doanything :(
            # self.ui.cfg_items.removeItemWidget(item)
            item_row = self.ui.cfg_items.row(item)
            self.ui.cfg_items.takeItem(item_row)

    def update_items(self, item=None, items=None):
        if item is not None:
            a2ctrl.qlist.select_items(self.ui.cfg_items, item)
            # item.setSelected(True)
        if items is None:
            items = a2ctrl.qlist.get_items_as_text(self.ui.cfg_items)
        self.cfg['items'] = items

    def keyPressEvent(self, event):
        """
        Capture delete key to remove entries
        """
        if event.key() == QtCore.Qt.Key_Delete:
            self.delete_item()
        return EditCtrl.keyPressEvent(self, event)

    @staticmethod
    def element_name():
        return 'ComboBox'

    @staticmethod
    def element_icon():
        return a2ctrl.Icons.inst().combo


def get_settings(module_key, cfg, db_dict, user_cfg):
    db_dict.setdefault('variables', {})
    value = a2ctrl.get_cfg_value(cfg, user_cfg, 'value', typ=str, default='')
    db_dict['variables'][cfg['name']] = value
