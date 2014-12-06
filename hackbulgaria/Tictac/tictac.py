from board import Board
import controls

def main():
    board = Board()
    print("Hi.. to start game enter 'start'")
    print("press CTRL + D to exit from game")
    if input() == 'start':
        controls.game(board,'x')
        while True:
            again = input('Do you want play again?(y/n)\n')
            if again == 'y':
                board.initBoard()
                controls.game(board,'x')
            elif again == 'n':
                break
    print('Buy...')





if __name__ == '__main__':
    main()