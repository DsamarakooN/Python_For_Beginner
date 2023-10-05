# For Loop
# Repeats the block of statements a specified number of times

#format - for iterating_var sequence:
#              statements(s)      

#example 1
for i in [1,2,3,4,5]:
    print("This is a loop: i = ", i)

# range function
#can use for iterating in a for loop

#range(stop)
#range(start, stop)
#range(start, stop, step)

print(list(range(10)))
print(list(range(6,12)))
print(list(range(1, 30, 3)))

#write a program to compute the sum of all even numbers up to 100, including 100 using a loop
total = 0
for i in range(1,101,2):
    total = total + i
print('total = ',total)