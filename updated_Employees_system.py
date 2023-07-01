def input_valid_int(msg,start=0,end=None):
    while True:
        inp=input(msg)
        if not inp.isdecimal():
            print('Invalid input . Try again !')
        elif start is not None and end is not None :
            if not (start<=int(inp)<=end):
                print('Invalid range . try again ')
            else:
                return int(inp)
        else:
            return int(inp)





class Emloyee:
    def __init__(self,name,age,salary):
        self.name,self.age,self.salary=name,age,salary

    def __str__(self):
        return f'Employee :{self.name} has age {self.age} and salary {self.salary}'

    def __repr__(self):
        return f'Employee (name = "{self.name}" , age= "{self.age} , salary="{self.salary}" '




class EmploeesManager:
    def __init__(self):
        self.employees=[]

    def add_employee(self,name,age,salary):

        self.employees.append(Emloyee(name,age,salary))

    def list_employees(self):
        if len(self.employees)==0:
            print('\nNo employees at the moment!')
            return

        print('\n***Employees lists***')
        for emp in self.employees:
            print(emp)

    def delete_employees_with_range(self,age_from,age_to):
        for idx in range(len(self.employees)-1,-1,-1):
            emp=self.employees[idx]
            if age_from<=emp.age<=age_to:
                print('\nDeleting',emp.name)
                self.employees.pop(idx)

    def find_employee_by_name(self,name):
        for emp in self.employees:
            if emp.name==name:
                return emp
            return None

    def update_salary_by_name(self,name,salary):
        emp=self.find_employee_by_name(name)
        if emp is None :
            print('Error : no employee with such a name ')
        else:
            emp.salary=salary



class FrontendManager:
    def __init__(self):
        self.employees_manager=EmploeesManager()
    def print_menu(self):
        print('\nProgram Options : ')
        messages=[
                  '1) Add a new employee ',
                  '2) List all employees ',
                  '3) Delete by age range',
                  '4) Update salary given a name',
                  '5) End the program '
        ]
        print('\n'.join(messages))
        msg=f'Enter your choice (from 1 to {len(messages)} : '
        return input_valid_int(msg,1,len(messages))

    def run(self):
        while True:
            choice=self.print_menu()
            if choice==1:
                print('\nEnter employee data : ')
                name = input('Enter Employee name : ')
                age = int(input('Enter Employee age :'))
                salary = int(input('Enter Employee salary :'))
                self.employees_manager.add_employee(name,age,salary)
            elif choice==2:
                self.employees_manager.list_employees()

            elif choice==3:
                age_from=input_valid_int('Enter age from')
                age_to=input_valid_int('Enter age to')
                self.employees_manager.delete_employees_with_range(age_from,age_to)
            elif choice==4:
                name=input('Enter name : ')
                salary=input_valid_int('Enter new salary :')
                self.employees_manager.update_salary_by_name(name,salary)
            else:
                break



if __name__=='__main__':
    app=FrontendManager()
    app.run()