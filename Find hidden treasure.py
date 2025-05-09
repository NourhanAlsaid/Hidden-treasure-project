import random
width = int(input("Enter the width of the grid: "))
height = int(input("Enter the height of the grid: "))
board = []
number_of_treasures = 0
undiscovered_treasures = 0
for _ in range(height):
    row = []
    for _ in range(width):
        if random.random() >= 0.7:
            row.append('T')
            number_of_treasures += 1
            undiscovered_treasures += 1
        else:
            row.append('o')
    board.append(row)
if number_of_treasures == 0:
    row = random.randint(0, height - 1)
    col = random.randint(0, width - 1)
    board[row][col] = 'T'
    number_of_treasures = 1
    undiscovered_treasures = 1
print(f"Number of treasures hidden: {number_of_treasures}")
while undiscovered_treasures > 0:
    number_of_treasures = 1
    row = int(input(f"Enter the row number (0 to {height-1}):  "))
    col = int(input(f"Enter the column number (0 to {width-1}): "))
    if board[row][col] == 'T':
        print("Congratulations! You found a treasure!")

        board[row][col] = 'X'
        for row in board:
            print((" ".join(row)).replace("T", "o"))
        number_of_treasures -= 1
        undiscovered_treasures -= 1
    else:
        print("No treasure here, try again!")
print("Congratulations! You have found all the treasures!")

for row in board:
    print(" ".join(row))





