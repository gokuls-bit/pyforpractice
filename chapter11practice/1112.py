# class tdvector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")

# class tredvector(tdvector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

# # Create and display 2D vector
# a = tdvector(1, 2)
# a.show()

# # Create and display 3D vector
# b = tredvector(1, 2, 3)
# b.show()

# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Pets(Animal):
#     def category(self):
#         print("This is a pet")

# class Dog(Pets):
#     def bark(self):
#         print("Woof! Woof!")

# # Example usage:
# d = Dog()
# d.speak()      # Inherited from Animal
# d.category()   # Inherited from Pets
# d.bark()       # Defined in Dog


class Employee:
    salary = 564
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))

e = Employee()
print(e.salaryAfterIncrement)  # This will raise an error because salaryAfterIncrement is not defined as a method