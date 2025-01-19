while True:
  string=str(input("Please type in a string: "))
  if string=='':
    break
  print(f"\033[4m{string}\033[0m")
  
