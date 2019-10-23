import os
import re
from builtins import eval, input, Exception, str
from sys import platform


class Calculator:
    def preProcess(self, input, n):
        i = input.replace(" ", "")
        if len(i) >= 128:
            raise Exception('input too large, must be under 128 characters')
        else:
            output = re.sub(r'(?<=\w|\))(?=\() | (?<=\))(?=\w) | (?<=\d)(?=n) | (?<=n)(?=\w)', '*', i.lower(), flags=re.X)
            output = output.replace('n', str(n))
            return output

    def process(self, input):
        input = eval(input)

        input = '{:.15f}'.format(float(input)).rstrip('0')  # Forces precision to 15 digits and remove trailing 0s
        if input[-1] == '.':
            input = input[:-1]

        return input


if __name__ == "__main__":
    if platform == "win32":
        os.system("title CalculatorSuperior")
    calc = Calculator()
    print("Ready to accept input")
    n = 0
    while True:
        i = input("> ")
        if i.lower() == 'quit':
            #os.system("shutdown /s /t 1")
            break
        try:
            o = calc.preProcess(i, n)
            o = calc.process(o)
            n = o
        except Exception as e:
            o = str(e)
        print('\t' + str(o))