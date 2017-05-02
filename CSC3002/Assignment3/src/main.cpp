#include <iostream>
#include <cmath>
#include <string>
#include "console.h"


#include "q1.h"
#include "q2.h"
#include "q3.h"
#include "q4.h"
#include "q5.h"

int main() {

    std::cout << "Assignment3" << std::endl;
    std::cout << "By Mao Licheng" << std::endl;
    std::cout << "Stu ID: 115010202" << std::endl;
    std::cout << "This is a test of q1-q5" << std::endl;


    std::cout << "### q1 ###" << std::endl;
    q1();
    std::cout << "### q1 done ###" << std::endl;


    std::cout << "### q2 ###" << std::endl;
    try {
        q2::q2();
    }
    catch (int e) {};
    std::cout << "### q2 done ###" << std::endl;


    std::cout << "### q3 ###" << std::endl;
    try {
        q3::q3();
    }
    catch (int e) {};
    std::cout << "### q3 done ###" << std::endl;


    std::cout << "### q4 ###" << std::endl;
    q4();
    std::cout << "### q4 done ###" << std::endl;


    std::cout << "### q5 ###" << std::endl;
    q5();
    std::cout << "### q5 done ###" << std::endl;

    return 0;
}
