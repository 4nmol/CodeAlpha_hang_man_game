import random
def hangman():
    print("Your game is started !")
    list_words=['php','java','sql','python','html']
    word=random.choice(list_words)
    ## print("your random word is: ",word)
    turns=10
    guessmade=''
    entries=set('abcdefghijklmnopqrstuvwxyz')
    
    while len(word)>0:
        main_word=''
        
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
                
        if main_word==word:
            print(main_word)
            print("You won the game!!")
            break
            
        print("guess the words",main_word)
        guess=input()
        if guess in entries:
            guessmade=guessmade+guess
        else:
            print("Enter valid character ")
            guess=input()
            
        if guess not in word:
            turns=turns-1
            
            if turns==9:
                print("9 turns left!!")
                print("--------------")
            if turns==8:
                print("8 turns left!!")
                print("--------------")
                print("    (*.*)     ")
                print("--------------")
            if turns==7:
                print("7 turns left!!")
                print("--------------")
                print("    (*.*)     ")
                print("      |       ")
                print("--------------")
            if turns==6:
                print("6 turns left!!")
                print("--------------")
                print("    (*.*)     ")
                print("      |       ")
                print("     /        ")
                print("--------------")
            if turns==5:
                print("5 turns left!!")
                print("--------------")
                print("    (*.*)     ")
                print("      |       ")
                print("     / \      ")
                print("--------------")
            if turns==4:
                print("4 turns left!!")
                print("--------------")
                print("    (*.*)     ")
                print("   ---|       ")
                print("     / \      ")
                print("--------------")
            if turns==3:
                print("3 turns left!!")
                print("--------------")
                print("    (*.*)     ")
                print("   ---|---    ")
                print("     / \      ")
                print("--------------")
            if turns==2:
                print("2 turns left!!")
                print("--------------")
                print("           |  ")
                print("    (*.*)     ")
                print("   ---|---    ")
                print("     / \      ") 
                print("--------------")
            if turns==1:
                print("1 turns left!!")
                print("--------------")
                print("           |  ")
                print("    (*.*)  |  ")
                print("   ---|---    ")
                print("     / \      ")
                print("--------------")
            if turns==0:
                print("0 turns left!!")
                print("--------------")
                print("           |  ")
                print("    (*.*)__|  ")
                print("   ---|---    ")
                print("     / \      ")  
                print("-----   ------")
                print("You loose ! You Died!")
                # print("")
                break
                    
                
                    
name=input("Enter name: ")
print("welcome! ",name,"to play the hang man game")
print("guess the game in less than 10 attempts")
hangman()