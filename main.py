import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from dialog import TableChangeDialog
from db import get_all_coffee, edit_coffee, add_coffee
from utils import convert_to_coffeeinf


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite3")
        self.add.clicked.connect(self.add_coffee)
        self.edit.clicked.connect(self.edit_table)

        self.add_header_to_table()
        self.update_table()

        self.dialog = TableChangeDialog()

    def add_header_to_table(self) -> None:
        headers = [
            "id",
            "сорт",
            "степень обжарки",
            "вид",
            "описание вкуса",
            "цена",
            "объём упаковки",
        ]
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(len(headers))

        for i, val in enumerate(headers):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(val)))

    def update_table(self) -> None:
        result = get_all_coffee(self.con)
        self.tableWidget.setRowCount(len(result) + 1)
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(val)))

    def add_coffee(self) -> None:
        self.dialog.done.disconnect()
        self.dialog.done.clicked.connect(self.finish_adding)
        self.dialog._clear()
        self.dialog.show()

    def finish_adding(self) -> None:
        new_data = self.dialog.ready()
        self.dialog.hide()
        self.dialog._clear()
        add_coffee(self.con, new_data)
        self.update_table()

    def edit_table(self) -> None:
        self.dialog.done.disconnect()
        self.dialog.done.clicked.connect(self.finish_editing)
        select_row_nuber = self.tableWidget.currentRow()
        if select_row_nuber != -1 and select_row_nuber != 0:
            data = []
            for i in range(self.tableWidget.columnCount()):
                data.append(self.tableWidget.item(select_row_nuber, i).text())
            self.ind = data[0]
            data = convert_to_coffeeinf(data[1:])
            self.dialog._update(data)
            self.dialog.show()

    def finish_editing(self) -> None:
        new_data = self.dialog.ready()
        self.dialog.hide()
        edit_coffee(self.con, new_data, self.ind)
        self.update_table()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
