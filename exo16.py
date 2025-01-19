# static  numbers=[1,2,3,4,5]
# dinamic initialisation of list
numbers=[]
print("enter the values for the list (-1 to quite)")
while True:
  number=int(input())
  if number==-1:
    break
  numbers.append(number)

#traitement programme

while True:
  index=input("input an index(-1 to quite): ")
  if index=='-1':
    break
 
  if index.isdigit():
    index=int(index)
    
    if index<len(numbers):
      Value=int(input("input a value: "))
      validation=str(input(f"are u shur u want to remplace the value: {numbers[index]} of the index {index} with the value: {Value} yes or no?"))
      if validation=='yes':
        numbers[index]=Value     
    else:
      print("index out of range")
   
  else:
    print("error type")
  print(numbers)    