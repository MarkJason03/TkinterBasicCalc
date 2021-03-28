"""
Calculator
Author: Mark Galicia
"""

from tkinter import *
from datetime import datetime


def main():
    root = Tk()
    shopping_app = Calculator(root)
    root.mainloop()


class Calculator:
    no_font = ("monaco", 50, "bold")
    date_font = ("monaco", 20, "bold")
    button_font = ("monaco", 20, "bold")

    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("500x550")
        self.master.configure(background="black")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.calculate_frame = Frame()
        self.calculate_frame.pack(side="top", pady=10)

        self.operator = ""  # This empty string takes  all of my input and evaluate them ex str(eval(" 5 + 5 + 5"))
        self.calculate_var = StringVar()
        date = datetime.now()
        format_date = f"{date:%a, %b %d %Y}"  # %a(day), %b(Month), %d(numeric date) , %Y (year)

        self.time = Label(self.calculate_frame, text=format_date, font=self.date_font).pack(side="top")
        self.calculator_entry_box = Entry(self.calculate_frame, state="disabled", width=10, bd=5,
                                          textvariable=self.calculate_var,
                                          font=self.no_font, justify="right")
        self.calculator_entry_box.pack(side="top")

        self.calculator_button_frame = Frame()
        self.calculator_button_frame.pack(side="top", pady=10)

        self.no_9_btn = Button(self.calculator_button_frame, text="9", font=self.button_font, width=6, height=2,
                               command=lambda: self.input_no(9)).grid(row=0, column=0)

        self.no_8_btn = Button(self.calculator_button_frame, text="8", font=self.button_font, width=6, height=2,
                               command=lambda: self.input_no(8)).grid(row=0, column=1)

        self.no_7_btn = Button(self.calculator_button_frame, text="7", width=6, height=2,
                               font=self.button_font, command=lambda: self.input_no(7)).grid(row=0, column=2, padx=2,
                                                                                             pady=2)

        self.no_6_btn = Button(self.calculator_button_frame, text="6", font=self.button_font, width=6, height=2,
                               command=lambda: self.input_no(6)).grid(row=1, column=0)

        self.no_5_btn = Button(self.calculator_button_frame, text="5", font=self.button_font, width=6, height=2,
                               command=lambda: self.input_no(5)).grid(row=1, column=1)

        self.no_4_btn = Button(self.calculator_button_frame, text="4", width=6, height=2,
                               font=self.button_font, command=lambda: self.input_no(4)).grid(row=1, column=2, padx=2,
                                                                                             pady=2)

        self.no_3_btn = Button(self.calculator_button_frame, text="3", width=6, height=2, font=self.button_font,
                               command=lambda: self.input_no(3)).grid(row=2, column=0)

        self.no_2_btn = Button(self.calculator_button_frame, text="2", width=6, height=2, font=self.button_font,
                               command=lambda: self.input_no(2)).grid(row=2, column=1)

        self.no_1_btn = Button(self.calculator_button_frame, text="1", width=6, height=2,
                               font=self.button_font, command=lambda: self.input_no(1)).grid(row=2, column=2, padx=2,
                                                                                             pady=2)

        self.no_0_btn = Button(self.calculator_button_frame, text="0", width=6, height=2,
                               font=self.button_font, command=lambda: self.input_no(0)).grid(row=3, column=0, padx=2,
                                                                                             pady=2)

        self.clear_btn = Button(self.calculator_button_frame, text="C", width=6, height=2,
                                font=self.button_font, command=self.clear).grid(row=3, column=1)

        self.equal_btn = Button(self.calculator_button_frame, text="=", width=6, height=2, font=self.button_font,
                                command=self.calculation).grid(row=3, column=2)

        self.add_btn = Button(self.calculator_button_frame, text="+", width=6, height=2, font=self.button_font,
                              command=lambda: self.input_no("+")).grid(row=2, column=3)

        self.sub_btn = Button(self.calculator_button_frame, text="-", width=6, height=2, font=self.button_font,
                              command=lambda: self.input_no("-")).grid(row=1, column=3)

        self.multi_btn = Button(self.calculator_button_frame, text="*", width=6, height=2, font=self.button_font,
                                command=lambda: self.input_no("*")).grid(row=0, column=3)

        self.div_btn = Button(self.calculator_button_frame, text="÷", width=6, height=2, font=self.button_font,
                              command=lambda: self.input_no
                              ("/")).grid(row=3, column=3)

    def input_no(self, no): # number container using lambda exp
        self.number = no
        self.operator = self.operator + str(no)  # Empty string  is concatinated with the input
        self.calculate_var.set(self.operator)

    def calculation(self):
        total = str(eval(self.operator))  # calculate whatever input is gathered by the empty string
        self.calculate_var.set(total)

    def clear(self):
        self.operator = ""
        self.calculate_var.set("")


if __name__ == '__main__':
    main()


