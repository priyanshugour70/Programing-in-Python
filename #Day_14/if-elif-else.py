a = int(input("Enter your age  :  "));

# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)


if(a >= 18):
    print("Your age is : ",a);
    print("You Can Drive.....");
elif(a <= 0):
    print("Your Age is invalid........");
elif(a >= 0 and 18 > a):
    if(a >= 15 and a <= 18):
        print("Your age is : ",a);
        print("Wait For some times, for Driving ......");
    elif(a >= 8 and a <= 14):
        print("Your age is : ",a);
        print("Your are Can Not Drive, Wait for time to Age 18.......");
    elif(0 < a and 7 >= a):
        print("Your Age is : ",a);
        print("You Cannot Drvie, Your kid.......");
else:
    print("Your age is : ",a);
    print("You Can't Drive.....");
    
print("\nYour Program is Completed......\nThanking For Visiting ...!\nVisit Again.....!!\n");