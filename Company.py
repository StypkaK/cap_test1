from tkinter import E


class Company:
    class Employer:
        # first_name = ("Adam")
        # last_name = ("Nowak")
        # age = 29
        # job = ("tester")
        # salary = 2020.0
        # bonus = 100.0        
        # total_salary = salary + bonus


        def __init__(self, first_name, last_name, age, job, salary, bonus):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.job = job
            self.salary = salary
            self.bonus = bonus
            self.total_salary = salary + bonus
        

        def applybonus(self):
            self.bonus = float(input("Podaj wartość bonusu: "))
            self.total_salary=self.salary+self.bonus

    class Department:
        def __init__(self, name, users):
            self.name = name
            self.users = users

        def display_employers(self):
            for i in self.users:    
                print(i.first_name + " " + i.last_name)

    department_list = []
    name_ddd = "Pierwszy"
        
        

    pracownik_1 = Employer("Adam", "Nowak", 16, "tester", 220.0, 15.0)
    print(pracownik_1.total_salary)

    pracownik_1.applybonus()
    print(pracownik_1.total_salary)
    pracownik_2 = Employer("Kamil", "Bocian", 55, "developer", 4500, 15000)
    
    employees_list = []
    employees_list.append(pracownik_1)
    employees_list.append(pracownik_2)

    department_1 = Department("Pierwszy", employees_list)
    department_2 = Department("Drugi", [])

    department_1.display_employers()

    department_list.append(department_1)
    department_list.append(department_2)

    def display_departments(_list):
        for i in _list:
            print(i.name)

    display_departments(department_list)

    def add_employee(self, name, last_name, age, job, salary, bonus):
        new_user = Employer(name, last_name, age, job, salary, bonus)
        self.employees_list.append(new_user)
        print("User " + name +" has been added")
    

    def add_department(self, name, users):
        new_department = Department(name, users)
        self.department_list.append(new_department)
        print("Department has been added")

    def remove_department(self, name):
        # self.department_list.remove(name)
        for idx, i in enumerate(self.department_list):
            if i.name == name:
                self.department_list.pop(idx-1)
        print("Department has been removed")

    remove_department(name_ddd)
    display_departments(department_list)

