import os
from builtins import eval, input, Exception, str


class Calculator:
    def preProcess(self, input):
        output = input  # TODO: Actually edit the input
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
            os.system("shutdown /s /t 1")
            break
        try:
            o = calc.preProcess(i)
            o = calc.process(o)
        except Exception as e:
            o = str(e)
        print('\t' + str(o))