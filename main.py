# importing everything from tkinter
from tkinter import *


# Creating Frame for Calculator
def calculator_frame(source, side):
    store_obj = Frame(source, borderwidth=4, bd=4, bg="orange")
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


# Creating Button
def button(source, side, text, command=None):
    store_obj = Button(source, text=text, command=command)
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 16 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Basic Calculator')

        # Adding Display Widget
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
              justify='right'
              , bd=30, bg="orange").pack(side=TOP,
                                         expand=YES, fill=BOTH)

        # Adding Clear Button Widget
        for clearButton in (["C"]):
            erase = calculator_frame(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))

        # Adding Numbers And Symbols Widget
        for numButton in ("789+", "456-", "123*", "0.%/"):
            function_num = calculator_frame(self, TOP)
            for iEquals in numButton:
                button(function_num, LEFT, iEquals, lambda
                    storeObj=display, q=iEquals: storeObj
                       .set(storeObj.get() + q))

        # Adding Equal Button
        equal_button = calculator_frame(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btni_equals = button(equal_button, LEFT, iEquals)
                btni_equals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                             storeObj=display: s.calc(storeObj), '+')
            else:
                btni_equals = button(equal_button, LEFT, iEquals,
                                     lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                     (storeObj.get() + s))

    # Applying Event Trigger On Widgets
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


# Start the GUI Calculator
if __name__ == '__main__':
    app().mainloop()
