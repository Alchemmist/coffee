import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from db import get_all_coffee


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite3")

        self.add_header_to_table()
        self.update_table()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
