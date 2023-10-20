#1.Ask user do they want to play game & tell the details about the game

def play():
    t = True
    while t == True:
        print ('\nHi !ʕ•́ᴥ•̀ʔっ Do you want to play a "♚ Master Mind Computer Game ♚" ?')
        hello = input('Enter (S) to start : ')
        if hello == 's' or hello == 'S' :
            print ('\n✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿  ➳ W E L C O M E ➳  ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿')
            print ()
            
            print ('\n----------------------------------➳WHAT IS THIS GAME ABOUT ?➳----------------------------------')
            print ('\nGuess what are the four shapes chosen by the computer.')
            print ('\nHere are list of the shapes: ',shapelist)
            
            print ('\n-------------------------------------------➳ RULES ➳-------------------------------------------')
            print ('\n1.Multiple attempts,player can choose to continue or end the game.')
            print ('2.Shapes can be REPEATED, not limited !')
            print ('3.Player is required to guess the shapes and place them correctly to win this game. ')
            print ()
            
            print ('\n----------------------------- ᕙʕ`▿´ʔᕗ G O O D   L U C K !ᕙʕ`▿´ʔᕗ ----------------------------- ')
            print ()
            t = False
            randomshape()
        else:
            #check validation
            print('\n★ ERROR! Please enter (S) to start, if u ready to play !')
            t = True
            continue



#2.Randomly choose four shapes from the list,attempt start counting
        
def randomshape():
    attempt = 1
    for count in range (1,4+1):
        computer = random.choice(shape_letter)
        random_list.append(computer)
    attempt = begin (attempt)
      

#3.Begin to guess
    
def begin(attempt):
    print ('REQUIREMENT ☜(ˆ▿ˆc): Please enter first letter of the shapes (ex:c=cirle)')

    #ask player to guess four shapes
    num = 1
    while num <= 4  :
        guess = input(f'Guess the shape {num}: ').lower()
        
        #check validation
        if guess not in shape_letter:
            print ('\n★ Please enter letter that is related to the list of shapes !')
            print ('List of shapes: c = circle, t = triangle, s = square, p = pentagon, d = diamond, h = heart')
            print ()
            
        #meet requirement
        elif guess in shape_letter:
            player_list.append(guess)
            num += 1

            
    #4.Checking for the results...
            
    correct_place = 0
    wrong_place = 0
    #create temporary list to advoid changes when modify from origin list
    r_random_list = random_list[:]
    r_player_list = player_list[:]

    #first,check for correct shape & correct place
    for a in range (4):
        if r_player_list[a] == r_random_list[a]:
            correct_place += 1
            #replace (correct shape & correct place)and modify for second check(correct shape & wrong place)
            r_player_list[a] = "0"
            r_random_list[a] = "1"
                        
    #second,check for correct shape & wrong place
    #using (r_player_list) & (r_random_list)to advoid re-check shape which is (correct shape & correct place)
    for a in range (4):
        for b in range (4): 
            if r_player_list[a] == r_random_list[b]:
                wrong_place += 1
                                
    print ()
    print ('Correct shape in correct place: ',correct_place)
    print ('Correct shape but in the wrong place:',wrong_place)
    print ()
    print (attempt,'round, this is your list: ',player_list)
    value = check_two(correct_place,attempt)

    
    
#5.Check whether player win the game & allow them to make decision
    
def check_two(correct_place,attempt):
    i = True
    while i == True:
        #player did not win the game
        if correct_place != 4:
            print ('\nOH NO ! NO WORRY...LETS TRY AGAIN ! (ɔ◔‿◔)ɔ ♥')
            print ('\ny = yes(continue), n = no(end game)')
            try_again = input('Do you want to continue guessing? Enter (Y/N):')
            
            #player decide to try again
            if try_again  == 'y' or try_again  == 'Y':
                attempt += 1
                #clear previous list
                del player_list [:]
                print()
                i = False
                attempt = begin(attempt)
                
            #player decide to end the game    
            elif try_again == 'n' or try_again == 'N':
                end()
                i = False
                
            #check validation
            else:
                print('\n★ Please enter (Y/N)! y=yes, n=no ')
                i = True
                
        #player win the game   
        else:
            print ('\n------------------*ᕙʕ`▿´ʔᕗ C O N G R A T U L A T I O N S ᕙʕ`▿´ʔᕗ*------------------')
            print ('------------------------------- You win this game ! --------------------------------')
            print ('\nYou took',attempt, 'attempts.')
            print ()
            i = False
            end()


#6.End the game~~~
        
def end():
    print ('\n------------------------------♚ G A M E _ E N D E D ! ♚------------------------------  ')
    print ('-----------------------✿ THANK YOU ! HOPE U HAVE A NICE DAY ツ✿-----------------------')



#Import from random library
import random

shapelist = ['circle','triangle','square','pentagon','heart','diamond']
#Use first letter to represent the shape list
shape_letter = ['c','t','s','p','h','d']

random_list = []
player_list = []
play()
