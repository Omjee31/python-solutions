'''
Diamond Problem

Create:

class A → method show()

class B(A)

class C(A)

class D(B, C)

👉 Print:

print(D.__mro__)
'''
class A:

    def show(self):
        return"A Is running"

class B(A):
    def car(self):
        return "B Is running "
class C(A):
    def bike(self):
        return f"C Is running"

class D(B,C):
    def main(self):
        return "D Is running"

print(D.__mro__)
