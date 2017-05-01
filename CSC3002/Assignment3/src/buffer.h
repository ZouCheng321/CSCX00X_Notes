#ifndef _buffer_h
#define _buffer_h

#include <string>

class EditorBuffer {
public:
	EditorBuffer();
	~EditorBuffer();
	void moveCursorForward();
	void moveCursorBackward();
	void moveCursorToStart();
	void moveCursorToEnd();
    void insertCharacter(char ch);
	void deleteCharacter();
	std::string getText() const;
    int getCursor() const;
private:
    struct Cell {
        char ch;
        Cell *link;
        Cell *prev;
        Cell *next;
    };

    Cell *start;
    Cell *end;
    Cell *cursor;

    EditorBuffer(const EditorBuffer & value) {}
    const EditorBuffer & operator=(const EditorBuffer & rhs) { return *this;}
};

#endif
