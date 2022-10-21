"""Given a numeric sequence, create a list in which each number will be a digit from this input string.
Then use this list to calculate the running total, or cumulative sum.
Essentially, it's a new list of partial sums that gets updated every time a new element appears.

For example, we can transform the list [1, 2, 3, 4] to [1, 1 + 2, 1 + 2 + 3, 1+2+3+4], which equals to [1, 3, 6, 10]."""

nums = [int(x) for x in input('Enter your values, seperated by spaces: ').replace(' ', '')]
new = []
counter = 1
for i in nums:
    new.append(sum(nums[:counter]))
    counter += 1




print(new)

