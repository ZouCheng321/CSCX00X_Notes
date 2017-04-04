#include <iostream>
#include "vector.h"

int findMajorityElement(Vector<int> &vec) {
    int cand_count = 0;
    int candidate = -1;
    const auto half = vec.size()/2;

    for (auto &element: vec) {
        if (element==candidate) cand_count++;
        else {
            if (--cand_count<=0){
                candidate=element;
                cand_count=1;
            }
        }
    }

    cand_count=0;
    for (auto &element: vec) {
        if (element==candidate) cand_count++;
    }

    return cand_count>half? candidate: -1;
}
