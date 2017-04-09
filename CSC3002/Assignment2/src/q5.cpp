#include <iostream>
#include <cassert>
#include "intarray.h"

void q5() {
    IntArray itay(5);
    assert(itay.size() == 5);
//    assert(itay.isEmpty());
    for (int i=5; i<5; i++) {
        assert(itay.get(i)==0);
        itay.put(i, i+1);
        // todo: add error detection for out of bound
        assert(itay.get(i)==i+1);
    }
    std::cout << "IntArray unit test (level q5) successed" << std::endl;
    return;
}
