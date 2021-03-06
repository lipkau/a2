"""
a2 path control
"""
from PySide import QtGui

import a2ctrl
from a2element import path_edit_ui, DrawCtrl, EditCtrl
from a2widget import a2path_field


class Draw(DrawCtrl):
    def __init__(self, main, cfg, mod):
        super(Draw, self).__init__(main, cfg, mod)
        self.value = self.get_user_value(str)
        self._setupUi()

    def _setupUi(self):
        self.main_layout = QtGui.QHBoxLayout(self)
        self.label_text = self.cfg.get('label', '')
        self.label = QtGui.QLabel(self.label_text, self)
        self.value_ctrl = a2path_field.A2PathField(self, value=self.value)
        self.value_ctrl.changed.connect(self.check)
        self.value_ctrl.writable = self.cfg.get('writable', False)
        self.value_ctrl.file_types = self.cfg.get('file_types', '')
        self.value_ctrl.browse_type = self.cfg.get('browse_type', '1')
        self.value_ctrl.save_mode = self.cfg.get('save_mode', False)

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.value_ctrl)

    def check(self, value=None):
        if value is None:
            value = self.value_ctrl.text()

        # prevent being called double
        if self.value == value:
            return

        self.value = value
        self.set_user_value(value)
        self.change('variables')


class Edit(EditCtrl):
    def __init__(self, cfg, main, parentCfg):
        super(Edit, self).__init__(cfg, main, parentCfg, add_layout=False)
        self.helpUrl = self.a2.urls.help_path

        self.ui = path_edit_ui.Ui_edit()
        self.ui.setupUi(self.mainWidget)

        self.check_new_name()
        a2ctrl.connect.cfg_controls(self.cfg, self.ui)
        self._adjust_path_field()
        for ctrl in [self.ui.cfg_writable, self.ui.cfg_browse_type_0, self.ui.cfg_browse_type_1,
                     self.ui.cfg_save_mode]:
            ctrl.clicked.connect(self._adjust_path_field)
        self.ui.cfg_file_types.editingFinished.connect(self._adjust_path_field)

    def _adjust_path_field(self):
        self.ui.cfg_value.writable = self.cfg.get('writable', False)
        self.ui.cfg_value.file_types = self.cfg.get('file_types', '')
        self.ui.cfg_value.browse_type = self.cfg.get('browse_type', a2path_field.BrowseType.file)
        self.ui.cfg_value.save_mode = self.cfg.get('save_mode', False)

        self.ui.cfg_file_types.setEnabled(self.ui.cfg_value.browse_type == a2path_field.BrowseType.file)
        self.ui.cfg_save_mode.setEnabled(self.ui.cfg_value.browse_type == a2path_field.BrowseType.file)

    @staticmethod
    def element_name():
        return 'Path'

    @staticmethod
    def element_icon():
        return a2ctrl.Icons.inst().folder


def get_settings(module_key, cfg, db_dict, user_cfg):
    db_dict.setdefault('variables', {})
    value = a2ctrl.get_cfg_value(cfg, user_cfg, typ=str, default='')
    db_dict['variables'][cfg['name']] = value
