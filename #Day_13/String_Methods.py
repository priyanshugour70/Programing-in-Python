# Today we learn about the methods of String in Python .......


name = "!!..priyanshu gour..!!!";
a = "1. my name is Priyanshu Gour";
b = "1_my_name_is_Priyanshu_Gour";

x = len(name);
print(x);

print("Orignal String is  :  ",name);

x = name.upper();
print(x);

x = name.lower();
print(x);

x = name.strip("!");
print(x);

x = name.rstrip("!");
print(x);

x = name.lstrip("!");
print(x);

x = name.replace("gour","Gour");
print(x);

x = name.split();  # split convert to string to list.
print(x);

x = name.splitlines(); # this splitlines work to convert the line in a list.
print(x);

x = a.capitalize();
print(x);

l = len(name);
x = name.center(50);
print("this length is without center use length  :  ",l,"\n",x,"\nthis length of with center  :  ",len(x));

x = name.count("r");
print(x);

x = name.endswith("!!!");
print(x);

x = b.endswith("is",0,-1);  # do not show correct output
print(x);

x = b.find("is"); # if the value you searched are find to show the index value else show the -1..........
print(x);

x = b.isalnum(); # this is show to our string is A-Z a-z 1-9 ........
print(x);

x = b.isalpha(); # this is show to our string is A-Z a-z........
print(x);


i = "hello guyz \n";

x = i.islower();
print(x);

x = i.isupper();
print(x);

x = i.isprintable();
print(x);

str1 = "     "  #using space ..
str2 = "        " #using Tab ..
x = str1.isspace();
print(x);

x = str2.isspace();
print(x);

str3 = "My Name Is Priyanshu Gour";
str4 = "my name is priyanshu gour";
str5 = "MY NAME IS PRIYANSHU GOUR";
str6 = "My name is Priyanshu Gour";

x = str3.istitle();  # first letter is capital then true else false........ 
print(x);

x = str4.istitle();   # first letter is capital then true else false........
print(x);

x = str5.isupper();   # to check string is upper or lower.. and return true or false.......
print(x);

x = str5.islower();   # to check string is upper or lower.. and return true or false.......
print(x);

x = str3.startswith("My");  # to check the staring word or the string .........
print(x);

x = str3.swapcase();   # to  convert upper to lower and lower to upper .......
print(x);

x = str6.title();   # to convert in string all first words to first letter upper case........
print(x); 
