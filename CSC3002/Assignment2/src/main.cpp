#include <iostream>
#include <cmath>
#include <string>
#include "console.h"
#include "gwindow.h"

#include "q1.h"
#include "q2.h"
#include "q3.h"
#include "q4.h"
#include "q5.h"
#include "q6.h"
#include "q7.h"

int main() {
    std::cout << "Assignment2" << std::endl;
    std::cout << "By Mao Licheng" << std::endl;
    std::cout << "Stu ID: 115010202" << std::endl;


    std::cout << "q1" << std::endl;
    GWindow gw;
    double xc = gw.getWidth() / 2;
    double yc = gw.getHeight() / 2;
    drawHFractal(gw, xc, yc, 100, 3);
    std::cout << "Please look at another window" << std::endl;
    std::cout << "q1 done" << std::endl;


    std::cout << "q2" << std::endl;
    TicTacToe game;
    game.play();
    std::cout << "q2 done" << std::endl;


    std::cout << "q3" << std::endl;
    Vector<int> q3v{1,5,3,4,5,5,5,5,6,7,5,5};
    std::cout << "Majority Element for the test case is: "
              << std::to_string(findMajorityElement(q3v)) << std::endl;
    std::cout << "q3 done" << std::endl;


    std::cout << "q4" << std::endl;
    q4();
    std::cout << "q4 done" << std::endl;


    std::cout << "q5" << std::endl;
    q5();
    std::cout << "q5 done" << std::endl;


    std::cout << "q6" << std::endl;
    q6();
    std::cout << "q6 done" << std::endl;


    std::cout << "q7" << std::endl;
    q7();
    std::cout << "q7 done" << std::endl;


    return 0;
}
