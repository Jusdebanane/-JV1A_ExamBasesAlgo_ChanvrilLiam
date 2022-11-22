#1
ligne0=[" ","A"," ","B"," ","C"]
ligne1=["1"," ","*"," ","*"," "]
ligne2=["2","*","*","*","*","*"]
ligne3=["3"," ","*"," ","*"," "]
ligne4=["4","*","*","*","*","*"]
ligne5=["5"," ","*"," ","*"," "]

print(ligne0)
print(ligne1)
print(ligne2)
print(ligne3)
print(ligne4)
print(ligne5)


#2
ligne0=[" ","A"," ","B"," ","C"]
ligne1=["1"," ","*"," ","*"," "]
ligne2=["2","*","*","*","*","*"]
ligne3=["3"," ","*"," ","*"," "]
ligne4=["4","*","*","*","*","*"]
ligne5=["5"," ","*"," ","*"," "]
joueur = ' '

print("croix ou rond?")
print("1= X / 2= O")
joueur = input('')
if(joueur=="1"):
    joueur = "X"
    print("Vous etes croix")
if(joueur=="2"):
    joueur=="O"
    print("Vous etes rond")
else:
    print("Choix par défaut: Vous etes croix")
    joueur = "X"
print(" ")
ligne1[1]= joueur

print(ligne0)
print(ligne1)
print(ligne2)
print(ligne3)
print(ligne4)
print(ligne5)






