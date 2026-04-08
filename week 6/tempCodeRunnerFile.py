# positional argument
print("positional argument")
def add(a,b):
     print("sum" , a+b)

add(4,4)

# keyword argument
print("keyword argument")
def student(name , age):
    print("name : " , name)
    print("age : " , age)
student(age = 18 , name = "Barun" )

#default argument
print("default argument")
def greet(name = "student"):
    print("hello " , name)
greet()
greet("Barun")

#variable length argument
print("variable length argument")
def total(*numbers):
    print("numbers : " , numbers)

total(10,20,30,40)
