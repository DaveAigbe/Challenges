x = "AWUBWUBWUBBWUBWUBWUBC"
final = (x.split('WUB'))
finished = []
for i in final:
    if i != '':
        finished.append(i)
print(final)
print(" ".join(finished))


