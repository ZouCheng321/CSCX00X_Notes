#include <iostream>
#include <cassert>

#include "intarray.h"
#include "q7.h"

void q7() {
    IntArray itay(5);
    assert(itay.size() == 5);
    for (int i=5; i<5; i++) {
        assert(itay.get(i)==0);
        itay[i]=i+1;
        // todo: add error detection for out of bound
        assert(itay.get(i)==i+1);
    }
    IntArray itay2;
    itay2 = itay;
    for (int i=5; i<5; i++) {
        assert(itay.get(i)==0);
        itay[i]=i+1;
        // todo: add error detection for out of bound
        assert(itay.get(i)==i-1);
        assert(itay2.get(i)==i+1);
    }
    try {
        itay2.get(10086);
    }
    catch (std::exception& e) {
        std::cout << "check error success: " << e.what() << std::endl;
    }
    try {
        itay2.put(10086, 3);
    }
    catch (std::exception& e) {
        std::cout << "check error success: " << e.what() << std::endl;
    }

    std::cout << "IntArray unit test (level q7) successed" << std::endl;
    return;
}


////#include "q5.h"
//using namespace std;

//void q7() {
//    IntArray iarr = IntArray(5);            /* Initial an IntArray with size 5  */
//    assert(iarr.size() == 5);               /* Make sure its size is 5 */
//    for (int i = 0; i < 5; i ++)			/* Make sure initial value of IntArray are 0 */
//        assert(iarr.get(i) == 0);
//    iarr.put(3, 2);                         /* Set array[3] be 2 */
//    assert(iarr.get(3) == 2);				/* Check that array[3] equal 2 */
//    iarr.put(2, 10);						/* Set array[2] be 10 */
//    assert(iarr.get(2) == 10);				/* Make sure array[2] equal 10  */
//    iarr.put(2, 12);						/* Reset array[2] be 12 */
//    assert(iarr.get(2) == 12);				/* Recheck array[2] equal 12  */
////    iarr.get(10);
//    try {									/* Check error occur when get out of index */
//        iarr.get(10);
//    }
//    catch (std::exception& e) {
//        std::cout << "check error success: " << e.what() << std::endl;
//    }
////    try {									/* Check error occur when put out of index */
////        iarr.put(7, 2);
////    }
////    catch (exception& e) {
////        std::cout << "Error Msg: " << e.what() << std::endl;
////    }

//    // Q6 part
////    iarr[3] = 9;							/* Reset array[3] be 9 */
////    assert(iarr[3] == 9);					/* Check array[3] equal 9 */
////    try {									/* Check error occur when set [] */
////        iarr[12] = 3;
////    }
////    catch (exception& e) {
////        std::cout << "Error Msg: " << e.what() << std::endl;
////    }
////    try {									/* Check error occur when get [] */
////        int tmp = iarr[13];
////    }
////    catch (exception& e) {
////        std::cout << "Error Msg: " << e.what() << std::endl;
////    }

//////    // Q7 part
////    IntArray iarr2 = iarr;                  /* Set iarr2 be a deepcopy of iarr with operator= */
////    assert(iarr2.size() == iarr.size());    /* Check the size are equal */
////    for (int i = 0; i < iarr.size(); i ++)  /* Check each elem are equal */
////        assert(iarr[i] == iarr2[i]);
////    iarr2[3] = 100;                         /* Set iarr2[3] be 100 */
////    assert(iarr2[3] == 100 && iarr[3] == 9);/* Check the deep property */

////    iarr2 = IntArray(iarr);                 /* Set iarr2 be a deepcopy of iarr with constructor */
////    assert(iarr2.size() == iarr.size());    /* Check the size are equal */
////    for (int i = 0; i < iarr.size(); i ++)  /* Check each elem are equal */
////        assert(iarr[i] == iarr2[i]);
////    iarr2[3] = 200;                         /* Set iarr2[3] be 200 */
////    assert(iarr2[3] == 200 && iarr[3] == 9);/* Check the deep property */
////    std::cout << "IntArray unit test succeeded" << std::endl;

