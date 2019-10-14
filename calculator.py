import os
import re
from builtins import eval, input, Exception, str


class Calculator:
    def preProcess(self, input):
        n = 0
        output = re.sub('(?<=\w|\))(?=\() | (?<=\))(?=\w) | (?<=\d)(?=n)', '*', input, flags=re.X)
        pattern = re.compile('n', flags=re.IGNORECASE)
        output = pattern.sub(str(n), output)

        return output


    def process(self, input):
        input = eval(input)
        return input

if __name__ == "__main__":
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