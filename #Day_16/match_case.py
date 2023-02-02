# in today we will learn about match case this is same as it switch case but some different ......



i = int(input("Enter Number  :  "));

match i :
    case 1 :
        print("Monday.....")
    case 2 :
        print("Tuesday....")
    case 3 : 
        print("Wednesday..")
    case 4 :
        print("Thrusday...")
        x = input("Enter You are Boy or Girl");
        print(x)
    case 5 if i == 5 :
        print("Friday.....")
    case _ if i == 6 :
        print("Saturday...")
    case _ if i == 7 :
        print("Sunday.....")
    case _:
        print("***************  Wrong Choice.....  ***************")
    
    
    
    