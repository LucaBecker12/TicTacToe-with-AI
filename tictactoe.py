from random import randint
from copy import deepcopy
import os
import minimax


class Game():
    def __init__(self):
        self.player = "X"
        self.computer = 'O'
        self.EMPTY = 0
        self.board = [[self.EMPTY for x in range(3)] for x in range(3)]
        self.current_player = self.player

    # Represents the main loop of the game
    def mainLoop(self):
        isPlaying = True

        while isPlaying:
            # Make a move
            if self.current_player == self.player:
                position = int(input('Type position: ')) - 1
                move = [(position//3), (position % 3)]
                while (not self.isValidMove(move)):
                    print('That wasn\'t a valid move. \nTry again: ')
                    position = int(input('Type position: ')) - 1
                    move = [(position//3), (position % 3)]
                self.playMove(move, self.player)
            else:
                move = minimax.find_best_move(deepcopy(self.board))
                self.playMove(move, self.computer)

            # Change Player
            self.changePlayer()

            # Print Game
            self.printGame()

            # Check for end of Game
            state = self.checkForWin()
            if state == self.player:
                print('Player won')
            elif state == self.computer:
                print('Computer won')
            elif state == 1:
                print("Draw")

            # changes isPlaying state if the game has terminated
            if state != 0:
                isPlaying = False

    # Let's the computer choose a random move
    def playRandomMove(self):
        position = randint(0, 8)
        move = ((position//3), (position % 3))
        while (not self.isValidMove(move)):
            position = randint(0, 8)
            move = ((position//3), (position % 3))
        self.playMove(move, self.computer)

    # A function which simple executes a move
    def playMove(self, move, player):
        self.board[move[0]][move[1]] = player

    # Checks if game is in a terminated state
    def checkForWin(self):
        for i in range(3):
            if self.board[i][0] != self.EMPTY:
                if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
                    return self.board[i][0]
            if self.board[0][i] != self.EMPTY:
                if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
                    return self.board[0][i]

        if self.board[0][0] != self.EMPTY:
            if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
                return self.board[0][0]

        if self.board[0][2] != self.EMPTY:
            if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
                return self.board[0][2]

        if self.isMoveLeft():
            return 0
        else:
            return 1

    # Returns wheter a move is left or not
    def isMoveLeft(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.EMPTY:
                    return True
        return False

    # Checks if a move is valid or not
    def isValidMove(self, move):
        if self.board[move[0]][move[1]] == 0:
            return True
        else:
            return False

    # Changes the Player
    def changePlayer(self):
        if self.current_player == self.player:
            self.current_player = self.computer
        else:
            self.current_player = self.player

    # Function used to print the game to the console
    def printGame(self):
        print('-'*19)
        for i in range(3):
            print('|', end='')
            for j in range(3):
                if self.board[i][j] == self.EMPTY:
                    print('{:^5}'.format(' '), end='|')
                else:
                    print('{:^5}'.format(self.board[i][j]), end='|')
            print(end='\n')
            print('-'*19)


game = Game()
game.mainLoop()
