# in today we get learn about most important topic function in Python.....


def fibonachi(a):
    pass

def meanoftwonumber(a, b):
    x = (a*b)/(a+b)
    print("Mean of The Two number is : ", x )


def greaterandless(a, b):
    if(a>b):
        print(a, " Is Greater then ",b);
    elif(a == b):
        print(a,b, " Both are Equal ..");
    else:
        print(b, " Is Greater Then ", a);

def sum(a,b):
    return a+b        
        
i = int(input("Enter First Nubmer : "))
j = int(input("Enter Second Nubmer : "))

meanoftwonumber(i, j );
# print("\n\n\n\n\n");
greaterandless(i,j);

s = sum(i,j)
print(s);