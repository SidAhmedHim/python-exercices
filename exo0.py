nb_people= int(input("How many people need a ride? "))
taxi_capacity=int(input("How many people can fit in a taxi? "))
print("Number of taxis needed: ", nb_people//taxi_capacity + (nb_people%taxi_capacity>0))
