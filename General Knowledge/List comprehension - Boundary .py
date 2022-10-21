#Write a program that divides numbers into two lists depending on whether they are greater than or less than 5. You don't have to include number 5 itself.

# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = [x for x in numbers if x < 5]
greater_than_5 = [x for x in numbers if x > 5]

# printing your results
print(less_than_5)
print(greater_than_5)