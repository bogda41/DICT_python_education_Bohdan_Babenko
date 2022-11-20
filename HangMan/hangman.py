##################Stage 8-th####################
import random
import string
import sys
print("HANGMAN")
print("Wanna play a game? (play/exit)")
game=input()
while game!="play":
    game=input("Wanna play a game? (play/exit)")
    if game=="exit":
        sys.exit()
def hangman():
    print ("Welcome to game")
    list=("python", "java", "javascript", "php")
    max_wrong=8
    wrong=0
    secret=random.choice(list)
    symbols="-"*len(secret)
    letters=[]
    lower_case=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while wrong<=max_wrong and symbols!=secret:
        print("Mistakes -  ",wrong)
        print("Already used letters: ",letters)
        print("Word - ",symbols)
        ans=input("Input a letter: ")
        while len(ans)!=1:
            ans=input("You should input a single letter. ")   #1 буква
        while ans not in lower_case:
            ans=input("Please enter a lowercase English letter. - ") #Англ.буква нижнего регистра
        while ans in letters:
            print("You already used this letter: ",ans) #Уже используется
            ans=input("Inpust a letter: ")
            if wrong>=max_wrong: 
                print("You lose, this word is:  ",secret)
                break
        if ans in secret:
            print("Right, have this letter: ",ans) #Правильно
            new= ""
            for i in range(len(secret)):
                if ans==secret[i]: 
                    new+=ans
                else:
                    new+=symbols[i]
            symbols=new
        else:
            print("This word don't have this letter: ",ans) #Нету такой буквы
            wrong+=1
        letters.append(ans)
    if wrong>=max_wrong:
        print("You lose, this word is: ",secret)
    else: 
        print("You WIN! This word is: ",secret)
answer="yes"
while answer=="yes":
    hangman()
    answer=input("Wanna paly again? (yes/no)")
    