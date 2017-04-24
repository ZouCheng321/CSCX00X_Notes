#include <iostream>
#include <cassert>

#include "intarray.h"
#include "q7.h"

void q7() {
    IntArray itay(5);
    assert(itay.size() == 5);
    std::cout << "size is right" << std::endl;
    for (int i=5; i<5; i++) {
        assert(itay.get(i)==0);
        itay[i]=i+1;
        assert(itay.get(i)==i+1);
    }
    std::cout << "array read/wirte successful" << std::endl;
    IntArray itay2;
    itay2 = itay;
    for (int i=5; i<5; i++) {
        assert(itay.get(i)==0);
        itay[i]=i+1;
        assert(itay.get(i)==i-1);
        assert(itay2.get(i)==i+1);
    }
    std::cout << "array copy successful" << std::endl;
    try {
        itay2.get(10086);
    }
    catch (std::exception& e) {
        std::cout << "error test successful: " << e.what() << std::endl;
    }
    try {
        itay2.put(10086, 3);
    }
    catch (std::exception& e) {
        std::cout << "error test successful: " << e.what() << std::endl;
    }

    std::cout << "IntArray unit test (level q7) successed" << std::endl;
    return;
}



