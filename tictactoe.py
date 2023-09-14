import random
import time
def display(pattern):
    for row in pattern:
        print("---------------")
        for element in row:
            if element == 0:
                print(" |  ", end='')
            else:
                print(" | " + str(element), end="")
        print(" |")
    print("---------------")
def ai_move(pattern):
    # AI move logic goes here
    available_positions = [pos for pos in range(1, 10) if pattern[(pos - 1) // 3][(pos - 1) % 3] == 0]

    # For two-way win check
    # case1
    if 1 not in available_positions and 9 not in available_positions and len(available_positions) == 6:
        return 8

        # case2
    if 3 not in available_positions and 7 not in available_positions and len(available_positions) == 6:
        return 4

    # Check for a winning move
    for position in available_positions:
        temp_pattern = [row[:] for row in pattern]
        if put_mark(temp_pattern, position, "O") and check_win(temp_pattern, "O"):
            return position

    # If there's no immediate winning move, check for a blocking move (defensive)
    for position in available_positions:
        temp_pattern = [row[:] for row in pattern]
        if put_mark(temp_pattern, position, "X") and check_win(temp_pattern, "X"):
            return position

    # Prioritize the center, corners, and edges
    strategic_positions = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    for position in strategic_positions:
        if position in available_positions:
            return position

    # If no strategic move is possible, select a random available position
    return random.choice(available_positions)


def put_mark(pattern, pos, mark):
    position = pos - 1
    idx1, idx2 = divmod(position, 3)
    if pattern[idx1][idx2] == 0:
        pattern[idx1][idx2] = mark
        return True
    else:
        return False

def check_win(pattern, mark):
    for i in range(3):
        if all(pattern[i][j] == mark for j in range(3)) or all(pattern[j][i] == mark for j in range(3)):
            return True
    if all(pattern[i][i] == mark for i in range(3)) or all(pattern[i][2 - i] == mark for i in range(3)):
        return True
    return False

def is_draw(turn,end):
    return turn == end

pattern = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("These are the positions of respective boxes")
template = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
display(template)
turn = 0
end = 9

ch = input("Do you want to make first move(Y/N)?")
if ch == "Y":
    turn =0
else:
    turn = 1
    end = 10
while True:
    if is_draw(turn,end):
        print("Match Draw!!")
        break

    player = "Player 1" if turn % 2 == 0 else "Player 2"
    mark = "X" if turn % 2 == 0 else "O"

    if player == "Player 1":
        try:
            pos = int(input(f"Enter the position {player} (1-9): "))
            if pos < 1 or pos > 9:
                raise ValueError()
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
    else:
        # AI player's move
        print("AI is Thinking.",end="")
        time.sleep(0.3)
        print(".",end="")
        time.sleep(0.3)
        print(".",end="")
        time.sleep(0.3)
        print(".")
        ai_position = ai_move(pattern)
        if ai_position is None:
            print("AI can't make a move. Match Draw!!")
            break
        else:
            pos = ai_position

    if put_mark(pattern, pos, mark):
        display(pattern)
        if check_win(pattern, mark):
            print(f"{player} wins!!")
            break
        turn += 1
    else:
        print("That position is already occupied. Try again.")