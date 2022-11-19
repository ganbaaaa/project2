class Farm:
    employeelist = list()
    def __init__(self,chiken , dog, cow ,dodo) -> None:
        self.chiken , dog , cow , dodo = chiken , dog , cow, dodo
    def addNewAnimal(self):
        Farm.anoimallist.append(self)
    def Animallist(self):
        return Farm . animallist
    def getAnimalById(self ,chiken):
        for emp in Farm.animallist:
            if(emp.getChiken() == chiken):
                return emp
            return False 
    def setChiken(self ,chiken):
        self.chiken = chiken
    def getChiken(self):
        return self . chiken
    def setDog(self,dog):
        self.dog = dog
    def getDog(self):
        return self.dog
    def setCow(self , cow):
        self.cow = cow
    def getCow(self):
        return self.cow
    def setDodo(self,dodo):
        self.dodo = dodo
    def getDodo(self):
        return self . dodo
    def __str__(self):
        return "%d %s %s %d" % (self.chiken ,self.dog, self.cow , self.dodo)

choice = 1
while choice >= 1 and choice <= 3 :
    print("\n\n 1 . tahia awah \n 2 . nohoi awah  \n 3 . vher awah \n 4 . dodo shuwuu awah  \n\n")
    choice = int(input("Та алийг нь сонгох вэ ? :"))
    if (choice == 1):
        print("Ta odort 10 ondog gargadag tahia awlaa bayr hvrgey ")

    if( choice == 2):
        print("Ta jinken golden vvldriin nohoi awlaa bayr hvrgey")

    if(choice == 3):
        print("Ta saaliin saihan har tarlan vnee awlaa bayr hvrgey ")

    if (choice == 4):
        print("Ta hamgiin howor DODO shuwuug awlaa tand bayr hvrgey")


    def getMoney(self, money):
        self.money = money
    
         
        # empName = (input("Ажилтний нэрийг оруулах:"))
        # empDes = (input("Ажилтний албан тушаалийг оруулах :"))
        # empSal = float(input("Ажилтний цалинг оруулах : "))
        # emp = Farm(empNo , empName , empDes , empSal)
        # emp.addNewEmployee()

    # elif(choice == 2):
    #     print(empNo ,empName ,empDes , empSal)
    #     for emp in employee.getEmpList():
    #         print(empNo ,empName ,empDes , empSal)
        
    # elif(choice == 3):
    #     empNo = int(input("Ажилтний номерийг оруулан уу : "))
    #     employee.getEmpById(empNo)
    #     if (emp == False):
    #         print("\nУучилаарай ажилтний ID олдсонгүй ...! : " , empNo)
    #     else:
    #         print(emp)