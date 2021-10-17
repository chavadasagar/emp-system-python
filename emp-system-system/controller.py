import mysql.connector
import mod.addemp as add
import mod.show_specific as spe
import mod.removeemp as remove
import mod.show_emp as fetch
import mod.search as find
import mod.login as check



def addemp():
    print("\n")
    name = input("\t\tEnter Name :")
    age = input("\t\tEnter Age :")
    phno = input("\t\tEnter Phone No :")
    print("\t\t1.male")
    print("\t\t2.female")
    gen = input("\t\tSelct Gender :")
    if gen == "1":
        gen = "male"
    else:
        gen = "female"

    print("\n")

    print("\t\t Verify Your info")
    print("\n")
    print("\t\t Name :",name)
    print("\t\t Age :",age)
    print("\t\t Phone No :",phno)
    print("\t\t Gender :",gen)


    q = input("\n\t\tit is a ok ?? y/n :")

    if(q == "y"):
        addemp = add.addemp(name,age,phno,gen)
        print("\t\tRegister Successfuly!!!!")        
    else:
        print("\n")
        print("\t\tok reenter your info ...")
        print("\n")
        return False


def del_emp():
    print("\n")
    id = input("\t\tEnter Your Id :")

    print("\n")

    obj = spe.show_specific(id)
    dataa = obj.show()

    print("\t\tinfo > ",dataa)

    q = input("\n\t\tIt is You ? y/n :")


    if(q == "y"):      
        msg = input("\n\t\tconfirm delete this employee ? y/n :")
        if(msg == "y"):
            delete = remove.remove_emp(id)
            print("\n")
            print("\t\tdelete successfuly!!!")
            dataa.clear()
            return True
        else:
            print("\n")
            print("\n\t\tOk ... ")
            dataa.clear()
            return False
    else:
        print("\t\tok Reenter your Id :")
        dataa.clear()
        return False
    
    


    
def showall():
    obj = fetch.show_emp()
    data = obj.alldata()

    print("\t\t all employee list\n")


    for x in data:
        print("\t\t",x,"\n")

def show_specific():
    print("\n")
    id =  input("\t\tEnter Id :")
    obj = spe.show_specific(id)

    print("\t\t",obj.show())

def search():
    print("\n")
    name = input("\t\tSearch : ")

    obj = find.search()
    result = obj.data(name)

    for x in result:
        print("\t\t",x)



def user_is_valid():
    obj = check.login()
    print("\n")
    print("\t\thi login First")
    username = input("\t\tUsername :")
    password = input("\t\tPassword :")
    if(obj.isvalid(username,password) == False):
        print("\t\t** username or password is wrong")
        user_is_valid()
    else:
        print("\t\tLogin successfuly!!!!")
