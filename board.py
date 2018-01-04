width = int(input('Write the width: '))
height = int(input('Write the height: '))
# x = int(input('Human x postion: '))
# y = int(input('Human y postion: '))

def create_board(width, height):
    board = []
    w = []
    h = []
    w2 = []
    for el in range(width):
        w.append('X')
    for el in range(height - 2):
        h.append('X' + (width - 2) * ' ' + 'X')
    for el in range(width):
        w2.append('X')

    board = [w, h, w2]
    return board

def print_board(board):
    for el in board:
        print (el)

# def insert_player(board,x,y):
#     board[1][1] =
#     return board

def main():
    board = create_board(width, height)
    print (board)
    '''insert_player(board, x, y)'''
    print_board(board)
if __name__ == '__main__':
    main()



#def print_board(board):
