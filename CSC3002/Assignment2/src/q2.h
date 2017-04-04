#ifndef _q2_h
#define _q2_h

#include <string>
#include <iostream>
#include "vector.h"
#include "error.h"

const int WINNING_POSITION = 1000;
const int LOSING_POSITION = -WINNING_POSITION;
const int MAX_DEPTH = 10;

typedef int Move;

enum Player {EMPTY, HUMAN, COMPUTER};

Player opponent(Player player);

const Player STARTING_PLAYER = COMPUTER;
std::string getPlayerNotation(Player player);
class TicTacToe {

public:
//    TicTacToe
    void play();
    void printInstruction();

private:
    void initGame();
    Player chessboard[3][3] = {EMPTY};
//    Player (*chessboard_ptr) = &chessboard;
    Player currentPlayer = STARTING_PLAYER;
    Player winner();
    bool gameIsOver();
    void displayChessboard();
    void displaySampleChessboard();
    void displayGame();
    void makeMove(Move move);
//    void retractMove(Move move);
    void retractMove(Move move);
    void displayMove(Move move);
    Move getComputerMove();
//    std::string getPlayerNotation();
    Move getUserMove();
    void announceResult();
    void generateMoveList(Vector<Move> &moveList);
    Move findBestMove();
    Move findBestMove(int depth, int &rating);
    int evaluatePosition(int depth);
    int evaulateStaticPosition();
};


#endif
