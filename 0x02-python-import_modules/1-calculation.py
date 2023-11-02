#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calculator
    a = 10
    b = 5
    add = calculator.add(a, b)
    sub = calculator.sub(a, b)
    mul = calculator.mul(a, b)
    div = calculator.div(a, b)
    print("{} + {} = {}".format(a, b, add))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))
