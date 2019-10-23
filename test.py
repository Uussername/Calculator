import unittest

from calculator import Calculator


class MyTestCase(unittest.TestCase):
    preProcessTests = [
        # [input, n, output],
        ['1 + 1', 0, '1+1'],
        ['1 - 1', 0, '1-1'],
        ['1 / 0', 0, '1/0'],
        ['1 * 2', 0, '1*2'],
        ['1 / 2', 0, '1/2'],
        ['2(1 + 1)', 0, '2*(1+1)'],
        ['(2 + 2) + (1 + 1)', 0, '(2+2)+(1+1)'],
        ['2 / 1 * 2', 0, '2/1*2'],
        ['(1 / 2)NN(3 + 4)', 6, '(1/2)*6*6*(3+4)'],
        ['1 + N', 0, '1+0'],
        ['(48 * 3)(1 / 3)n(51.3)N', 42, '(48*3)*(1/3)*42*(51.3)*42'],
        ['1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1', 0, '1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1'],
        ['1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 - 1', 0, 'input too large, must be under 128 characters'],

        ['99999 * 9999999 * 9999999', 0, '99999 * 9999999 * 9999999'],
        [':D', 0, 'syntax error'],
        ['1 / 510000', 0, '1/510000'],
        ['n2', 2, '2*2'],
        ['nnn', 2, '2*2*2']
    ]

    processTests = [
        # [input, output],
        ['1+1', 2],
        ['1-1', 0],
        ['1/0', ' / 0 error'],  # TODO: Find real error string
        ['1*2', 2],
        ['1/2', .5],
        ['2*(1+1)', 4],
        ['(2+2)+(1+1)', 6],
        ['2/1*2', 4],
        ['(1/2)*6*6*(3+4)', 126],
        ['1+126', 127],
        ['(48*3)*(1/3)*127*(51.3)*127', (48*3)*(1/3)*127*(51.3)*127],
        ['1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1', -62],

        # ['1-1-1-1-1-1-1-1-1-1-1-1-1-1-
        # 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-
        # 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-
        # 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1', 'Character limit error']

        ['99999*9999999*9999999', 'Number too large'],
        ['1/510000', '0.000001960784314'],
    ]

    def test_preProcessInput(self):
        for (input, n, output) in self.preProcessTests:
            with self.subTest(input):
                calc = Calculator()
                calc.n = n
                print(n)
                self.assertEqual(calc.preProcess(input, n), output, input)

    def test_processInput(self):
        for (input, output) in self.processTests:
            with self.subTest(input):
                calc = Calculator()
                if isinstance(output, str):
                    self.assertEqual(calc.process(input), output, input)
                else:
                    self.assertEqual(float(calc.process(input)), output, input)


if __name__ == '__main__':
    unittest.main()
