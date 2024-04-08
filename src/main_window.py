from PySide6.QtWidgets import QMainWindow, QMessageBox

from bandmerch import execute
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.gen_btn.clicked.connect(self.generate)

    def get_options(self):
        options = {}
        options["label"] = self.ui.label_edit.text()
        if self.ui.type_btns.checkedButton() is None:
            options["merch_types"] = None
        else:
            options["merch_types"] = []
            for btn in self.ui.type_btns.buttons():
                if btn.isChecked():
                    options["merch_types"].append(btn.text())
        options["sort_by"] = self.ui.sort_combo.currentText()
        options["sort_order"] = self.ui.sort_btns.checkedButton().text()
        options["include_sold_out"] = self.ui.include_sold_out_btn.isChecked()
        return options

    def generate(self):
        try:
            execute(self.get_options())
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.exec()
