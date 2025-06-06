# class Programmers:
#     # class‑level defaults
#     language = ".net"
#     salary = 56000
#     company = "Microsoft"

#     def __init__(self, name, salary=salary, language=language, company=company):
#         self.name = name
#         self.salary = salary
#         self.language = language
#         self.company = company
#         print("I am a Microsoft employee")

#     def getinfo(self):
#         print(f"This language is {self.language}. The salary is {self.salary}")

#     @staticmethod
#     def greet():
#         print("Hello, good morning!")


# # --------------- objects ---------------
# manpreet = Programmers("Manpreet", 56000, ".net")   # OK: name, salary, language
# manpreet.greet()
# manpreet.getinfo()
# print(manpreet.name, manpreet.salary, manpreet.company, manpreet.language)

# samdeep = Programmers("Samdeep", 56000, ".net")     # same order
# samdeep.getinfo()
# print(samdeep.name, samdeep.salary, samdeep.company, samdeep.language)


class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")
    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n ** 0.5}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")
a = Calculator(4)
a.square()
a.squareroot()
a.cube()    
