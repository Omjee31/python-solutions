class Employee:  # Creating Class
    hike_percent = 8   # Class Variable (shared by all employees)

    def __init__(self, first_name, last_name, salary):
        # Instance variables (unique for each object)
        self.f_name = first_name
        self.l_name = last_name
        self.salary = salary
        # Creating email automatically
        self.email = first_name + last_name + '@gmail.com'

    def fullname(self):
        # Returns full name of employee
        return f"{self.f_name} {self.l_name}"

    def display(self):
        # Display employee details
        print("Employee Details --:")
        
        # Use self.fullname(), NOT Emp_1.fullname() you should always use self, not a specific object name.
        print("Employee Name Is", self.fullname(), "Email Is", self.email)
        
        return f"Salary Of {self.fullname()} Is {self.salary}"

    def salary_hike(self):
        # Calculate salary after hike using class variable
        
        new_salary = self.salary + self.salary * (self.hike_percent / 100)
        
        return f"Salary After Hike Is {new_salary} of {self.fullname()}"


# Creating object
Emp_1 = Employee('omjee', 'singh', 89000) 

# Calling methods
print(Emp_1.fullname())
print(Emp_1.display())
print(Emp_1.salary_hike())
