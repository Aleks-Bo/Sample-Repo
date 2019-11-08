# from sys import argv

# script, filename = argv  # to run this script you
# must put "python ex15.py ex15_sample.txt"

# txt = open(filename)

# print(f"Here's your file {filename}:")
# print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
file_again = input("> ")
# txt_again.close()
