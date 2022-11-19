class Employee:
    employeelist = list()
    def __init__(self, empNo , empName, empDes , empSal) -> None:
        self.empNo ,self.empName , self.empDes , self.empSal = empNo , empName , empDes , empSal
    def addNewEmployee(self):
        Employee.employeelist.append(self)
    def Emplist(self):
        return Employee . employeelist
    def getEmpById(self ,empNo):
        for emp in Employee.employeelist:
            if(emp.getEmpNo() == empNo):
                return emp
            return False 
    def setEmpNo(self ,empNo):
        self.empNo = empNo
    def getEmpNo(self):
        return self . empNo
    def setEmpName(self,empName):
        self.empName = empName
    def getEmpName(self):
        return self.empName
    def setEmpDes (self , empDes):
        self.empDes = empDes
    def getEmpDes(self):
        return self.empDes
    def setEmpSal(self,empSal):
        self.empsal = empSal
    def getEmpSal(self):
        return self.empSal
    def __str__(self):
        return "%d %s %s %d" % (self.empNo ,self.empName, self.empDes , self.empSal)

choice = 1
employee = Employee(0, "", "", 0.0)
while choice >= 1 and choice <= 3 :
    print("\n\n 1 . Ажилтан нэмэх \n 2 . Ажилчидийн жагсаалт харах \n 3 . Ажилтанг ID р нь хайх : \n\n")
    choice = int(input("Та алийг нь сонгох вэ ? :"))
    if (choice == 1):
        empNo = int(input("Ажилтний номерийг оруулан уу :"))
        empName = (input("Ажилтний нэрийг оруулах:"))
        empDes = (input("Ажилтний албан тушаалийг оруулах :"))
        empSal = float(input("Ажилтний цалинг оруулах : "))
        emp = Employee(empNo , empName , empDes , empSal)
        emp.addNewEmployee()

    elif(choice == 2):
        print(empNo ,empName ,empDes , empSal)
        for emp in employee.getEmpList():
            print(empNo ,empName ,empDes , empSal)
        
    elif(choice == 3):
        empNo = int(input("Ажилтний номерийг оруулан уу : "))
        employee.getEmpById(empNo)
        if (emp == False):
            print("\nУучилаарай ажилтний ID олдсонгүй ...! : " , empNo)
        else:
            print(emp)