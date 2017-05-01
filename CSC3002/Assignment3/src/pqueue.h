#ifndef _pqueue_h
#define _pqueue_h

#include <vector>
#include "error.h"

namespace q2 {
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
       double priority;
       Item *next = NULL;
   };

   Item * start = NULL;
   Item * end = NULL;
   unsigned int sizeItem = 0;
};

template <typename ValueType>
Queue<ValueType>::Queue() {
    start = nullptr;
    end = nullptr;
    sizeItem = 0;
}

template <typename ValueType>
Queue<ValueType>::~Queue() {
     clear();
}


template <typename ValueType>
int Queue<ValueType>::size() const {

   return sizeItem;
}



template <typename ValueType>
bool Queue<ValueType>::isEmpty() const {
   return sizeItem == 0;
}


template <typename ValueType>
void Queue<ValueType>::clear() {
    Item * curItem = start;
    while (start != nullptr) {
        curItem = start;
        start = start->next;
        delete curItem;
    }
    sizeItem = 0;
    start = NULL;
    end = NULL;

}

template <typename ValueType>
void Queue<ValueType>::enqueue(ValueType value, double priority) {
    if (end!=nullptr) {
        Item * temp;
        temp = start;
        if (priority < start->priority) {
            Item * newItem = new Item;
            newItem->next = start;
            newItem->priority = priority;
            newItem->value = value;
            start = newItem;
        } else {
            while (temp->next != NULL && priority >= temp->next->priority) {
                temp = temp->next;
            }
            Item * newItem = new Item;
            newItem->next = temp->next;
            newItem->priority = priority;
            newItem->value = value;
            temp->next = newItem;
        }
    } else {
        end = start = new Item;
        start->value = value;
        start->priority = priority;

    }
    sizeItem ++;
}

template <typename ValueType>
ValueType Queue<ValueType>::dequeue() {
   if (isEmpty()) error("dequeue: Attempting to dequeue an empty queue");
   ValueType result = start->value;
   Item * temp = NULL;
   temp = start;
   start = start->next;
   if (start == NULL) end = NULL;
   delete temp;
   sizeItem --;
   return result;
}

template <typename ValueType>
ValueType Queue<ValueType>::peek() const {
   if (isEmpty()) error("peek: Attempting to peek at an empty queue");
   return start->value;
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
    start = NULL;
    end = NULL;
    sizeItem = 0;
    for (Item *cp = src.start; cp != NULL; cp = cp->next) {
       enqueue(cp->value, cp->priority);
    }
}
}
#endif
