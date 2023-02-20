from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from data_types import CoffeeInf, CoffeeKind


class TableChangeDialog(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)

    def _clear(self) -> None:
        self.sort.setText("")
        self.degree_of_roasting.setText("")
        self.kind.setCurrentIndex(0)
        self.taste_description.setText("")
        self.price.setValue(0)
        self.volume.setValue(0.0)

    def _update(self, data: CoffeeInf) -> None:
        self.sort.setText(data.sort)
        self.degree_of_roasting.setText(data.degree_of_roasting)
        self.kind.setCurrentIndex(0 if data.kind == CoffeeKind.GROUND else 1)
        self.taste_description.setText(data.taste_description)
        self.price.setValue(data.price)
        self.volume.setValue(data.volume)

    def ready(self) -> CoffeeInf:
        if self.kind.currentText() == "молотый":
            kind = CoffeeKind.GROUND
        else:
            kind = CoffeeKind.BEANS

        result = CoffeeInf(
            sort=self.sort.text(),
            degree_of_roasting=self.degree_of_roasting.text(),
            kind=kind,
            taste_description=self.taste_description.text(),
            price=self.price.value(),
            volume=self.volume.value(),
        )
        return result
