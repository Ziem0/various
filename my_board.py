# width = int(input('type a width: '))
# height = int(input('type a height: '))
#
# def create_board(width, height):
#     boards = []
#     list_w = list('X'*width)
#     boards.append(list_w)
#     for list_h in range(height-2):
#         list_h = list('X'+' '*(width-2)+'X')
#         boards.append(list_h)
#     boards.append(list_w)
#     return boards
#
# def print_board(boards):
#     for row in boards:
#         line = ' '.join(row)
#         print (line)
#
# def main():
#     boards = create_board(width,height)
#     print_board(boards)
#
# main()
#
#
#
#
#
#
#
#
#
#
# def create_board(width, height):
#   width = int(width)
#   height = int(height)
#   board = []
#   for line in range(1, height + 1):
#       rows = []
#       if line == 1:
#           for char in range(1, width+1):
#               rows.append('X')
#           board.append(rows)
#       elif line in range(2, height):
#           rows.append('X')
#           for char in range(2, width):
#               rows.append(' ')
#           rows.append('X')
#           board.append(rows)
#       elif line == height:
#           for char in range(1, width+1):
#               rows.append('X')
#           board.append(rows)
#   return board
#
#
# def print_board(board):
#   for line in board:
#       print(" ".join(line))
#
#
# board = create_board(5, 5)
# print_board(board)
#
#



width = int(input('Write the width: '))
height = int(input('Write the height: '))
#x = int(input('Human x postion: '))
#y = int(input('Human y postion: '))

def create_board(width, height):
   h = []
   w = []
   w2 = []
   for el in range(width):
       w.append('X')
   for el in range(height - 2):
       h1 = []
       h.append(h1)
       for el in range(width):
           if el == 0 or el == width - 1 :
               h1.append('X')
           else:
               h1.append(' ')

   for el in range(width):
       w2.append('X')

   board = [w, *h, w2]
   return board

def print_board(board):
   for el in board:
       print (*el)

def insert_player(board,x,y):
   board[x][y] = '@'
   return board

def main():
   board = create_board(width, height)
   print (board)
   insert_player(board, 1, 1)
   print_board(board)
if __name__ == '__main__':
   main()
