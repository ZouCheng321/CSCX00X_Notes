/*
 * File: q4.cpp
 * --------------------------
 * This is the answer to q4, Assignmet1, CUHK(SZ), 2017 Spring
 * Done by Licheng Mao, 115010202
 */

#include <iostream>
#include <fstream>
#include <string>
#include "error.h"
#include "map.h"
#include "strlib.h"

using namespace std;

void readCodeFile(string filename, Map<string, string> & map){
    ifstream infile;
    infile.open(filename.c_str());
    if(infile.fail()) error("Can't read the data file.");
    string line;
    while (getline(infile, line)){
        line.pop_back();
        if (line.length()<4 | line[3] != '-'){
            error("Illegal data line: " + line);
        }
        string code = line.substr(0, 3);
        map.put(code, line.substr(4));
        if (map.containsKey(line.substr(4))){
            map.put(line.substr(4), map.get(line.substr(4))+'\n'+code);
        } else{
            map.put(line.substr(4), code);
        }

    }
    infile.close();
}

int searchCode(){
    Map<int, string> forAnswer;
    forAnswer.put(1,"...");
    Map<string, string> areaCodes;
    readCodeFile("AreaCodes.txt", areaCodes);
    cin.get();
    while (true) {
        string line;
        cout << "Enter area code or state name: ";
        getline(cin,line);
        if (line == "") break;
        string code = line;
        if (areaCodes.containsKey(code)){
            cout << areaCodes.get(code) << endl;
        }
    }
    return 0;
}
