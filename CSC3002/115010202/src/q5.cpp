#include <iostream>
#include <cassert>
#include "intarray.h"

void q5() {
    IntArray itay(5);
    assert(itay.size() == 5);
    std::cout << "array init successful" << std::endl;
//    assert(itay.isEmpty());
    for (int i=5; i<5; i++) {
        assert(itay.get(i)==0);
        itay.put(i, i+1);
        // todo: add error detection for out of bound
        assert(itay.get(i)==i+1);
    }
    std::cout << "array read/wirte successful" << std::endl;
    try {
        itay.get(10086);
    }
    catch (std::exception& e) {
        std::cout << "error test successful: " << e.what() << std::endl;
    }
    try {
        itay.put(10086, 3);
    }
    catch (std::exception& e) {
        std::cout << "error test successful: " << e.what() << std::endl;
    }
    std::cout << "IntArray unit test (level q5) successed" << std::endl;
    return;
}
