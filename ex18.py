# this one is like your scripts with argv
def print_two(*args): # "*" take alle arguments which are
    arg1, arg2 = args # № of arguments in line 22 
    print(f"arg1: {arg1}, arg2: {arg2}") # get arguments from line 22


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # take two arguments wich put on ()
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
