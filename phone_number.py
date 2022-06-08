from curses.ascii import isalpha
from re import search
class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_punctuation(number)
# ['+', '.', '-', ' ', '(', ')']
    def letters(self, number):
        for item in number:
            if item.isalpha() == True:
                raise ValueError("letters not permitted")
#filter((lambda x: if x in ['+', '.', '-', ' ', '(', ')']: list.remove(x)) else, list(number))
#list comprehention: sq2 = [n ** 2 for n in range(10) if not n % 2]

    def clean_punctuation(self, number):
        no_punctuation = list(filter(str.isdigit, list(number)))
        if len(no_punctuation) > 11:
            raise ValueError('more than 11 digits')
        elif len(no_punctuation) < 11:
            raise ValueError('incorrect number of digits')
        elif len(no_punctuation) == 11 and no_punctuation[0] != '1':
            raise ValueError('11 digits must start with 1')
        elif len(no_punctuation) == 11 and no_punctuation[0] == '1': 
            no_punctuation.remove('1')
            clean_num = ''.join(no_punctuation)    
        return clean_num

    def check_validity(self, number):
        pass

#"incorrect number of digits"
#"11 digits must start with 1"
#"more than 11 digits"
#"letters not permitted"
#"punctuations not permitted"
#"area code cannot start with zero"
#"area code cannot start with one"
#"exchange code cannot start with zero"
#"exchange code cannot start with one"

    #area_code[0] in range(2, 10)
    #exchange_code[0] in range(2, 10)


 

