
def game(board, symbol):
    if board.wins():
        if symbol == 'o':
            print(chr(27) + "[2J \n")
            print(board)
            print ('You win')
        else:
            print('Looser')
    elif board.isFull():
        return 'no winner'
    elif symbol is 'x':

        print(chr(27) + "[2J")
        print(board)
        try:
            wightInput = int(input("Enter wight position\n"))
            heightInput = int(input("Enter height position\n"))

            if board.isEditable(wightInput,heightInput):
                board.editX(wightInput,heightInput)
            else:
                game(board, 'x')
            game(board, 'o')

        except ValueError:
            game(board, 'x')

           
    elif symbol is 'o':
        game(board, 'x')
