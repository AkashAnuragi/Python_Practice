"""
TIC TAC TOE

"""

li = [1,2,3,4,5,6,7,8,9]
player = "X"
while True:
    print("\n\t\t  TIC_TAC_TOE")
    print(f"\n\t\t   {li[0]} | {li[1]} | {li[2]} ")
    print("\t\t  -----------")
    print(f"\t\t   {li[3]} | {li[4]} | {li[5]} ")
    print("\t\t  -----------")
    print(f"\t\t   {li[6]} | {li[7]} | {li[8]} ")

    print(f"\n\t\t Player {player} Turn:", end="")
    ch = int(input())
    li[ch-1]=player

    if player == "X":
        player = "O"
    else:
        player = "X"
