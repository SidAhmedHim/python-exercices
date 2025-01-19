width=int(input("width: "))
height=int(input("height: "))
print("\n")
char=''
for i in range(width) :
  char+='#'
chaine=''  
for j in range(height) :
  chaine+=char
  chaine+=' '
print(chaine)