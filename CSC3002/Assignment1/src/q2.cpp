/*
 * File: q2.cpp
 * --------------------------
 * This is the answer to q2, Assignmet1, CUHK(SZ), 2017 Spring
 * Done by Licheng Mao, 115010202
 */

#include <iostream>
#include <string>
#include "console.h"

using namespace std;

int findDNAMatch(string s1, string s2, int start){
    for(int i=0; i<s1.length(); i++){
        switch(s1[i]){
        case 'A': s1[i]='T'; break;
        case 'T': s1[i]='A'; break;
        case 'G': s1[i]='C'; break;
        case 'C': s1[i]='G'; break;
        }
    }
    for(int i=start; i<s2.length(); i++){
        for(int j=0; j<s1.length(); j++){
            if(s2[i+j]!=s1[j]) break;
            if(j==s1.length()-1) return i;
        }
    }
    return -1;
}
