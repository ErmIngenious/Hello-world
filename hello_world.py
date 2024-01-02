'''
ask users name and store this input in 
a variable and print name.
ask users age store this input in a variable and print age
print the string Hello World on a new line.
'''

#greets and asks for user name then stores this in a variable. 
name = input("Welcome. Please enter your name: " )

# greets user personally
print ("Hello " + name)

#asks for user name then stores this in a variable
age = input("next, please tell me your age:")

#asks for user interest then stores this in a variable
interest = input("and finally what subject are you interested in learning more about? ")

#thanks the user and concatenates all strings to confirm inputs.
print (f"Thank you {name}, so your are {age} and you are interested in learning more about {interest}")

#print hello world on a new line
print ("hello world")