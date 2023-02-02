'''
In today we get learn about function argument in Python Programing Language....

mainly four type of Function Argument in python ......

1. Default Aruguments.
2. Keyword Arguments.
3. VAriable length Arguments. 
4. Required Arguments. 

'''

#***************************************
def twonumsum(a = 10 , b = 20):
    print("Sum of two number is : ", a+b)
    
a = 5
b = 15
twonumsum()
twonumsum(a,)
twonumsum(a,b)


#***************************************
def names(fname = "Devanshu", mname = "Kumar", lname="Gour"):
    print("hello Buddy, ",fname," ",mname," ",lname)

fname = "Priyanshu"
mname = "Kumar"
lname = "Gour"

names()
names(fname,)
names(fname,mname)
names(fname,mname,lname)


#***************************************
def myname():
    nme = input("Enter Your Name. : ")
    return nme 

nameis =  myname()
print("\nMy Name is : ",nameis,"\n")


#***************************************
def nmbrs(*values):
    print(type(values))
    print(values)
    
nmbrs(1,2,3,4,5,6,7,8,9,10)


#***************************************
def colours(**color):
    print(type(color))
    for i in color:
        print(i);
        
colours(lal="red",pila="Yellow",nila="blue")