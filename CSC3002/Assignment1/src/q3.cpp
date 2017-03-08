/*
 * File: q3.cpp
 * --------------------------
 * This is the answer to q3, Assignmet1, CUHK(SZ), 2017 Spring
 * Done by Licheng Mao, 115010202
 */

#include <iostream>
using namespace std;

void removeComments(istream & is, ostream & os){
    char ch=0;
    char prevCh=0;
    const bool isQuoteEnable=false;
    const int inSingleQuote=4;
    const int inDoubleQuote=3;
    const int inBlockComment=2;
    const int inLineComment=1;
    const int inDefault=0;
    int status=inDefault;
    while (ch=is.get()){
        switch(status){
            case inSingleQuote:{
                if(ch=='\''&&prevCh!='\\')status=inDefault;
                break;
            }
            case inDoubleQuote:{
                if(ch=='\"'&&prevCh!='\\')status=inDefault;
                break;
            }
            case inLineComment:{
                if(ch=='\n')status=inDefault;
                prevCh=0;
                break;
            }
            case inBlockComment:{
                if(ch=='/'&&prevCh=='*'){
                    status=inDefault;
                    ch=0;
                }
                prevCh=0;
                break;
            }
            case inDefault:{
                if(ch=='/'&&prevCh=='/'){
                    status=inLineComment;
                    ch=0;
                    prevCh=0;
                } else if(ch=='*'&&prevCh=='/'){
                    status=inBlockComment;
                    ch=0;
                    prevCh=0;
                } else if(ch=='\''&&isQuoteEnable){
                    status=inSingleQuote;
                } else if(ch=='\"'&&isQuoteEnable){
                    status=inDoubleQuote;
                }
                break;
            }
        }
        if(prevCh) os.put(prevCh);
        if (ch==EOF){
            if(status!=inDefault){
                cout<<"Warning! Unfinished quote/comment found." <<endl;
            }
            break;
        }
        prevCh=ch;

    }
}
