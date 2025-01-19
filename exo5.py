print("Runner1:")
R1_name=input("Name: ")
R1=float(input("time(in seconuds): "))
print("Runner2:")       
R2_name=input("Name: ")
R2=float(input("time(in seconuds): "))
if R1<R2:
    print("The faster runner is ",R1_name)
elif R1>R2:
    print("The faster runner is ",R2_name)
else:
    print(R1_name,"and",R2_name,"have the same time!")