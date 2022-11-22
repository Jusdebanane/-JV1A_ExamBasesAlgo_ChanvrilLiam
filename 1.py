#1
MyTable = [1,8,21,22,95,56,42]
save = 0

save = MyTable[0]
MyTable[0]= MyTable[3]
MyTable[3] = save
print(MyTable)
input()

#2
MyTable = [1,8,21,22,95,56,42]
save = 0

for i in range(1,len(MyTable)):
    if (MyTable[i]<MyTable[i-1]):
        save = MyTable[i]
        MyTable[i]=MyTable[i-1]
        MyTable[i-1]=save
print(MyTable)
input()

#3
MyTable = [1,8,21,22,95,56,42]
save = 0

for j in range(1,len(MyTable)):
    for i in range(1,len(MyTable)):
        if (MyTable[i]<MyTable[i-1]):
            save = MyTable[i]
            MyTable[i]=MyTable[i-1]
            MyTable[i-1]=save
print(MyTable)
input()

#4
#A chaque boucle "j" on parcours a nouveau tout le tableau et meme s'il est déjà trié