
def get_user_name():
    name = input("What is your name? ")
    print("hello")
    print(name)
    return name
    # Inside the function

#Outside the function
print("Hello")
get_user_name() # Calling the function

print("-----------------------------------")

def get_user_name2():
    name2 = input("What is your name? ")
    return name2
    # Inside the function

#Outside the function
print("Hello")
name2 = get_user_name2() # Calling the function
print("hello")
print(name2)

print("-----------------------------------")

name3 = ""
def get_user_name3():
    name3 = input("What is your name? ")
    # Inside the function

#Outside the function
print("Hello")
get_user_name3() # Calling the function
print("Hello")
print(name3)