# in today we learn about sliceing in python so lets learn.........



name = "Priyanshu Gour";

length = len(name);

print("Length of the Name is : ",length);

# lets star Sliceing .....

print(name[2:5]);
print(name[:7]);
print(name[5:]);
print(name[:]);

# negative sliceing...

print(name[0:-5]);  #name[0:len(name)-5];
print(name[0:len(name)-5]);
print(name[-4:-2]);
print(name[len(name)-4:len(name)-2]);




#Loop....

x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ..";

for a in x :
    print(a);