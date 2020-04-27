#!/usr/bin/python3

from my_pkg.module1 import *
from my_pkg.module2 import *

choice = 0

while choice != 3:
    print("<Select menu>")
    print("1) conversion")
    print("2) union/intersection")
    print("3) exit")
    choice = int(input("what is your choice: "))

    if choice == 1:
        bin_tmp = input("input binary number: ")
        bin_changer(bin_tmp)

    if choice == 2:
        list1 = input("1st list: ")
        list2 = input("2nd list: ")
        tmplist1 = clean(list1)        
        tmplist2 = clean(list2)

        interfunction(tmplist1, tmplist2)
        unionfunction(tmplist1, tmplist2)
    if choice == 3:
        print("good bye!")
        break

    print("")




