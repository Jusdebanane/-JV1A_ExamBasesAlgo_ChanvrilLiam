#1
A=[".",".","."]
B=[".",".","."]
C=[".",".","."]
Grille=[A,B,C]
for i in range(0,len(Grille)):
    print(Grille[i])

#2
A=[".",".","."]
B=[".",".","."]
C=[".",".","."]
Grille=[A,B,C]
for i in range(0,len(Grille)):
    print(Grille[i])
player="X"
save= ''

print("CROIX ou ROND?")
print("1: X / 2:O")
save=input()
if(save==1):
    player="X"
if(save==2):
    player="O"

A[1]=player
for i in range(0,len(Grille)):
    print(Grille[i])

#3




