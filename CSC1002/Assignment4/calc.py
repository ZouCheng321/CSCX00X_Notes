#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CSC1002 Assignment 4
By Mao Licheng
ID 115010202
"""

from math import *
from tkinter import *


class DisplayModule(object):
    """
    This class works as a display control. It will update the screen and store the expression.
    """
    def __init__(self, screen0, screen1):
        self.__sc0 = screen0
        self.__sc1 = screen1
        self.__current_expression = ''
        self.__current_result = ''
        self.__previous_expression = ''
        self.__fast_access = False
        self.__sc0_display()
        self.__sc1_display()

    def exp_rewrite(self, str0):
        """
        By this method, the current expression can be modified directly by argument str0.
        """
        self.__fast_access = False
        self.__current_expression = str0
        self.__sc0_display()

    def pop_string(self):
        """
        Delete the last character.
        """
        self.__fast_access = False
        self.__current_expression = self.__current_expression[:-1]
        self.__sc0_display()

    def add_string(self, str0):
        """
        Add an input at the end of the expression
        """
        self.__fast_access = False
        self.__current_expression += str0
        self.__sc0_display()

    def __sc0_display(self):
        """
        Update the screen0
        """
        self.__sc0.configure(text=self.__current_expression)

    def __sc1_display(self):
        """
        Update the screen1
        """
        self.__sc1.configure(text=self.__current_result)

    def fast(self):
        """
        In some condition, some operator can get the result as a argument immediately.
        For example, you can press '+' if a previous result is already got as '7', it will display as '7+'
        Whether this functionality is available can be checked by this method.
        (Only available after a calculation.)
        """
        return self.__fast_access

    def get_result(self):
        return self.__current_result

    def get_previous(self):
        return self.__previous_expression

    def solve(self):
        """
        Solve the expression.
        Display 'Expression error!' if error raised.
        """
        try:
            self.__current_result = eval(self.__current_expression)
            self.__sc1_display()
            self.__previous_expression = self.__current_expression
            self.__current_expression = ''

            self.__fast_access = True
        except Exception as error:
            self.__current_result = error
            self.__current_result = 'Expression error!'
            self.__sc1_display()
            self.__fast_access = False

    def clear(self):
        """
        Clear the screen.
        """
        self.__init__(self.__sc0, self.__sc1)


def main():
    calculator = Tk()
    calculator.geometry('257x250+100+100')
    calculator.title('Calculator')
    calculator.resizable(width=FALSE, height=FALSE)
    glass_panel = Frame(calculator)
    glass_panel.pack(fill=X)
    screen0 = Label(glass_panel, text="I'm a screen 1", justify=CENTER, bg='green', fg='yellow', height=3)
    screen1 = Label(glass_panel, text="I'm a screen 2", justify=CENTER, bg='yellow', fg='green', height=3)
    screen0.pack(fill=X)
    screen1.pack(fill=X)
    screen_module = DisplayModule(screen0, screen1)
    button_panel = Frame(calculator)
    button_panel.pack(fill=X)
    # Button data
    buttons_text = (
        ('7', '8', '9', '+', 'Clear'),
        ('4', '5', '6', '-', '('),
        ('1', '2', '3', '*', ')'),
        ('0', '.', '<=', '/', '='),
        ('tan', 'cos', 'sin', 'sqrt', '1/x'),
    )
    button_command = dict()
    # generate button event function and button geometry.
    for i, button_row in enumerate(buttons_text):
        for j, button_text in enumerate(button_row):
            # event generator
            def button_func_generator(text0):
                if text0 in '0123456789.()':
                    # Static button
                    def button_click():
                        screen_module.add_string(text0)
                elif text0 in '+-*/':
                    # Static buttoned operator with fast capture
                    def button_click():
                        if screen_module.fast():
                            screen_module.exp_rewrite(str(screen_module.get_result()) + text0)
                        else:
                            screen_module.add_string(text0)
                elif text0 in ('sin', 'cos', 'tan', 'sqrt',):
                    # Static buttoned function with fast capture
                    def button_click():
                        if screen_module.fast():
                            screen_module.exp_rewrite(text0 + '(' + str(screen_module.get_result()) + ')')
                            screen_module.solve()
                        else:
                            screen_module.add_string(text0 + '(')
                elif text0 in ('1/x',):
                    # Dynamic buttoned function with fast capture
                    def button_click():
                        if screen_module.fast():
                            screen_module.exp_rewrite('1/' + str(screen_module.get_result()))
                            screen_module.solve()
                elif text0 == '<=':
                    # Special button
                    def button_click():
                        screen_module.pop_string()
                elif text0 == '=':
                    # Special button
                    def button_click():
                        if screen_module.fast():
                            screen_module.exp_rewrite(screen_module.get_previous())
                        screen_module.solve()
                elif text0 == 'Clear':
                    # Special button
                    def button_click():
                        screen_module.clear()
                else:
                    # Unknown button
                    def button_click():
                        screen_module.add_string('UNDEF')
                return button_click
            # Initialize the button.
            button_command[button_text] = button_func_generator(button_text)
            Button(button_panel, text=button_text,
                   command=button_command[button_text]).grid(row=i, column=j, sticky='NESW')
    calculator.mainloop()

if __name__ == '__main__':
    main()
