#include <iostream>
#include <cstdlib>
#include <bitset>
#include <string>

#include "simpio.h"
#include "q4.h"

bool goodImput(std::string tempString) {
    if (tempString.length() != 16) return false;
    for (const auto ch: tempString) {
        if (ch!= '0' and ch!='1') return false;
    }
    return true;

}

void printBit (const unsigned short x) {
    for (int i=15; i>-1; i--) {
        std::cout << ((x >> i) & (unsigned short)1);
    }
}

int q4() {
    std::string tempString;
    unsigned short x = 0;
    unsigned short y = 0;
    const unsigned short one = 1;
    while(true) {
        tempString = getLine("Enter x:");
        if (!goodImput(tempString)) continue;
        for (int i = 0; i<16; i++) {
            if (tempString[i] == '1') {
                x |= one << (15-i);
            }
        }
        break;
    }
    while(true) {
        tempString = getLine("Enter y:");
        if (!goodImput(tempString)) continue;
        for (int i = 0; i<16; i++) {
            if (tempString[i] == '1') {
                y |= one << (15-i);
            }
        }
        break;
    }
    std::cout << " x & y = ";
    printBit(x & y);
    std::cout << std::endl;

    std::cout << " x | y = ";
    printBit(x | y);
    std::cout << std::endl;

    std::cout << " x ^ y = ";
    printBit(x ^ y);
    std::cout << std::endl;

    std::cout << "    ~y = ";
    printBit(~y);
    std::cout << std::endl;

    std::cout << "x & ~y = ";
    printBit(x & ~y);
    std::cout << std::endl;

    return 0;
}




