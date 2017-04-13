#include "intarray.h"
#include "error.h"

class cscerror: public std::exception
{
  virtual const char* what() const throw()
  {
    return "csc3002 - Size error";
  }
} sizeOver;

IntArray::IntArray() {
//    IntArray(INITIAL_CAPACITY);
    capacity = INITIAL_CAPACITY;
    array = new int[INITIAL_CAPACITY]{0};
}

IntArray::IntArray(int n) {
    capacity = n;
    array = new int[n]{0};

}

IntArray::~IntArray() {
    delete[] array;
}

int IntArray::size() const {
    return capacity;
}

int IntArray::get(int i) {
    if (i>=size()) throw sizeOver;
    return array[i];
}

void IntArray::put(int k, int value) {
    if (k>=size()) throw sizeOver;
    array[k] = value;
}

//bool IntArray::isEmpty() const {
//    ;
//}

void IntArray::deepCopy(const IntArray & src) {
    int n = src.size();
    array = new int[n]{0};
    for (int i=0; i<n; i++) {
        array[i] = src.array[i];
    }
}

IntArray & IntArray::operator=(const IntArray & src) {
    if (this != &src) {
        delete[] array;
        deepCopy(src);
    }
    return *this;
}

int& IntArray::operator[] (int i) {
          return array[i];
      }



