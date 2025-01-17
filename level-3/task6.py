class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return f"Class A {self.a + self.b}"
    
class B(A):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return f"Class B {self.a + self.b}"
    
    def minus(self):
        return f"Class B {self.a - self.b}"
    
class C(B):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return f"Class C {self.a + self.b}"
    
    def minus(self):
        return f"Class C {self.a - self.b}"
    
    def multiplication(self):
        return f"Class C {self.a * self.b}"
    
class D(B, A):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return f"Class D {self.a + self.b}"
    
    def minus(self):
        return f"Class D {self.a - self.b}"
    
    def multiplication(self):
        return f"Class D {self.a * self.b}"

# self
a = A(3,5)
print(a.add())
print("============")

# sinle inheritance
b = B(5,2)
print(b.add())
print(b.minus())
print("============")

# multiple inheritance
c = C(7,3)
print(c.add())
print(c.minus())
print(c.multiplication())
print("============")

# multilevel inheritance
d = D(9,5)
print(d.add())
print(d.minus())
print(d.multiplication())
print("============")