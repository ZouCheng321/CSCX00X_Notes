#include <iostream>
#include <cassert>
#include "intarray.h"
#include "q6.h"

void q6() {
    IntArray itay(5);
    assert(itay.size() == 5);
    for (int i=5; i<5; i++) {
        assert(itay.get(i)==0);
        itay[i]=i+1;
        // todo: add error detection for out of bound
        assert(itay.get(i)==i+1);
    }
    std::cout << "IntArray unit test (level q6) successed" << std::endl;
    return;
}
