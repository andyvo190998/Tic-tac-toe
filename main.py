import os
clear = lambda: os.system('clear')

print("welcome to tic tac toe game \n")
print("please type where do you want to mark by choose the corresponding number\n")


row1_list = ["    ","    ","    ","    ","    ","    ","    ","    ","    "]
colum = "|"

row2_list = ["    ","|","    ","|","    "]

row3_list = ["    ","|","    ","|","    \n"]
game_on = True

def render_graphic():
    print("  1  |  2  |  3  ")
    print("-----|-----|-----")
    print("  4  |  5  |  6  ")
    print("-----|-----|-----")
    print("  7  |  8  |  9  \n")

    row1 = print(row1_list[0],colum,row1_list[1],colum,row1_list[2])
    print("-----|------|-----")

    row2 = print(row1_list[3],colum,row1_list[4],colum,row1_list[5])
    print("-----|------|-----")

    row3 = print(row1_list[6],colum,row1_list[7],colum,row1_list[8])
def check_result(list1):
    global game_on
    for i in [1,4,7]:
        if i in list1:
            if i + 1 in list1 and i + 2 in list1:
                print("Player 1 wins")
                game_on = False

    for i in [1,2,3]:
        if i in list1:
            if i + 3 in list1 and i + 6 in list1:
                print("Player 1 wins")
                game_on = False

            elif i + 4 in list1 and i + 8 in list1:
                print("Player 1 wins")
                game_on = False

            elif i + 2 in list1 and i + 4 in list1 and i != 1 and i != 2:
                print("Player 1 wins")
                game_on = False

    # if list1[0] == 3 and list1[0] + 2 in list1 and list1[0] + 4 in list1:
    #     print("Player 1 wins")
    #     game_on = False





def check_result2(list2):
    global game_on
    for i in [1,4,7]:
        if i in list2:
            if i + 1 in list2 and i + 2 in list2:
                print("Player 2 wins")
                game_on = False
                break
    for i in [1,2,3]:
        if i in list2:
            if i + 3 in list2 and i + 6 in list2:
                print("Player 2 wins")
                game_on = False
                break

            elif i + 4 in list2 and i + 8 in list2:
                print("Player 2 wins")
                game_on = False
                break

            elif i + 2 in list2 and i + 4 in list2 and i != 1 and i != 2:
                print("Player 2 wins")
                game_on = False
                break

player1_list = []
player2_list = []
while game_on == True:
    render_graphic()
    valid1 = True
    valid2 = True

    while valid1:
        player1 = int(input("player 1 choses a position: \n"))
        player1_mark = " X  "
        if player1 not in player1_list and player1 not in player2_list:
            row1_list[player1-1] = player1_mark
            render_graphic()
            player1_list.append(player1)
            sorted_list1 = sorted(player1_list)
            print(sorted_list1)
            check_result(list1=sorted_list1)
            valid1 = False
        else:
            print("invalid position")
        if len(player1_list) == 5:
            print("DRAW!!!")
            game_on = False
            valid2 = False
    if game_on == True:
        while valid2:
            player2 = int(input("player 2 choses a position: \n"))
            player2_mark = " O  "
            if player2 not in player2_list and player2 not in player1_list:
                row1_list[player2-1] = player2_mark
                render_graphic()
                player2_list.append(player2)
                sorted_list2 = sorted(player2_list)
                check_result2(list2=sorted_list2)
                valid2 = False
            else:
                print("invalid position")
