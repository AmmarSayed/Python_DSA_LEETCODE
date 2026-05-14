
################## immutable objects, so they are passed by value
num1 = 11
num2 = num1

print("before num2 value is updated:")
print("num1:", num1)
print("num2:", num2)
# same value and same memory address
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


num1 = 22
# the value of num1 is updated, but the value of num2 is not updated because they point to different memory addresses, Integers are immutable objects, so when we update the value of num1, it creates a new memory address for num1 and num2 still points to the old memory address where the value is 11

print("\nafter num1 value is updated:") 
print("num1:", num1)
print("num2:", num2)
# different value and different memory address
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


################## lists are mutable objects, so they are passed by reference
dict1 = { 'value': 11  }
dict2 = dict1

print("\nbefore dict2 value is updated:")
print("dict1:", dict1)  
print("dict2:", dict2)
# same value and same memory address
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict1['value'] = 22

# The value of dict1 is updated, so the value of dict2 is also updated because they point to the same memory address, Dictionaries are mutable objects, so when we update the value of dict1, it updates the value at the same memory address where dict2 also points to, so both dict1 and dict2 reflect the updated value.
print("\nafter dict1 value is updated:")
print("dict1:", dict1)
print("dict2:", dict2)
# same value and same memory address
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


################## swapping values of two variables
number1 = 50
number2 = 60

print("\nbefore number1 is updated:")
print("number1:", number1)
print("number2:", number2)

# swapping the values of number1 and number2
# temp = number1
# number1 = number2
# number2 = temp

# quick way to swap the values of number1 and number2
number1, number2 = number2, number1
print("\nafter number1 is updated:")
print("number1:", number1)
print("number2:", number2)