from Thematic_dictionary.TextIO import TextIO


class TermDictionary:

    def ReturnsDictionary(self):
        IOport = TextIO()
        return IOport.ReadJson('udk_504117.json')