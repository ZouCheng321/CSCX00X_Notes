#include <iostream>
#include "editorBuffer.h"



EditorBuffer::EditorBuffer() {
    start = cursor = new Cell;
    end = new Cell;
    start->prev = NULL;
    start->next = end;
    end->prev = start;
    end->next = NULL;

}

EditorBuffer::~EditorBuffer() {
    Cell *cp = start;
    while (cp != NULL) {
        Cell *next = cp->next;
        delete cp;
        cp = next;
    }
}

void EditorBuffer::moveCursorForward() {
    if (cursor->next->next != NULL) {
        cursor = cursor->next;
    }
}

void EditorBuffer::moveCursorBackward() {
//    Cell *cp = start;
//    if (cursor != start) {
//        while (cp->next != cursor) {
//            cp = cp->next;
//        }
//        cursor = cp;
//    }
    if (cursor->prev != NULL) {
        cursor = cursor->prev;
    }
}

void EditorBuffer::moveCursorToStart() {
    cursor = start;
}

void EditorBuffer::moveCursorToEnd() {
//    while (cursor->next != NULL) {
//        cursor = cursor->next;
//    }
    cursor = end->prev;
}

void EditorBuffer::insertCharacter(char ch) {
    Cell *cp = new Cell;
    cp->ch = ch;

    cp->next = cursor->next;
    cp->next->prev = cp;

    cp->prev = cursor;
    cursor->next = cp;

    cursor = cp;
}

void EditorBuffer::deleteCharacter() {
    if (cursor->next->next != NULL) {
        Cell *oldCell = cursor->next;
        cursor->next = cursor->next->next;
        cursor->next->prev = cursor;
        delete oldCell;
    }
}

std::string EditorBuffer::getText() const {
    std::string str = "";
    for (Cell *cp = start->next; cp->next != NULL; cp = cp->next) {
        str += cp->ch;
    }
    return str;
}

int EditorBuffer::getCursor() const {
    int nChars = 0;
    for (Cell *cp = start; cp != cursor; cp = cp->next){
        nChars++;
    }
    return nChars;
}
