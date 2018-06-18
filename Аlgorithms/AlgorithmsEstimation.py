


class AlgorithmsEstimation:

    def __init__(self, candidate_words):
        self.candidate_words = candidate_words
        self.DefiChar()

    def Estimation(self):
        self.IOport = TextIO()
        self.UppdateOccurrence()
        self.Calc_Meas_Keywords()