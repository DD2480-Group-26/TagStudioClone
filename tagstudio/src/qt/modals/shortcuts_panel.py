from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QFormLayout, QKeySequenceEdit, QLabel, QVBoxLayout, QWidget
from src.qt.widgets.panel import PanelWidget


class ShortcutSettingsPanel(PanelWidget):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.setMinimumSize(320, 200)

        # Layout for the panel
        self.root_layout = QVBoxLayout(self)
        self.root_layout.setContentsMargins(6, 0, 6, 0)

        # Container for form items
        self.form_container = QWidget()
        self.form_layout = QFormLayout(self.form_container)
        self.form_layout.setContentsMargins(0, 0, 0, 0)

        # Example shortcut: "Add Tag" action
        add_tag_label = QLabel("Add Tag Shortcut:")
        self.add_tag_shortcut_edit = QKeySequenceEdit()
        # Load the existing shortcut from QSettings
        current_shortcut = self.driver.settings.value("shortcuts/add_tag", defaultValue="T")
        self.add_tag_shortcut_edit.setKeySequence(current_shortcut)
        self.form_layout.addRow(add_tag_label, self.add_tag_shortcut_edit)

        self.root_layout.addWidget(self.form_container)
        self.root_layout.addStretch(1)

    def save_shortcuts(self):
        add_tag_shortcut = self.add_tag_shortcut_edit.keySequence().toString()
        self.driver.settings.setValue("shortcuts/add_tag", add_tag_shortcut)
        self.driver.settings.sync()

        if self.driver.add_tag_to_selected_action:
            self.driver.add_tag_to_selected_action.setShortcut(QKeySequence(add_tag_shortcut))
            self.driver.add_tag_to_selected_action.setToolTip(add_tag_shortcut)
