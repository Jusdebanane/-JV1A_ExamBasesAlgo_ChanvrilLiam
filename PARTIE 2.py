#1
A=[".",".","."]
B=[".",".","."]
C=[".",".","."]
Grille=[A,B,C]
for i in range(0,len(Grille)):
    print(Grille[i])

#2
COL=[" ","A","B","C"]
A=["D",".",".","."]
B=["E",".",".","."]
C=["F",".",".","."]
Grille=[COL,A,B,C]
for i in range(0,len(Grille)):
    print(Grille[i])
player="X"
save= ''
pos= ''

print("CROIX ou ROND?")
print("1: X / 2:O")
save=input()
if(save==1):
    player="X"
if(save==2):
    player="O"


for i in range(0,len(Grille)):
    print(Grille[i])

#3




