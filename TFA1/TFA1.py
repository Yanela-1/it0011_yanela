#3.1
'''
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

print("Full Name: ", fname + " " + lname )
print("Sliced Name: ", fname[0:2] )
greetings = "Hello, {}! Welcome. You are {} years old."
print(greetings.format(fname[0:2], age))
'''
#3.2
'''
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print("Full Name: ", fname + " " + lname)
print("Full Name (Upper Case) :", (fname + " " + lname).upper())
print("Full Name (Lower Case) :", (fname + " " + lname).lower())
print("Length of Full name: ", len(fname + " " + lname))
'''

#3.3
lname = input("Enter last name: ")
fname = input("Enter first name: ")
age = input("Enter age: ")
cnumber = input("Enter contact number: ")
course = input("Enter course: ")

f=open("TFA1\students.txt", "a+")
f.write("Last name: " + lname)
f.write("First name: " + fname)
f.write("Age: " + age)
f.write("Contact Number: " + cnumber)
f.write("Course: " + course)
f.close()

print("Student information has been saved to 'students.txt'.")