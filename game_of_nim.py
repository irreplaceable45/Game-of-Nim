import random
#no of heap = K
print("Description of game \ Heap means stack of coin \ Each heap has certain no of coins number of coins \ set heap and no of coins in each heap continuous by yourself")
K=int(input("Enter of heap you want: "))
size=[]
for k in range(1,K+1):
    n="heap"
    heap=int(input(f"Enter the no of coins in {n +str(k)}: "))
    size.append(heap)
Player1=input("Enter Player 1 Name: ")
Player2=input("Enter Player 2 Name: ")
print(f"No of coins in each heap shown in these list: {size}")
while size.count(0) != K:
    print(f"{Player1}'s turn")
    print(f"No of coins in each heap shown in these list: {size}")
    a=int(input("Enter from which head you want to remove coin from the above list,like, 1 for first, 2 for second, it will continue: "))
    head_chosen= size[a-1]
    b=int(input("Enter no of coins you want to remove: "))
    new_coin_number=head_chosen-b
    size.remove(head_chosen)
    size.append(new_coin_number)
    print(f"No of coins in each heap shown in these list: {size}")
    if size.count(0) == K:
        print(f"{Player1} won the game")
        break
    else:
        print(f"{Player2}'s turn")
        print(f"No of coins in each heap shown in these list: {size}")
        a=int(input("Enter from which head you want to remove coin from the above list,like, 1 for first, 2 for second, it will continue: "))
        head_chosen= size[a-1]
        b=int(input("Enter no of coins you want to remove: "))
        new_coin_number=head_chosen-b
        size.remove(head_chosen)
        size.append(new_coin_number)
        print(f"No of coins in each heap shown in these list: {size}")
        if size.count(0) == K:
            print(f"{Player2} won the game")
            break
