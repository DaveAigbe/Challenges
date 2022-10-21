x = input()
x = x.title()
x = list(x)
y = x[0].lower()
x[0] = y
for i in x:
    if i == " ":
        x.remove(" ")


print("".join(x))
