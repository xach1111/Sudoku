import random
import copy
board = {
    19:"  ",29:"  ",39:"  ",  49:"  ",59:"  ",69:"  ",  79:"  ",89:"  ",99:"  ",
    18:"  ",28:"  ",38:"  ",  48:"  ",58:"  ",68:"  ",  78:"  ",88:"  ",98:"  ",
    17:"  ",27:"  ",37:"  ",  47:"  ",57:"  ",67:"  ",  77:"  ",87:"  ",97:"  ",
    
    16:"  ",26:"  ",36:"  ",  46:"  ",56:"  ",66:"  ",  76:"  ",86:"  ",96:"  ",
    15:"  ",25:"  ",35:"  ",  45:"  ",55:"  ",65:"  ",  75:"  ",85:"  ",95:"  ",
    14:"  ",24:"  ",34:"  ",  44:"  ",54:"  ",64:"  ",  74:"  ",84:"  ",94:"  ",
    
    13:"  ",23:"  ",33:"  ",  43:"  ",53:"  ",63:"  ",  73:"  ",83:"  ",93:"  ",
    12:"  ",22:"  ",32:"  ",  42:"  ",52:"  ",62:"  ",  72:"  ",82:"  ",92:"  ",
    11:"  ",21:"  ",31:"  ",  41:"  ",51:"  ",61:"  ",  71:"  ",81:"  ",91:"  "
}

def print_board():
    print("|-----------------|")
    index = 19
    while index != 10:
        print("|",end="")
        for i in range(9):
            print(board[index], end=" ")
            if (index >30 and index <40)  or (index > 60 and index < 70):
                print("|", end=" ")
            index = index + 10
            
        print("|")
        index = index - 91
        if index == 16 or index == 13:
            print("|-----------------|")
    print("|-----------------|")




def update_pencilmarks():
    for i in board:
        pencilmarks[i] = [1,2,3,4,5,6,7,8,9]
    
    for pos1 in board:
        for pos2  in pencilmarks:
            if pos1 != pos2:
                if (str(pos1)[0] == str(pos2)[0]) or str(pos1)[1] == str(pos2)[1]:
                    if board[pos1] != "  ":
                        if board[pos1] in pencilmarks[pos2]:
                            pencilmarks[pos2].remove(board[pos1])

                if int(str(pos1)[0]) in box[0]:
                    firstdigits = box[0]
                elif int(str(pos1)[0]) in box[1]:
                    firstdigits = box[1]
                else:
                    firstdigits = box[2]

                if int(str(pos1)[1]) in box[0]:
                    seconddigits = box[0]
                elif int(str(pos1)[1]) in box[1]:
                    seconddigits = box[1]
                else:
                    seconddigits = box[2]


                if (int(str(pos2)[0]) in firstdigits) and (int(str(pos2)[1]) in seconddigits):
                    if board[pos1] != "  ":
                        if board[pos1] in pencilmarks[pos2]:
                            pencilmarks[pos2].remove(board[pos1])
        if board[pos1] != "  ":
            pencilmarks[pos1] = []
    #smart pencilmarks
    # copyofpencilmarks = copy.deepcopy(pencilmarks)
    # square = [[19,29,39,18,28,38,17,27,37],[49,59,69,48,58,68,47,57,67],[79,89,99,78,88,98,77,87,97],[16,26,36,15,25,35,14,24,34],[46,56,66,45,55,65,44,54,64],[76,86,96,75,85,95,74,84,94],[13,23,33,12,22,32,11,21,31],[43,53,63,42,52,62,41,51,61],[73,83,93,72,82,92,71,81,91]]
    # for cube in square:
    #     for place in cube:
    #         for possible in pencilmarks[place]:
    #             single = True
    #             for pos2 in cube:
    #                 if possible in pencilmarks[pos2] and str(pos2)[0] != str(place)[0] and str(pos2)[1] != str(place)[1]:
    #                     single = False
    #                 else:
    #                     compare = pos2
    #             if single == True:
    #                 if str(place)[0] == str(compare)[0]:
    #                     for i in pencilmarks:
    #                         if str(i)[0] == str(place)[0]:
    #                             if possible in pencilmarks[i]:
    #                                 pencilmarks[i].remove(possible)
    #                 elif str(place)[1] == str(compare)[1]:
    #                     for i in pencilmarks:
    #                         if str(i)[1] == str(place)[1]:
    #                             if possible in pencilmarks[i]:
    #                                 pencilmarks[i].remove(possible)
    # if copyofpencilmarks != pencilmarks:
    #     update_pencilmarks()



    #----------------
            
pencilmarks = {}
for i in board:
    pencilmarks[i] = [1,2,3,4,5,6,7,8,9]
box = [[1,2,3],[4,5,6],[7,8,9]]
update_pencilmarks()
def generateBoard():
    while "  "  in board.values():
        lowestlen = 10
        lowestPositions = []
        for i in pencilmarks:
            if board[i] == "  ":
                if len(pencilmarks[i]) < lowestlen:
                    lowestlen = len(pencilmarks[i]) 
        for i in pencilmarks:
            if len(pencilmarks[i]) == lowestlen:
                lowestPositions.append(i)
        position = random.choice(lowestPositions)
        if len(pencilmarks[position]) == 0:
            for i in board:
                board[i] = "  "
        else:
            board[position] = pencilmarks[position][0]
        update_pencilmarks()
        prePos = position
    messages = ["Nearly there.....","Just bit more....","Almost finished.....","Just a teenniee tiny idddy little bit more.............", "...................."]
    print(random.choice(messages))
