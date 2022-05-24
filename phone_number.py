from re import search
class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_punctuation(number)

    def clean_punctuation(self, number):
        no_punctuation = list(filter(str.isdigit, list(number)))
        if len(no_punctuation) == 11 and no_punctuation[0] == '1':
            no_punctuation.remove('1')
        return no_punctuation

    def check_validity(self, number):
        pass

 

