# ---------------- Parent Class ----------------
class Employee:  
    Company_name = 'Google'   # Class variable (shared by all employees)


    def __init__(self, names, age, Emp_id):
        self.names = names     
        self.age = age         
        self.Emp_id = Emp_id    
        


# ---------------- Child Class ----------------
class Manager(Employee):


    def __init__(self, names, age, Emp_id, employee=None):
        # Call parent constructor to initialize common attributes
        super().__init__(names, age, Emp_id)

        # If no employee role list is given, create empty list
        if employee is None:
            self.employee = []
        else:
            self.employee = employee 

    # Method to add a new employee role
    def add_employee_role(self, emp):
        # Add role only if it does not already exist
        if emp not in self.employee:
            self.employee.append(emp)

    # Method to remove employee role
    def remove_employee_role(self, emp):

        # Check if role exists in list
        if emp in self.employee:
            # Get index of that role
            index = self.employee.index(emp)

            # Remove role from role list
            self.employee.remove(emp)
            
            # Remove corresponding name, age, and ID using same index
            self.names.pop(index)
            self.age.pop(index)
            self.Emp_id.pop(index)

    # Method to print all employee details
    def print_all_employee_role(self):
        self.c = 0   # Counter to track index

        # Loop through employee roles
        for emp in self.employee:
            # Print role, name, and age
            print("-->", emp, self.names[self.c], self.age[self.c])
            self.c += 1


# ---------------- Data ----------------
names = ['A','B','C','D','E','F']  
age = [16,18,19,14,15,20]               
emp_id = [1001,1002,1003,1004,1005,1006]  
employeee = ['IT','HR','Coock','DEV','AiE','Cloud'] 


# Create Manager object
emp = Manager(names, age, emp_id, employeee)

# Remove employee with role 'HR'
emp.remove_employee_role('HR')

# Print remaining employees
emp.print_all_employee_role()
