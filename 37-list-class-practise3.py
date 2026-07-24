#WAP to take a input from the user 
# and make different list for different user.
number=int(input("Enter the number of people: "))
i=1
database=[]

while i<=number:
    user_data=[] #Reset list_second for each user
    print(f"For user {i}")
    user_data.append(input(f"Enter the Name : "))
    user_data.append(input(f"Enter the Age: "))
    user_data.append(input(f"Enter the Address ")) 

    database.append(user_data)
    i+=1

print(database)