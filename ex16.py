from sys import argv

script, filename = argv  # make a file e.g. ex16.txt and run with .py file
# python ex16.py ex16.txt

print(f"We're going to erase {filename},")
print("If you don't want that, hit CTRL-C (^C).")
print("iF you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three line.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
