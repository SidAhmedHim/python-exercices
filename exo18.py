import pickle
import os
numbers=[]
filename=""

while True:
  load=input("do u want to load a list from the file or start with the standard one? 1 for load, 0 for standard: ")
  
  if load=="1":
   filename=input("enter ur file name with its extension: ")
   if os.path.exists("./"+filename): 
    with open(filename, 'rb') as file:  # Open the file in binary read mode
      numbers=pickle.load(file)
      print(f"the loaded list : {numbers}")
      break
   else:
      print("your file doesn't exist")

  elif load=="0":
   numbers = [1, 2, 3, 4, 5]
   print(f"the standard list: {numbers}")
   break

  else:
    print("choose between 1 and 0")

print("Menu: ")
print("  1.Append")
print("  2.Insert")
print("  3.Pop")
print("  4.Remove")
print("  5.sorting")
print("  6.reversing")
print("  7.save the list to a file")
print("  8.reload the stored list")
print("  9.Quit")

while True:
  option=(input("Choose an option: "))
  if option.isdigit():
    option=int(option)    
    if option in [1,2,3,4,5,6,7,8,9]:
      
      if option==9:
        break
      
      if option==7:
        filename=input("enter ur filename with its extension: ")
        with open("./"+filename, 'wb') as file:  # Open in binary write mode
           pickle.dump(numbers, file)
        print(f"the stored list: {numbers}")

      elif option==8:
        filename=input("enter ur file name with its extension: ")
        if os.path.exists("./"+filename): 
          with open(filename, 'rb') as file:  # Open the file in binary read mode
            numbers=pickle.load(file)
            print(f"the loaded list : {numbers}")
            
        else:
          print("your file doesn't exist")  

      elif option==5:
        while True:
          choose=input("enter 1 for ascendant, 2 for descendant: ")
          if choose =='1':
            numbers.sort()
            print(f"updated list :{numbers}")
            break
          elif choose=='2':
            numbers.sort(reverse=True)
            print(f"updated list :{numbers}")
            break
          else:
            print("enter the right value for chosing")   
      
      elif option==6:
        numbers.reverse()
        print(f"updated list :{numbers}")

      elif option==3:
        while True:

          index=(input("enter index: "))
          if index.isdigit():
            index=int(index)
            if index<len(numbers) and index>0:
              numbers.pop(index)
              print(f"updated list :{numbers}")
              break
            else:
              print("enter a valide index")
          else:
            print("enter the right type")      
      else:
        Value=input("enter value: ")
        if Value.isdigit():
          Value=int(Value)
          if option==4:
            if Value in numbers:            #searching for an element
              numbers.remove(Value)
              print(f"updated list :{numbers}")
            else:
              print("your value is not in the list")
          elif option==1:
            numbers.append(Value)
            print(f"updated list :{numbers}")
          else:
            while True:
              index=input("enter index: ")
              if index.isdigit():
                index=int(index)
                if index<len(numbers) and index>=0:
                  numbers.insert(index,Value)
                  print(f"updated list :{numbers}")
                  break
                else:
                  print("enter a valide index")
              else:
                print("enter the right type")      
        else:
          print("enter the right type")
    else:
      print("enter a valid option")  
  else:
    print("enter the right type")





