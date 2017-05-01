#ifndef _pqueue_heap_h
#define _pqueue_heap_h

#include <vector>
#include "error.h"

namespace q3{
inline unsigned int parentIndex(const unsigned int n) {return (n - 1) / 2;}
inline unsigned int leftChildIndex(const unsigned int n) {return 2 * n + 1;}
inline unsigned int rightChildIndex(const unsigned int n) {return 2 * n + 2;}

template <typename ValueType>
class Queue {
public:
   Queue();
   ~Queue();

   int size() const;

   bool isEmpty() const;

   void clear();

   void enqueue(ValueType Value, double priority);

   ValueType dequeue();

   ValueType peek() const;

   Queue(const Queue<ValueType> & src);
   Queue<ValueType> & operator=(const Queue<ValueType> & src);
   void deepCopy(const Queue<ValueType> & src);

private:
   struct Item{
       ValueType value;
       double priority = 0;
       unsigned int order = 0;
       const inline bool operator <(const Item& rhs) const {
           return priority !=rhs.priority? priority<rhs.priority: order<rhs.order;
       }
   };
   std::vector<Item *> heap;

   unsigned int order = 0;
};

template <typename ValueType>
Queue<ValueType>::Queue() {
//    heap = new std::vector<Item>;
}

template <typename ValueType>
Queue<ValueType>::~Queue() {
     clear();
}


template <typename ValueType>
int Queue<ValueType>::size() const {
   return heap.size();
}



template <typename ValueType>
bool Queue<ValueType>::isEmpty() const {
   return heap.size()== 0;
}


template <typename ValueType>
void Queue<ValueType>::clear() {

    for(auto const& item :heap) {
        delete item;
    }
    order = 0;
    heap.clear();
}

template <typename ValueType>
void Queue<ValueType>::enqueue(ValueType value, double priority) {
    Item * tempItem = new Item;
    tempItem->order = order++;
    tempItem->priority = priority;
    tempItem->value = value;
    heap.push_back(tempItem);
    std::cout << heap.size() << std::endl;
    unsigned int n = heap.size()-1;
    std::cout << n << std::endl;
    while (n!=0 && *heap[n]<*heap[parentIndex(n)]) {
        std::cout << "true" << heap[n]->order << "|" << heap[parentIndex(n)]->order << std::endl;
        tempItem = heap[n];
        heap[n] = heap[parentIndex(n)];
        heap[parentIndex(n)] = tempItem;
        n = parentIndex(n);
    }

}

template <typename ValueType>
ValueType Queue<ValueType>::dequeue() {
   if (isEmpty()) error("dequeue: Attempting to dequeue an empty queue");
   ValueType result = heap[0]->value;

   heap[0] = heap.back();
   heap.pop_back();
   unsigned int n = 0;
   Item * tempItem = heap[0];
   while((leftChildIndex(n)<heap.size() && *heap[leftChildIndex(n)] < *heap[n]) ||
         (rightChildIndex(n)<heap.size() && *heap[rightChildIndex(n)] < *heap[n])) {
       if ((leftChildIndex(n)<heap.size() && *heap[leftChildIndex(n)] < *heap[n])) {
           tempItem = heap[n];
           heap[n] = heap[leftChildIndex(n)];
           heap[leftChildIndex(n)] = tempItem;
           n = leftChildIndex(n);
       } else {
           tempItem = heap[n];
           heap[n] = heap[rightChildIndex(n)];
           heap[rightChildIndex(n)] = tempItem;
           n = rightChildIndex(n);
       }
   }
   return result;
}

template <typename ValueType>
ValueType Queue<ValueType>::peek() const {
   if (isEmpty()) error("peek: Attempting to peek at an empty queue");
   return heap[0]->value;
}


template <typename ValueType>
Queue<ValueType>::Queue(const Queue<ValueType> & src) {
   deepCopy(src);
}

template <typename ValueType>
Queue<ValueType> & Queue<ValueType>::operator=(const Queue<ValueType> & src) {
   if (this != &src) {
      deepCopy(src);
   }
   return *this;
}

template <typename ValueType>
void Queue<ValueType>::deepCopy(const Queue<ValueType> & src) {

    for (int i=0; i<src.size(); i++) {
        Item * tempItem = new Item;
        tempItem->order = src.heap[i]->order;
        tempItem->priority = src.heap[i]->priority;
        tempItem->value = src.heap[i]->value;
        heap.push_back(tempItem);
    }
    order = src.order;
}

}

#endif
