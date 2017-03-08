/*
 * File: q1.cpp
 * --------------------------
 * This is the answer to q1, Assignmet1, CUHK(SZ), 2017 Spring
 * Done by Licheng Mao, 115010202
 */

#include <iostream>
#include "random.h"

using namespace std;

int q1(){
    int countHead = 0;
    int countFlip = 0;
    while(countHead!=3){
        if(randomBool()){
            cout << "heads" << endl;
            countHead++;
        } else {
            cout << "tails" << endl;
            countHead=0;
        }
        countFlip++;
    }
    cout << "It tooks " << countFlip << " flips to get " << countHead << " consecutive heads." << endl;
    return 0;
}
