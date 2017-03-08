#include <iostream>
#include <fstream>
#include <string>
#include "console.h"
#include "q1.h"
#include "q2.h"
#include "q3.h"
#include "q4.h"
#include "q5.h"
using namespace std;

int main() {
    string var1, var2;
    cout << "Test answer for Assignment1" << endl;
    cout << "q1:" << endl;
    q1();
    cout << "q2:" << endl;
    cout << "Please input s1 and s2." << endl;
    cin >> var1 >> var2;
    cout << findDNAMatch(var1, var2) << endl;
    cout << "q3:" << endl;
    ifstream is ("comment_in.txt");
    ofstream os ("comment_out.txt");
    removeComments(is, os);
    is.close();
    os.close();
    cout << "successfully output to comment_out.txt"<< endl;
    cout << "q4" << endl;
    searchCode();
    cout << "q5" << endl;
    q5();
    return 0;
}
