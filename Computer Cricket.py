#importing Module
import random

#function for play
def p_batting():
    global bat
    global bowl
    for i in range(20):
        bat=int(input('Bat: '))
        bowl=random.choice(Com_option)
        print('Bowl',bowl)
        if bat==bowl:
            print('Player out')
            
            break
def p_bowl():
    global bat2
    global bowl2
    for i in range(20):
        bowl2=int(input('Bowl: '))
        bat2=random.choice(Com_option)
        print('Bat:',bat2)
        if bat2==bowl2:
            print('Out, How is it!')
            break
        
#Player Playing
def Player():
    global Player_action
    if Player_action==1:
        print('Player Batting Go!')
        bat=int(input('Bat: '))
        bowl=random.choice(Com_option)
        print('Bowl',bowl)
        if bat==bowl:
            print('Out, How is it!')
        else:
            p_batting()
    elif Player_action==2:
        print('Player Bowling Go!')
        bowl2=int(input('Bowl: '))
        bat2=random.choice(Com_option)
        print('Bat: ',bat2)
        if bat2==bowl2:
            print('Player out')
        else:
            p_bowl()
            
#Toss for the Match
Com_option=[0,1,2,3,4,5,6]
com=random.choice(Com_option)
Com_Chose=['Batting', 'Bowling']

print("welcome to Computer Cricket")
print('Rules--,\n the Numbers allowed are "0" to "6"\n if you win the toss you get to choose for bating or for bolwing')
print('\n Please Choose odd or even for the choose')
Player_choice=int(input('1 for Odd or 2 for Even \n'))
if Player_choice==1:
    Player_choice='odd'
    print('Player Chose odd')
else:
    Player_choice='even'
    print('Player Chose even')
toss=int(input('Please Enter the Number '))
Com_toss= com
print('Computer Number is:', com)
Result= toss + Com_toss

x='even'
y='odd'
if x==Player_choice:
    if Result%2==0:
        print(" It's Even you Won the toss")
        Player_action=int(input('Please opt for Batting->1 or Bowling->2\n'))
        Player()
    else:
        print("It's Odd You lose the toss")
        z=random.choice(Com_Chose)
        print('Computer opt for', z )
if y==Player_choice:
    if Result%2==1:
        print("It's Odd You Won the toss")
        Player_action=int(input('Please opt for Batting->1 or Bowling->2\n'))
        Player()
    else:
         print(" It's Even you lose the toss")
         z=random.choice(Com_Chose)
         print('Computer opt for', z )

#Computer Playing
if z=='Batting':
    print('Player Bowling Go!')
    bowl2=int(input('Bowl: '))
    bat2=random.choice(Com_option)
    print('Bat: ',bat2)
    if bat2==bowl2:
        print('Player out')
    else:
        p_bowl()
elif z=='Bowling':
    print('Player Batting Go!')
    bat=int(input('Bat: '))
    bowl=random.choice(Com_option)
    print('Bowl',bowl)
    if bat==bowl:
        print('Out, How is it!')
    else:
        p_batting()
