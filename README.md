# Max-Connect4

Implemented alpha beta pruning with depth limited

Player1 is red/1 or makes the next move in interactive game<br>
Player2 is green/2<br>
  -Programming Language - **Python**<br>
  -The program is written in python 3.9<br>
  -The program is executed in pycharm terminal<br>
  -Start point is maxconnect4.py<br>
  -IDE used is **pycharm**<br>
	
command I tested with are (in pycharm terminal) -<br>
        1. for **One move mode** - python maxconnect4.py one-move input1.txt output.txt 10<br>
        2. for **interactive mode** - python maxconnect4.py interactive input1.txt computer-next 2<br>
        
# New methods/functions implemented are:-<br>
    -In MaxConnect4Game.py<br>
        aiPlayComputer - takes the depth and calls alphaBetaDecisionDepth,<br>
        alphaBetaDecisionDepth - find all the possible moves for max value and then assign each gameboard to minPlayer,<br>
        maxPlayer - find all the successors of the node and calls minPlayer else if depth limit is reach<br>
        calls the calculateEvalScore,<br>
        minPlayer - find all the successors of the node and calls maxPlayer else if depth limit is reach<br>
        calls the calculateEvalScore,<br>
        calculateEvalScore - calculates the eval score for player 1 and player 2 to make a decision,<br>
        countScoreHorizontal - it counts all the players count in row wise and return it to calculateEvalScore<br>
    -In maxconnect4.py<br>
        checkIfMoveValid - checks if the move made by human is valid or not<br>
        isColoumnFull - checks if the coloumn is full or has space<br>
