class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_emp(self, name, age, salary):
        emp = Employee(name, age, salary)
        self.employees.append(emp)

    def print_emp_list(self):

        print('\n** Employees List **')
        for employee in self.employees:
            print(f'Employee  : {employee.name} has an age of {employee.age} and salary  of {employee.salary} .')
        if len(self.employees) == 0:
            print('No employees yet ):')

    def delete_age(self, start_age, end_age):
        # for index,value in enumerate(self.employees):
        #     if start_age <= value.age<=end_age:
        #         print('Deleting ->  ',value.name)
        #         print()
        #         self.employees.pop(index)
        indx = 0
        while indx < len(self.employees):
            if start_age <= self.employees[indx].age <= end_age:
                print("Deleting -> ", self.employees[indx].name)
                self.employees.pop(indx)
            else:
                indx += 1

    def update_salary(self, emp_name, salary):
        name_exit = False
        for name in self.employees:
            if name.name == emp_name:
                name.salary = salary
                name_exit = True
                break

        if not name_exit:
            print("Error : Employee not found")


employes = EmployeeManager()


class FrontendManager:
    while True:
        print('\n'
              'Program Options : \n'
              '1) Add a new Employee\n'
              '2) List all Employees\n'
              '3) Delete by age range\n'
              '4) Update salary give a name\n'
              '5) End the program')
        task = input("Enter your choice (from 1 to 5 ) : ")

        if task.isdigit():
            task=int(task)
            if 1 <= task <= 5:

                if task == 1:
                    print('\nEnter employee data :')
                    emp_name = input("Enter Employee name : ")
                    emp_age = int(input('Enter Employee age : '))
                    emp_salary = int(input('Enter Employee salary : '))
                    employes.add_emp(emp_name, emp_age, emp_salary)
                elif task == 2:
                    employes.print_emp_list()
                elif task == 3:
                    start_age = int(input("\nEnter Age from : "))
                    end_age = int(input('Enter Age to : '))
                    employes.delete_age(start_age, end_age)
                elif task == 4:
                    emp_name = input('\nEnter employee name : ')
                    n_salary = int(input("Enter the new salary : "))
                    employes.update_salary(emp_name, n_salary)
                elif task == 5:
                    print("\n***** Thank you for using my service , have a great day *****")
                    break
            else:

                print("Error : please choose the correct option -> invalid range")


        else:
            print('Invalid input : Try again ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    FrontendManager()
