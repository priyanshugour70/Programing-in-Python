

# in this loop we get use range to print the number to our choice. ..

n = int(input("Enter The Number to print value :  "));

for i in range(n+1):
    if(i == 0):
        continue;
    print(i);
    
    
for j in range(10, 20):
    if(j == 10):
        continue;
    print(j);
    
    
    
for k in range(21 , 30 , 3):
    print(k);