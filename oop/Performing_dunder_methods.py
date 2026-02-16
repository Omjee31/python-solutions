class Student:
    Bank_Name = "SBI"  # class variable (shared by all objects)

    def __init__(self, balance, fname, lname):
        self.fname = fname      # instance variable
        self.lname = lname
        self.balance = balance

    @property   # getter
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @property
    def show_balance(self):
        return f"Your Balance in {self.Bank_Name} is {self.balance}"



    @classmethod   # modifies class variable
    def change_Bank(cls, New_Bank_name):
        cls.Bank_Name = New_Bank_name

    def __add__(self, other):   # + operator overloading
        return self.balance + other.balance

    def __sub__(self, other):   # - operator overloading
        return self.balance - other.balance

    def __len__(self):  # must return integer only
        return len(self.fullname)

    def __str__(self):  # for user-friendly printing
        return f"Student Name: {self.fullname}"
    # def __repr__(self):  # I pass Deposit method in this and it runs
        #return f"Student {self.fullname} Bank NAme is {self.Bank_Name}  Balance is {self.show_balance} {self.deposit(9000)}"
        


    def __repr__(self):  # for developer/debug representation
        return f"Student('{self.balance}', '{self.fname}', '{self.lname}')"

    def __eq__(self,other):
        return self.balance == other.balance
#-------------------Main Function-----------------------------
def main():
    S1 = Student(9000,'Omjee','Singh') # passing Instance to class 
    S2 = Student(5000,'Rahul','gupta')
    print(S1+S2)
    print(S1-S2)
    print(len(S1))
    print(str(S1))
    print(repr(S1))
    print(S1.balance)
    print("Is S1 And S2 Balance Equal ? ",(S1==S2))
    
if __name__=="__main__":
    main()
