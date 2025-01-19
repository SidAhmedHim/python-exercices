print("enter the name of different citys")
citys=[]
#input the citys and store their population
while True:
    city=str(input())
    if city == 'stop':
      break
    citys.append((city,len(city)*1000000))
#sort the citys
citys=sorted(citys,key=lambda city: city[1],reverse=True)
for city,population in citys:
   print(f"The city {city} has {len(city)} letters, so its population is {population}.")

