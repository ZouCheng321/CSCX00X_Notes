#ifndef _q2_h
#define _q2_h


#include <iostream>
#include <string>
#include "pqueue.h"
#include "simpio.h"
#include "strlib.h"
#include "tokenscanner.h"

namespace q2 {

/* Function prototypes */
void executeCommand(TokenScanner & scanner, Queue<std::string> & queue);
void helpCommand();
void listQueue(const Queue<std::string> & queue);

/* Main program */
int q2();

}

#endif
