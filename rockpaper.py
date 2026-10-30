import random 

# num = random.randint( 1 , 6 ) 
# print(num)

handsigns = [ "rock" , "paper" , "scissors" ]

comp_win = 0 
human_win = 0 

while( True ) : 
    print(" 1 : rock ")
    print(" 2 : paper ")
    print(" 3 : scissors ")
    handuser = int(input("choose your sign : "))
    
    if( handuser == 1 ) : 
        num1 = random.randint( 0 , 2 )
        if( num1 == 0 ) : 
            print("comp chose : ", handsigns[num1])
            print("stalemate")
        if( num1 == 1 ) : 
            print("you lose")
            print("comp chose : ", handsigns[num1])
            comp_win += 1 
        if( num1 == 2 ) : 
            print("you win")
            print("comp chose : ", handsigns[num1])
            human_win += 1
        print("your score : ", human_win )
        print("comp score : ", comp_win )

    if( handuser == 2 ) : 
        num1 = random.randint( 0 , 2 )
        if( num1 == 2 ) : 
            print("stalemate")
            print("comp chose : ", handsigns[num1])
        if( num1 == 3 ) : 
            print("you lose")
            print("comp chose : ", handsigns[num1])
            comp_win += 1 
        if( num1 == 1 ) : 
            print("you win")
            print("comp chose : ", handsigns[num1])
            human_win += 1
        print("your score : ", human_win )
        print("comp score : ", comp_win )
            
    if( handuser == 3 ) : 
        num1 = random.randint( 0 , 2 )
        if( num1 == 3 ) : 
            print("stalemate")
            print("comp chose : ", handsigns[num1])
        if( num1 == 0 ) : 
            print("you lose")
            print("comp chose : ", handsigns[num1])
            comp_win += 1 
        if( num1 == 1 ) : 
            print("you win")
            print("comp chose : ", handsigns[num1])
            human_win += 1
        print("your score : ", human_win )
        print("comp score : ", comp_win )
        
    if( comp_win == 3 ) : 
        print("you lose")
        break
    if( human_win == 3 ) : 
        print("you win")
        break

