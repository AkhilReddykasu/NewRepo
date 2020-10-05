"""__name__"""
from Calc import add1


def fun1():
    add1()
    print("from fun1")


def fun2():
    print("from fun2")


def main():
    fun1()
    fun2()


main()
