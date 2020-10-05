"""48.Decorators"""


def div(a, b):
    print(a / b)


def smart_div(n):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return n(a, b)

    return inner


div1 = smart_div(div)
div1(2, 4)

