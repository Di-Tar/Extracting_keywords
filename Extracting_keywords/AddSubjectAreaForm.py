#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QGridLayout


class AddSubjectAreaForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        but_subject_area = QPushButton("Добавить предметную область")

        leb2 = QLabel("УДК код")
        leb3 = QLabel("Нименование")

        udk_code = QLineEdit(self)
        naming = QLineEdit(self)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(leb2, 2, 0)
        grid.addWidget(udk_code, 2, 1)
        grid.addWidget(leb3, 3, 0)
        grid.addWidget(naming, 3, 1)
        grid.addWidget(but_subject_area, 4, 0)

        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle('Добавление предметной области')
        self.show()
