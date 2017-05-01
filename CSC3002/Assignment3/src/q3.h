#ifndef _q3_h
#define _q3_h


#include <iostream>
#include <string>
#include "pqueue_heap.h"
#include "simpio.h"
#include "strlib.h"
#include "tokenscanner.h"

namespace q3 {

/* Function prototypes */
void executeCommand(TokenScanner & scanner, Queue<std::string> & queue);
void helpCommand();
void listQueue(const Queue<std::string> & queue);

/* Main program */
int q3();

}

#endif
