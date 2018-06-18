from Thematic_dictionary.TextIO import TextIO
from Thematic_dictionary.TermDictionary import TermDictionary


class DefinitionCharacteristics:

    def __init__(self, candidate_words):
        self.candidate_words = candidate_words
        self.DefiChar()

    def DefiChar(self):
        self.IOport = TextIO()
        self.UppdateOccurrence()
        self.Calc_Meas_Keywords()

    def Calc_Meas_Keywords(self):
        for key_w in self.candidate_words:
            (self.candidate_words[key_w]).append(1)
        d = TermDictionary()
        key_diction = d.ReturnsDictionary()

        for key_w in key_diction:
            if key_w in self.candidate_words:
                (self.candidate_words[key_w][2]) = 1 / self.candidate_words[key_w][1]

        print(self.candidate_words)
        print('Fin Calc_Meas_Keywords')

    def UppdateOccurrence(self):
        pass

# base_text = TextIO()
# f = DefinitionCharacteristics(base_text.ReadJson('Text_dis_alg.json'))