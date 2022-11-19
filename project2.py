# Baiguullgiin Taniltsuulga
class Baiguullga():
    def __init__(self,name,bvtets,tsagiinhuwaari,hayg,mail,number,vilajillagaa):
        self.name = name
        self.bvtets = bvtets
        self.tsagiinhuwaari = tsagiinhuwaari
        self.hayg = hayg
        self.mail = mail
        self.number = number
        self.vilajillagaa = vilajillagaa

list_1 = Baiguullga('GS 25','20 hvnii bvreldehvvntei zahiral menijr nybo hamgaalach engineer busad ajilchid ','08:00 - 18:00','Hoimor office','Gs25@gmail.com','77777777','vilchilgeenii baigullaga')

print(list_1.name)
print(list_1.bvtets)
print(list_1.tsagiinhuwaari)
print(list_1.hayg)
print(list_1.mail)
print(list_1.number)
print(list_1.vilajillagaa)

# Web site  link
class Web():
    def __init__(self,link):
        self.link = link

link_1 = Web('https://gs25.mn/')

print(link_1.link)

#Ajilchidiin medeelel
class Employee():
    def __init__(self,name,age,salary,mail,number):
        self.name = name
        self.age = age
        self.salary = salary
        self.mail = mail
        self.number = number

emp_1 = Employee('sheiriw','30','5500000','gsheiriw0210@gmail.com','88117273') #Zahiral
emp_2 = Employee('Bold','29','450000','bold21@gmail.com','89896744') #Menijrr
emp_3 = Employee('pvrew','39','3500000','pvrew39@gmail.com','89896743') # Nygtlan bodogch
emp_4 = Employee('svren','49','1500000','svren49@gmail.com','89896742') # Hamgaalagch
emp_5 = Employee('miigaa','59','2500000','miigaa59@gmail.com','89896741') # Engineer

print(emp_1.name)
print(emp_1.age)
print(emp_1.salary)
print(emp_1.mail)
print(emp_1.number)

print(emp_2.name)
print(emp_2.age)
print(emp_2.salary)
print(emp_2.mail)
print(emp_2.number)

print(emp_3.name)
print(emp_3.age)
print(emp_3.salary)
print(emp_3.mail)
print(emp_3.number)

print(emp_4.name)
print(emp_4.age)
print(emp_4.salary)
print(emp_4.mail)
print(emp_4.number)

print('''
emp_5.name
emp_5.age
emp_5.salary
emp_5.mail
emp_5.number
''')
#Ajilsan tsag tootsoh
class Irts():
    def __init__(self,name,come_time,went_time):
        self.name = name
        self.come_time = come_time
        self.went_time = went_time
           
Come_time = int(input("Irsen tsagaa oruul:"))
Went_time= int(input("Yawsan tsagaa oruul:"))
print("Ajilsan tsag:",(Went_time - Come_time))

#Ajiltnii medeell oruulah gargah
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