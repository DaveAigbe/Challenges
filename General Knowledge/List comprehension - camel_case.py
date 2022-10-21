
emlist=[]
case = 'DogWork'
cm=""


for letter in (case):
   if letter.isupper():
       emlist.append('_')
       emlist.append(letter)
   else:
       emlist.append(letter)
if emlist[0] == '_':
    emlist.pop(0)



print((cm.join(emlist)).lower())


