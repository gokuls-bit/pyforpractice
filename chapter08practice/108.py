# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# c = int(input("enter a number: "))

# def greatest(a,b,c):
#     if (a>b and a >c):
#         return a 
#     elif(b>a and b>c):
#         return b 
#     elif(c>a and c>b):
#         return c 
# print(greatest(a,b,c))

# def conversion():
#   tempc = int(input("enter a temperature : "))
#   tempf = (tempc*33.8)
#   print (" new temperature is:" ,tempf)
# conversion()


# print("a")
# print("b")
# print("c", end = "")
# print("d", end = "")

# def sum(n):
#     if(n==1):
#         return 1 
#     return sum(n-1)+n
# print(sum(4))

# def pattern(n):
#     if(n==0):
#          return
#     print("*"* n)
#     pattern(n-1)
# pattern(3)

# def conversion():
#    inch = int(input("enter a measurement : "))
#    cm = (inch*2.54)
#    print (" new measurement is:  cm " ,cm)
# conversion()
# def rem(l, word ):
#      n = []
#      for item in l:
#              if not (item==word):
#                 n.append(item.strip(word))
#      return n 
# l = ["manjeet","gurjeet","majhithia ","gunjan", "simaranjeet"]
# print(rem(l,"an"))
def multiply(n):
    for i in range (1, 11):
       print(f"{n}*{i}={n*i}") 
multiply(12)     