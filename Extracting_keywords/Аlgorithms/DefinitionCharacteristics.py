# -*- coding: utf-8 -*-
import re


class DefinitCharact:

    def __init__(self, text):
        self.text = text

    def Tokenization(self):
        t_text = []
        for num_sentence in range(self.text.size):
            sentence = re.split('[^a-z]', self[num_sentence])
            t_sentence = []
            for num_words in range(len(sentence)):
                if sentence[num_words] != '':
                    t_sentence.append(sentence[num_words])
            t_text.append(t_sentence)
        return t_text
