#include <iostream>
#include <string>
#include "q2.h"
#include "error.h"
#include "simpio.h"
#include "vector.h"

Player opponent(Player player) {
    return (player == HUMAN) ?  COMPUTER : HUMAN;
}

void TicTacToe::play() {
        initGame();
        Move move = getComputerMove();
        displayMove(move);
        makeMove(move);
        currentPlayer = opponent(currentPlayer);
        while (!gameIsOver()) {
            displayGame();
            if (currentPlayer == HUMAN) {
                makeMove(getUserMove());
            } else {
                Move move = getComputerMove();
                displayMove(move);
                makeMove(move);
            }
            currentPlayer = opponent(currentPlayer);
        }
        announceResult();
    }


void TicTacToe::printInstruction() {
    std::cout << "Welcome to TicTacToe, the game of three in a row." << std::endl;
    std::cout << "I'll be X, and you'll be O." << std::endl;
    std::cout << "The squares are numbered like this:" << std::endl;
//    std::cout << "***RESERVED for sample***" << std::endl;
    displaySampleChessboard();
    return;
}

void TicTacToe::initGame() {
    printInstruction();
    return;
}

Player TicTacToe::winner(){
    for (int i=0; i<3; i++){
        // check row
        if (chessboard[i][0] != EMPTY && chessboard[i][0] == chessboard[i][1] && chessboard[i][0] == chessboard[i][2]) return chessboard[i][0];
        // check column
        if (chessboard[0][i] != EMPTY && chessboard[0][i] == chessboard[1][i] && chessboard[0][i] == chessboard[2][i]) return chessboard[0][i];
    }
    if (chessboard[0][0] != EMPTY && chessboard[0][0] == chessboard[1][1] && chessboard[0][0] == chessboard[2][2]) return chessboard[0][0];
    if (chessboard[2][0] != EMPTY && chessboard[2][0] == chessboard[1][1] && chessboard[2][0] == chessboard[0][2]) return chessboard[2][0];
    return EMPTY;
}

bool TicTacToe::gameIsOver(){
    if (winner()!= EMPTY) return true;
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            if (chessboard[i][j] == EMPTY) return false;
        }
    }
    return true;
}

std::string getPlayerNotation(Player player){
    return (player==EMPTY)? " ": (player==HUMAN)? "O": "X";
}

void TicTacToe::displayChessboard(){
    std::cout << std::endl;
    std::cout << " " << getPlayerNotation(chessboard[0][0])
            << " | " << getPlayerNotation(chessboard[0][1])
            << " | " << getPlayerNotation(chessboard[0][2]) << " " <<  std::endl;
    std::cout << "---+---+---" << std::endl;
    std::cout << " " << getPlayerNotation(chessboard[1][0])
            << " | " << getPlayerNotation(chessboard[1][1])
            << " | " << getPlayerNotation(chessboard[1][2]) << " " <<  std::endl;
    std::cout << "---+---+---" << std::endl;
    std::cout << " " << getPlayerNotation(chessboard[2][0])
            << " | " << getPlayerNotation(chessboard[2][1])
            << " | " << getPlayerNotation(chessboard[2][2]) << " " <<  std::endl;
    std::cout << std::endl;
}

void TicTacToe::displaySampleChessboard(){
    std::cout << std::endl;
    std::cout << " " << "1"
            << " | " << "2"
            << " | " << "3" << " " <<  std::endl;
    std::cout << "---+---+---" << std::endl;
    std::cout << " " << "4"
            << " | " << "5"
            << " | " << "6" << " " <<  std::endl;
    std::cout << "---+---+---" << std::endl;
    std::cout << " " << "7"
            << " | " << "8"
            << " | " << "9" << " " <<  std::endl;
    std::cout << std::endl;
}

void TicTacToe::displayGame() {
        std::cout << "The game now looks like this:" << std::endl;
        displayChessboard();
    }

void TicTacToe::makeMove(Move move){
    chessboard[move/3][move%3] = currentPlayer;
}

void TicTacToe::retractMove(Move move){
    chessboard[move/3][move%3] = EMPTY;
}

Move TicTacToe::getComputerMove(){
    return findBestMove();
}

void TicTacToe::displayMove(Move move) {
    std::cout << "I'll move to " << std::to_string(move+1) << "." << std::endl;
    return;
}

Move TicTacToe::getUserMove(){
    std::cout << "Your move." << std::endl;
    while (true) {
        Move move = getInteger("What square?")-1;
        return move;
    }
}

void TicTacToe::announceResult(){
    std::cout << "The final position looks like this:" << std::endl;
    displayChessboard();
    if (winner()==EMPTY){
        std::cout << "No one wins." << std::endl;
    }
    else if (winner()==COMPUTER){
        std::cout << "I win." << std::endl;
    }
    else {
        std::cout << "You win." << std::endl;
    }
//    std::cout << "Happy to announce the result!" << std::endl;
}

Move TicTacToe::findBestMove() {
    int rating;
    return findBestMove(0, rating);
}

void TicTacToe::generateMoveList(Vector<Move> &moveList){
    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            if(chessboard[i][j] == EMPTY) moveList.add(i*3+j);
        }
//    f("movelist %i\n", moveList.size());
    }
}

Move TicTacToe::findBestMove(int depth, int &rating) {
    Vector<Move> moveList;
    Move bestMove;
    int minRating = WINNING_POSITION + 1;
    generateMoveList(moveList);
    if (moveList.isEmpty()) error("No moves available");

    for (auto move : moveList) {
        makeMove(move);
        currentPlayer=opponent(currentPlayer);

        int moveRating = evaluatePosition(depth + 1);
        if (moveRating < minRating) {
            bestMove = move;
//            f("rating%i\n", moveRating);
            minRating = moveRating;
        }
        currentPlayer=opponent(currentPlayer);
        retractMove(move);
    }
    rating = -minRating;
    return bestMove;
}

int TicTacToe::evaulateStaticPosition(){
    return (winner()==EMPTY)? 0: (winner()==currentPlayer)? 1 : -1;
}

int TicTacToe::evaluatePosition(int depth) {
    if (gameIsOver() || depth >= MAX_DEPTH) {
        return evaulateStaticPosition();
    }
    int rating;
    findBestMove(depth, rating);
    return rating;
}
