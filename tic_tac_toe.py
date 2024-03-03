def printboard(x_state, zero_state):
    zero = 'X' if x_state[0] else ('0' if zero_state[0] else 0)
    one = 'X' if x_state[1] else ('0' if zero_state[1] else 1)
    two = 'X' if x_state[2] else ('0' if zero_state[2] else 2)
    three = 'X' if x_state[3] else ('0' if zero_state[3] else 3)
    four = 'X' if x_state[4] else ('0' if zero_state[4] else 4)
    five = 'X' if x_state[5] else ('0' if zero_state[5] else 5)
    six = 'X' if x_state[6] else ('0' if zero_state[6] else 6)
    seven = 'X' if x_state[7] else ('0' if zero_state[7] else 7)
    eight = 'X' if x_state[8] else ('0' if zero_state[8] else 8)

    print(f"{zero} | {one} | {two} ")
    print("--|---|---")
    print(f"{three} | {four} | {five} ")
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ")

def check_winner(x_state, zero_state):
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in win_conditions:
        if sum(x_state[i] for i in win) == 3:
            return 'X'
        elif sum(zero_state[i] for i in win) == 3:
            return '0'
    
    return None

if __name__ == "__main__":
    x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zero_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for x and 0 for zero
    print("Welcome Everyone!!")
    
    while True:
        printboard(x_state, zero_state)
        
        if turn == 1:
            print("X's chance")
            value = int(input("Please enter value where you want to insert: \n"))
            x_state[value] = 1
        else:
            print("0's chance")
            value = int(input("Please enter value where you want to insert: \n"))
            zero_state[value] = 1

        winner = check_winner(x_state, zero_state)
        if winner is not None:
                print(f"{winner} won the match!")
                print("Khatam Tata Bye Bye!")
                break
        
        turn = 1 - turn
