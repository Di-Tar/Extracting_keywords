# -*- coding: utf-8 -*-
import codecs
import json


class TextIO:

    # Считывание текста из фала
    def ReadTeaxt(self, addresIn):
        self.addresIn = addresIn
        with codecs.open(self.addresIn, 'r', "utf_8_sig") as file:
            IntermText = [row for row in file]

        IntermText = [line.rstrip() for line in IntermText]

        self.InputText = ""
        for part in IntermText:
            if part[-1] == '-':
                self.InputText += part[:-1]
            else:
                self.InputText += part + ' '

        print('Fin ReadTeaxt')
        return self.InputText

    def WriteJson(self, text, addresOut):
        self.addresOut = addresOut
        with codecs.open(self.addresOut, 'w', "utf_8_sig") as OutFile:
            json.dump(text, OutFile, ensure_ascii=False, indent = 4, sort_keys = True)
        print('Fin WriteJson')

    def ReadJson(self, addresIn):
        self.addresIn = addresIn
        with codecs.open(self.addresIn, 'r', "utf_8_sig") as InFile:
            InputText = json.load(InFile, )

        print('Fin ReadJson')
        return InputText

# Testing

# t = TextIO('tren_text_1.txt')
# t.ReadTeaxt()
