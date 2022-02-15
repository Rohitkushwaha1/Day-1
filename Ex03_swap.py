# Write a program that switches/swap the values stored in the variable a and b.

# solution:

a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

print("Before Swaping a and b")
print("a:",a)
print("b:",b)

c = a # Taking another variable so the we can store value of a. 
a = b # After storing a into c store b into a. Till now c = a and a = b.
b = c # Stored the value of c to b because c havign the value of a.

print("After Swaping a and b")
print("a:",a)
print("b:",b)
