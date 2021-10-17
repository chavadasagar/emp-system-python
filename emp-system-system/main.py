import os
from typing import Container
import controller


controller.user_is_valid()


while True:
    os.system("cls")
    print("\t0.exit program")
    print("\t1.add employee")
    print("\t2.update employeclse")
    print("\t3.delete employee")
    print("\t4.show all employee")
    print("\t5.show show specific")
    print("\t6.search")

    ch = input("\n\tEnter Your Choice :")

    if ch == '0':
        break
    elif ch == '1':
        controller.addemp()
        input()
    elif ch == '2':
        input()
    elif ch == '3':
        controller.del_emp()
        input()
    elif ch == '4':
        controller.showall()
        input()
    elif ch == '5':
        controller.show_specific()
        input()
    elif ch == '6':
        controller.search()
        input()
    else:
        print("\t\t*** please enter valid choice")
