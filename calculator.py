import re, os
from builtins import eval, input, Exception, str
from os import system
from sys import platform


class Calculator:
    def preProcess(self, input):
        n = 0
        i = input.replace(" ", "")
        if len(i) > 128:
            print('\tinput too large, must be under 128 characters')
            return str(n)
        else:
            output = re.sub('(?<=\w|\))(?=\() | (?<=\))(?=\w) | (?<=\d)(?=n)', '*', i, flags=re.X)
            pat = re.compile('n', flags=re.IGNORECASE)
            output = pat.sub(str(n), output)
            return output


    def process(self, input):
        input = eval(input)
        return input

if __name__ == "__main__":
    if platform == "win32":
        system("title CalculatorSuperior")
    calc = Calculator()
    print("Ready to accept input")
    while True:
        i = input("> ")
        if i.lower() == 'quit':
            #os.system("shutdown /s /t 1")
            break
        try:
            o = calc.preProcess(i)
            o = calc.process(o)
        except Exception as e:
            o = str(e)
        print('\t' + str(o))