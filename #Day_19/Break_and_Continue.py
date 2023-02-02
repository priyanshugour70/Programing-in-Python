# in today we get lern about break and continue..



# for j in range (True):
#     if(j >20):
#         break;
#     if(j == 0):
#         continue;
#     if(j % 2 != 0):
#         continue;
#     print(j)

# j = 1
# while True : 
#     if(j >20):
#         break;
#     if(j == 0):
#         continue;
#     if(j % 2 != 0):
#         continue;
#     print(j)
#     j = j+1;

i = int(input("Enter Nubmer : "))

for j in range(i):
    if(j > 20):
        break
    if(j % 2 == 0):
        if(j == 0):
            continue
        print(j)
        
        
i = 1 
while True :
    print(i)
    if(i % 50 == 0):
        break
    
    i = i + 1 ; 
    