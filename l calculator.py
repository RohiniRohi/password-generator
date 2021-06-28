print("welcome to love calculator")
name1=input("enter your name\n")
name2=input("enter your second name\n")
string=name1+name2
print(string)
lower_string=string.lower()
t=lower_string.count("t")
r=lower_string.count("r")
u=lower_string.count("u")
e=lower_string.count("e")
true=t+r+u+e
l=lower_string.count("l")
o=lower_string.count("o")
v=lower_string.count("v")
e=lower_string.count("e")
love=l+o+v+e
score=int(str(true)+str(love))
print(score)
if score<10 or score>90:
    print("your score is {} ,you are alright together".format(score))
elif score>=40 and score<=50:
    print("your score is {},you go to alright together".format(score))
else:
    print("your  love score is {}".format(score))
