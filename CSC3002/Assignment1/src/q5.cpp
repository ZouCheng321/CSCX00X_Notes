/*
 * File: q5.cpp
 * --------------------------
 * This is the answer to q5, Assignmet1, CUHK(SZ), 2017 Spring
 * Done by Licheng Mao, 115010202
 */

#include <iostream>
#include <string>
#include <cctype>
#include "simpio.h"
#include "stack.h"
#include "strlib.h"
#include "tokenscanner.h"

int priority(char ch){
    switch(ch){
    case '+':return 1;
    case '-':return 1;
    case '*':return 1;
    case '/':return 1;
    default:return -1;
    }
}

void applyOperator(char op, Stack<double> & opdStack){
    double result=0;
    double rhs=opdStack.pop();
    double lhs=opdStack.pop();
    switch (op){
        case '+': result = lhs+rhs;opdStack.push(result);break;
        case '-': result = lhs-rhs;opdStack.push(result);break;
        case '*': result = lhs*rhs;opdStack.push(result);break;
        case '/': result = lhs/rhs;opdStack.push(result);break;
        default: break;
    }

}

void q5(){
    std::string input;
    std::cout << "Please input an expression." << std::endl;
    while (true){
        input=getLine("> ");
        if(input==""){
            std::cout<<std::endl;break;
        }
        TokenScanner scanner(input);
        scanner.getPosition();
        // Implementation of the shunting-yard algorithm.
        Stack<double> opdStack;
        Stack<char> optStack;
        bool prevOpt=true;
        std::string opCache;
        char ch=0;
        for(int i=0;i<input.length();i++){
            ch=input[i];
            if(ch==' ')continue;
            if (ch=='-'&&prevOpt){
                opCache+=ch;
                prevOpt=false;
            }else if(isdigit(ch)||ch=='.'){
                opCache+=ch;
                prevOpt=false;
            }else {
                prevOpt=true;
                opdStack.push(stringToDouble(opCache));
                opCache="";
                if(!optStack.isEmpty()){
                    while(!optStack.isEmpty()&&priority(ch)<=priority(optStack.peek())){
                        applyOperator(optStack.pop(),opdStack);
                    }
                }
                optStack.push(ch);
            }
        }
        opdStack.push(stringToDouble(opCache));
        while(!optStack.isEmpty()){
                applyOperator(optStack.pop(),opdStack);
        }
        std::cout << opdStack.pop() << std::endl;
    }
    return;
}