##---------------


def solvable():
    global board, originalBoard
    
    definite = []
    for i in pencilmarks:
        if len(pencilmarks[i]) == 1:
            definite.append(i)
                                
    while len(definite) != 0:
        
        for i in definite:
            board[i] = pencilmarks[i][0]
        update_pencilmarks()
        definite = []
        for i in pencilmarks:
            if len(pencilmarks[i]) == 1:
                definite.append(i)

    if "  " in board.values():
        board = copy.deepcopy(originalBoard)
        return False
    else:
        board = copy.deepcopy(originalBoard)
        return True
print("""
 __            ________ _       _____ ____  __  __ ______  
 \ \          / /  ____|  |     / ____/ __ \ |  \/  |  ____| 
  \ \  /\  / /| |__    | |     | |      | |  |   | \  / | |__    
   \ \/  \/ / |  __|   | |     | |      | |  |   | |\/| |  __|   
    \  /\   /  | |____ | |___| |___  | |__|  | |  | | |____  
     \/   \/   |______|_____\____ \____/|_|  |_|_____| 

  ___________
 |__   __/ __ \                                         
    |  |  | |  |  |                                        
    |  |  | |  |  |                                        
    |  |  | |__| |                                        
    |_|   \____/

    ____ __   __  _____   ____  _  _____   __                  
  / ____|  |  |  |   __  \ / __ \|  |/  /  |  |  |              
 | (___  |  |  |  |  |   |  |  |  |  |   '  /|  |  |  |              
  \___ \|  |  |  |  |   |  |  |  |  |   <  |  |  |  |              
  ____) |  |__|  |  |__| |  |__| |   .  \|  |_|  |              
 |_____/\____/|_____/\____/|_|\_\\____/   

----------------------------------------

coordinates:-
|---------------------------|
|19 29 39 | 49 59 69 | 79 89 99|
|18 28 38 | 48 58 68 | 78 88 99|
|17 27 37 | 47 57 67 | 77 87 97|
|---------------------------|
|16 26 36 | 46 56 66 | 76 86 96|
|15 25 35 | 45 55 65 | 75 85 95|
|14 24 34 | 44 54 64 | 74 84 94|
|---------------------------|
|13 23 33 | 43 53 63 | 73 83 93|
|12 22 32 | 42 52 62 | 72 82 92|
|11 21 31 | 41 51 61 | 71 81 91|
|---------------------------|

""")






playagain = "yes"
while playagain.lower() == "yes":
    lives = 3
    answer = input("Easy, Medium or hard?: ")
    while answer.lower() != "easy" and answer != "medium" and answer !="hard":
        answer = input("INVALID INPUT. Please type: Easy, Medium or hard?: ")
    answer = answer.lower()
    if answer == "easy":
        given = random.randint(38,45)
    elif answer == "medium":
        given = random.randint(30,36)
    elif answer == "hard":
        given = random.randint(25,29)
    print("loading..............")
    generateBoard()
    answerBoard = copy.deepcopy(board)
    givenSpaces = 81
    doesntWork = []
    while givenSpaces > given:
        position = random.choice(list(board))
        while board[position] == "  " or position in doesntWork:
            position = random.choice(list(board))
            
        value = board[position]
        
        board[position] = "  "
        
        update_pencilmarks()
        
        originalBoard = copy.deepcopy(board)
        
        if solvable() == False:
            doesntWork.append(position)
            numberofnumbers = 0
            for i in board:
                if board[i] != "  ":
                    numberofnumbers += 1
            if numberofnumbers == len(doesntWork):
                generateBoard()
                answerBoard = copy.deepcopy(board)
            board[position] = value
        else:
            doesntWork = []
        givenSpaces = 0
        for i in board:
            if board[i] != "  ":
                givenSpaces += 1
    print_board()

    inputposition = 19
    while "  " in board.values():
        inp = input("Enter coordinate as a two digit number, (eg: 2,3 - type 23), or number from 1-9: ")
        while (inp.isnumeric() == False) or (inp[len(inp) -1] == "0") or (len(inp) > 2) :
            inp = input("INVALID INPUT. Enter coordinate as a two digit number, (eg: 2,3 - type 23), or number from 1-9: ")
        if(len(inp) == 2):
            inputposition = inp
            inputposition = int(inputposition)
        if(len(inp) == 1):
            inputnumber = inp
            inputnumber = int(inputnumber)

            if board[inputposition] == "  ":
                if answerBoard[inputposition] == inputnumber:
                    board[inputposition] = inputnumber
                    print_board()
                    if "  " not in board.values():
                        print("YOU WIN!!!")
                        break
                else:
                    lives -= 1
                    if lives == 0:
                         print("GAME OVER :( \n\nAnswer:")
                         board = copy.deepcopy(answerBoard)
                         print_board()
                         break
                    print("WRONG.." + str(lives), "lives left")
                   
            else:
                print("Number already filled.")
            


    
    playagain = input("Play again?: ")

    


        
                
                    
            
            
            
