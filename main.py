
def board(signs):
    print(f"   |   |   ")
    print(f" {signs[0]} | {signs[1]} | {signs[2]} ")
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {signs[3]} | {signs[4]} | {signs[5]} ")
    print(f"___|___|___")
    print(f"   |   |   ")
    print(f" {signs[6]} | {signs[7]} | {signs[8]} ")
    print(f"   |   |   ")

def player_1(signs):
    print("Player 1:")
    while True:
        move = input("Enter the cell number: ")
        if (not move.isdigit()):
            continue
        else:
            move = int(move)
            
        if(not 1<=move<=9):
            print("Invalid cell number!!")
            print("You must enter (1-9)")
            continue
        
        if(signs[move-1]== " "):
            signs[move-1] = "X"
            break
        else:
            continue
    return signs

def player_2(signs):
    print("Player 2:")
    while True:
        move = input("Enter the cell number: ")
        if (not move.isdigit()):
            print("Invalid cell number!!")
            print("You must enter (1-9)")
            continue
        else:
            move = int(move)
            
        if(not 1<=move<=9):
            print("Invalid cell number!!")
            print("You must enter (1-9)")
            continue
            
        if(signs[move-1]== " "):
            signs[move-1] = "O"
            break
        else:
            continue
    return signs

def win_check(signs):
    if(signs[0]==signs[1]==signs[2]!=" " or 
       signs[3]==signs[4]==signs[5]!=" " or 
       signs[6]==signs[7]==signs[8]!=" " or 
       signs[2]==signs[5]==signs[6]!=" " or 
       signs[0]==signs[5]==signs[8]!=" " ):
        return 1
    else:
        return 0
        
    


def main():
    signs = [" "," "," "," "," "," "," "," "," "]
    
    for x in range(1,11):
        if (x == 10):
            if win_check(signs)==0:
                print("Draw!!")
        elif (x % 2 == 1):
            board(signs)
            signs = player_1(signs)
            if win_check(signs) == 1:
                print("Player 1 win!!")
                break
        elif (x % 2 == 0):   
            board(signs)
            Signs = player_2(signs)
            if win_check(signs) == 1:
                print("Player 2 win!!")
                break
        

if __name__ == "__main__":
    main()