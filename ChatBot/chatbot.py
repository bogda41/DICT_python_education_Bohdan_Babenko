bot_name = " DefBot"
birth_year = " 2022"
############1-st stage########################
print ("Hello! My name is"+bot_name)
print ("I was created in"+birth_year)
############2-nd stage########################
user_name=input("Please, remind me your name ")
print("What a great name you have, "+user_name)
############3-rd stage########################
print("Let me guess your age")
print("Enter remainders of dividing your age by 3,5 and 7.")
a = int(input ()) 
b = int(input ()) 
c = int(input ())
age = (a*70+b*21+c*15)%105
print("Your age is %s that's a good time for starting programming!" %age)
############4-th stage########################
print("Now i will prove to you that I can count to any number wou want.")
x = int(input())
y = 0 
print("OK. Let's Dance")
while y<=x:
    print(y,"!")
    y=y+1
print("Completed, have a nice day!") 
############5-th stage########################
print("Let's test your programming knowledge.")
print("Which command we use to make a commit?")
x=int(input(""" 
1. git commit -m
2. git reset --hard 
3. git checkout
4. git log --oneline
"""))
if x==1:
    print("Right, have a nice day!")
while x!=1:
    print("Please, try again")
    x=int(input())
    if x==1:
        print("Right, have a nice day!")
        break
    