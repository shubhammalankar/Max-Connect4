#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import sys
from MaxConnect4Game import *


def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:  # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlayComputer()  # Make a move (only random is implemented)

    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()

def checkIfMoveValid(move):
    if 0 < move < 8:
        return True

def isColoumnFull(currentGame, move):
    if not currentGame.playPiece(move - 1):#it places the move in the coloumn and check if it is valid
        return True

def interactiveGame(currentGame, nextMove):
    # Fill me in
    if currentGame.pieceCount == 42:  # Is the board full already?
        currentGame.printGameBoard()
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    #print("depthLevel", currentGame.depthLimit)
    if nextMove == 'human-next':
        print('human-next')
        while currentGame.getPieceCount() != 42:
            humanMove = int(input('Enter a coloumn number between 1 to 7:'))
            if not checkIfMoveValid(humanMove):
                print('Invalid coloumn number. Enter a number between 1 to 7')
                continue
            if isColoumnFull(currentGame, humanMove):
                print('Coloumn is full')
                continue
            print('Move made by human - ', humanMove)
            currentGame.gameFile = open('human.txt', 'w')
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            if currentGame.getPieceCount() >= 42:
                print('All the places are filled. No possible move')
                currentGame.countScore()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                break
            else:
                print('AI is thinking...')
                if currentGame.currentTurn == 1:
                    currentGame.currentTurn = 2
                elif currentGame.currentTurn == 2:
                    currentGame.currentTurn = 1
                currentGame.aiPlayComputer()
                print('Game state after move:')
                currentGame.printGameBoard()
                currentGame.countScore()
                print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                currentGame.gameFile = open('computer.txt', 'w')
                currentGame.printGameBoardToFile()
                currentGame.gameFile.close()
    else:
        currentGame.aiPlayComputer()
        print('Game state after move:')
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        currentGame.gameFile = open('computer.txt', 'w')
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()
        interactiveGame(currentGame, 'human-next')



def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    print(game_mode)
    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game()  # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])  # print the next player number either 1 or 2
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        nextMove = argv[3]
        #print(nextMove)
        if not nextMove == 'human-next' and not nextMove == 'computer-next':
            print('%s is an unrecognized next move' % nextMove)
            sys.exit(2)
        currentGame.depthLimit = int(argv[4])
        interactiveGame(currentGame, nextMove)  # Be sure to pass whatever else you need from the command line
    else:  # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame)  # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)

    # python maxconnect4.py one-move input1.txt output.txt 10
    # python maxconnect4.py interactive input1.txt computer-next 10
