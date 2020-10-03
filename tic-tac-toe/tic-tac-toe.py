from random import randint
import os,time
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr


board = [' ']*10

won = 1
player = 1
running = 0
choice = 0
Draw = -1
game = running
p1_option = ''
p2_option = ''
chose = ''
p1=''
p2=''

def drawboard():
    print(' {0} |{1}| {2}'.format(board[1],board[2],board[3]))
    print('_____|___|______')
    print(' {0} |{1}| {2}'.format(board[4],board[5],board[6]))
    print('_____|___|______')
    print(' {0} |{1}| {2}'.format(board[7],board[8],board[9]))
    print('     |   |    ')

def boardStatic():
    print('  1  | 2 |  3 ')
    print('_____|___|______')
    print('  4  | 5 |  6 ')
    print('_____|___|______')
    print('  7  | 8 |  9 ')
    print('     |   |    ')

def wins():
    global game
    if game==running:
        for n in [1,4,7]: #horizontal
            if board[n]==board[n+1]!=' ' and board[n+1]==board[n+2] :
                game = won

        for n in [1,2,3]: #vertical
            if board[n]==board[n+3]!=' ' and board[n+3]==board[n+6] :
                game = won

        for n in [1]: #leading diagonal
            if board[n]==board[n+4]!=' ' and board[n+4]==board[n+8] :
                game = won

        for n in [3]: #other diagonal
            if board[n]==board[n+2]!=' ' and board[n+2]==board[n+4] :
                game = won

    else:
        game = running


def audio():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio=r.listen(source)
        
        try:
            word=r.recognize_google(audio)
            return word
            
        except:
            print("NOT PROPERLY AUDIBLE")
            
def gameP():
    global p1
    global p2
    global p1_option
    global p2_option


    print("------------------------WELCOME TO THE TIC-TAC-TOE GAME - (created by CiPH3R)-----------------------------\n")
    playsound('f1.mp3', True)
    
    print("\nPlayer 1 enter your name : ",end='')
    playsound('f2.mp3',True)
    p1 = audio()
    print(p1)
    
    print("\nPlayer 2 enter your name : ",end='') 
    playsound('f2-1.mp3', True)
    p2 = audio() 
    print(p2)
    
    
    k = [p1,p2]
    l = randint(0,1)
    
    rand = print("\nRandom player chosen by computer to get the choice : {}".format(k[l]))
    
    
    if l == 0:
        print("\n{} choose 'X' or 'O' : ".format(p1))
        playsound('x_or_0.mp3',True)
        p1_option = str(audio())
        print(p1_option)
    else:
        print("\n{} choose 'X' or 'O' : ".format(p2))
        playsound('x_or_0.mp3',True)
        p2_option = str(audio())
        print(p2_option)
    

    if p1_option == 'X' or 'axe' or 'sex' or'x' :
        p2_option = 'O'
        p1_option = 'X' 
    elif p1_option == 'O' or 'zero' or'o' or '0':
        p2_option = 'X'
        p1_option = 'O'
    
    
    print("Here, all the locations are accessed as : ")
    playsound('board_location.mp3',True)

    boardStatic()
    print('\n')

    time.sleep(3)
    os.system('cls')  
    drawboard()
    while(game==running):
        global player
        
        if player%2!=0:
            player+=1
            print("\n{}'s chance : ".format(p1),end='')
            playsound('index.mp3',True)
            chose = audio()
            print(chose)

            board[int(chose)] = ' '+str(p1_option)+' '
            os.system('cls')
            drawboard()
            wins()
            if game == won:
                text1 = 'CONGRATULATIONS {} , YOU WON.'.format(p1)
                language = 'en-us'
                obj = gTTS(text=text1, lang=language, slow=False)
                obj.save("won.mp3")
                playsound('won.mp3',True)
                print("\n--------------------CONGRATULATIONS {} !! YOU WON.--------------------".format(p1))
                
                break
            elif game == Draw:
                print("--------------------OH NO...GAME DRAW !!--------------------")
                playsound('draw.mp3',True)
                break
        else :
            player-=1
            print("\n{}'s chance : ".format(p2), end='')
            playsound('index.mp3',True)
            chose = audio()
            print(chose)

            board[int(chose)] = ' '+str(p2_option)+' '
            os.system('cls')
            drawboard()
            wins()
            if game == won:
                text1 = 'CONGRATULATIONS {} , YOU WON.'.format(p2)
                language = 'en-us'
                obj = gTTS(text=text1, lang=language, slow=False)
                obj.save("won.mp3")
                playsound('won.mp3',True)
                print("\n--------------------CONGRATULATIONS {} !! YOU WON.--------------------".format(p2))
                
                break
            
            elif game == Draw:
                print("--------------------OH NO...GAME DRAW !!--------------------")
                playsound('draw.mp3',True)
                break
        
gameP()
 
 
