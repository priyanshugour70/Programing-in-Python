import time ;


tym = time.strftime('%H:%M:%S');
print(tym);

H = int(time.strftime('%H'));
M = int(time.strftime('%M'));
S = int(time.strftime('%s'));


if (H<12):
    print("Good Morning!")
elif(H >= 12 and H < 18):
    print("Good Afternoon!")
elif(H >= 18 and H < 21):
    print("Good Evening!")
else:
    print("Good Night!")       
        

print("\n\n\n*************Thanx For Visiting*************\n\n\nVisit Again..");


"""if(0 <= H and (H <=11 and (59 >= M and (59 >= S) ) )):
    if(0 <= H and (H <=5 and (59 >= M and (59 >= S) ) )):
        print("Good Morning Sir..");
    else:
        print("This time is Night but next day moring Night..");
else:
    if(12 <= H and (H <=16 and (59 >= M and (59 >= S) ) )):
        print("Good Afternoon Sir..");
    elif(5 <= H and (H <=20 and (59 >= M and (59 >= S) ) )):
        print("Good Evening Sir..")
    else:
        print("Good Night Sir..");"""