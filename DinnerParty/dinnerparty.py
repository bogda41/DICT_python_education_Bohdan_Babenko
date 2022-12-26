#################Stage 1-st################
people={}
names=[]
answer=int(input("How much people: "))
while answer<=0:
    print("No one is joining for the party.")
    answer=int(input("How much people: replay: ")) #delete replay
if answer>0:
    print("Input a name")
    for i in range(answer):
        name=input(">")
        names.append(name)
people=dict.fromkeys(names, "0")
#################Stage 2-nd################
cost=int(input("Enter the total amount: "))
while cost<=0:
    print("Invalid number")
    cost=int(input("Enter the total amount: replay: ")) #delete replay
money=round(cost/answer,2)
people=dict.fromkeys(names, money)
print(people)
#################Stage 3-rd################
import random
ans=input("Use 'Happy Choice? (yes/no)'" )
while ans!="yes":
    print("Invalid input")
    ans=input("Use 'Happy Choice? (yes/no)'" )
    if ans=="no":
        print(people)
        break
if ans=="yes":
    lucky=random.choice(names)
    print(lucky)
#################Stage 4-th################
    names.remove(lucky)
    money=round(cost/(answer-1),2)
    people=dict.fromkeys(names, money)
    print(people)
    