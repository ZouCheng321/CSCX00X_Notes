#include <iostream>
#include <cmath>
#include <string>
#include "console.h"


#include "q1.h"
#include "q2.h"
#include "q3.h"
#include "q4.h"

int main() {


//    TokenScanner scanner;
//    scanner.ignoreWhitespace();
//    scanner.scanNumbers();
//    scanner.scanStrings();

//    scanner.setInput(getLine("***> "));
//    std::cout << scanner.hasMoreTokens() << std::endl;
//    std::cout << scanner.getStringValue(scanner.nextToken()) <<
//                 std::endl;
//    std::cout << scanner.hasMoreTokens() << std::endl;
//    std::cout << std::stoi(scanner.getStringValue(scanner.nextToken())) <<
//                 std::endl;


    std::cout << "Assignment3" << std::endl;
    std::cout << "By Mao Licheng" << std::endl;
    std::cout << "Stu ID: 115010202" << std::endl;
    std::cout << "This is a test of q1-q5" << std::endl;


    std::cout << "### q1 ###" << std::endl;
    q1();
    std::cout << "### q1 to be done ###" << std::endl;


    std::cout << "### q2 ###" << std::endl;
    try {
        q2::q2();
    }
    catch (int e) {};
    std::cout << "### q2 to be done ###" << std::endl;


    std::cout << "### q3 ###" << std::endl;
    try {
        q3::q3();
    }
    catch (int e) {};
    std::cout << "### q3 tobe done ###" << std::endl;


    std::cout << "### q4 ###" << std::endl;
    q4();
    std::cout << "### q4 to be done ###" << std::endl;


    std::cout << "### q5 ###" << std::endl;

    std::cout << "### q5 to be done ###" << std::endl;

    return 0;
}
