numbers=[]
shoe_sizes=[]
for i in range(5):
  num=int(input())
  if num not in numbers:                  #handle duplicate
   numbers.append(num)

for i in range(5):                        
 show=int(input())
 shoe_sizes.append(show)

num_shoes=numbers+shoe_sizes                    #third list combining numbers and show size

print(f"Numbers List: {numbers} Shoe Sizes List: {shoe_sizes}")
print(f"num_shoes {num_shoes}")
