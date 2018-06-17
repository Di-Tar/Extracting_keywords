# -*- coding: utf-8 -*-


class IOInterface:

    def __init__(self, addres):
        self.addres = addres


    def InputText(self):
        with open(self.addres, 'r') as file:
            t = [row.strip().lower() for row in file]
            print(t)