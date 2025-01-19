string=str(input("Please type in a string: "))
chars=['a','e','o']

for char in chars:

  if char in string:
    print(f"{char} found")
  else:
    print(f"{char} not found")  