
#ifndef _intarray_h
#define _intarray_h

#include <exception>

class IntArray {
public:

    IntArray();
    IntArray(int n);
    ~IntArray();
    int size() const;
    int get(int i);
    void put(int k, int value);
//    bool isEmpty() const;
//    void clear();
    IntArray & operator=(const IntArray & src);
    int & operator[] (int i);

private:
    static const int INITIAL_CAPACITY = 10;
    int capacity;
    int *array;
    void deepCopy(const IntArray & src);
};

#endif

