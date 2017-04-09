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
    std::cout << "IntArray unit test (level q7) successed" << std::endl;
    return;
}
