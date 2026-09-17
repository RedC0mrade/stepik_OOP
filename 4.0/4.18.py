class Knight:

    def __init__(self, horizontal: str, vertical: int, color: str):

        self.horizontal = horizontal
        self.vertical = 8 - vertical
        self.color = color

    def get_char(self):
        return "N"

    def can_move(self, horizontal, vertical) -> bool:

        if 0 > vertical > 9 and 96 < ord(horizontal) < 105:
            return False

        if abs(self.vertical - vertical) not in [1, 2] and abs(ord(self.horizontal) - ord(horizontal)) not in [1, 2]:
            return False

        if abs(self.vertical - vertical) + abs(ord(self.horizontal) - ord(horizontal)) != 3:
            return False

        return True
    
    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal=horizontal, vertical=vertical):
            self.horizontal = horizontal
            self.vertical = vertical


    def draw_board(self):

        horizontal_on_board = ord(self.horizontal)-97
        board = [["."] * 8 for _ in range(8)]
        board[self.vertical][horizontal_on_board] = "N"

        try:
            board[self.vertical+2][horizontal_on_board+1] = '*'
        except:
            pass
        
        try:
            board[self.vertical+2][horizontal_on_board-1] = '*'
        except:
            pass
        
        try:
            board[self.vertical+1][horizontal_on_board-2] = '*'
        except:
            pass
        
        try:
            board[self.vertical+1][horizontal_on_board+2] = '*'
        except:
            pass
        
        try:
            board[self.vertical-1][horizontal_on_board-2] = '*'
        except:
            pass
        
        try:
            board[self.vertical-1][horizontal_on_board+2] = '*' #!
        except:
            pass
        
        try:
            board[self.vertical-2][horizontal_on_board+1] = '*'
        except:
            pass
        
        try:
            board[self.vertical-2][horizontal_on_board-1] = '*'
        except:
            pass
                

        [print(*i) for i in board]



# TEST_1:
knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)

# TEST_2:
knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

# TEST_3:
knight = Knight('c', 3, 'white')

knight.draw_board()

# TEST_4:
knight = Knight('e', 5, 'black')

knight.draw_board()
knight.move_to('d', 3)
print()
knight.draw_board()

# TEST_5:
knight = Knight('a', 1, 'white')

knight.draw_board()
knight.move_to('e', 8)
print()
knight.draw_board()

# TEST_6:
knight = Knight('g', 7, 'black')
knight.draw_board()

# TEST_7:
knight = Knight('d', 8, 'white')
knight.draw_board()

# TEST_8:
knight = Knight('h', 1, 'black')
knight.draw_board()
