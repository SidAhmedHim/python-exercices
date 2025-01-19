import statistics,os

user_list=list()
while True:
  number=input("enter a number: ")
  if number.isdigit():

    if number!='0':
      number=int(number)
      user_list.append(number)
      print(f"current list {user_list}, sorted list ascending ordor: {sorted(user_list)}, sorted list descdending ordor: {sorted(user_list,reverse=True)} ")
    else:
      break
  else:
    print("enter an integer ")

if not user_list:
  print("The list is empty. No statistics can be calculated.")
else:
   mean = statistics.mean(user_list)            # Calculate mean and median
   median = statistics.median(user_list)
   print(f"the mean is {mean}, and the mediane is {median}")  

filename="user_list.txt"
try:
        with open(filename, "w") as file:
            for num in user_list:
                file.write(f"{num}\n")
        print(f"List saved to {filename}")
except Exception as e:
        print(f"Error saving to file: {e}")                                          

if os.path.exists(filename):
  
  try:
          with open(filename, "r") as file:
              user_list = [int(line.strip()) for line in file]
          print(f"List loaded from {filename}: {user_list}")
          
  except Exception as e:
          print(f"Error loading file: {e}")
      
else:
          print(f"File '{filename}' does not exist.")
    
