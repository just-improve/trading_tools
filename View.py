import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '_', '='
    ]

    def __init__(self, controller):
        super().__init__()

        self.title('Get Spread')
        self.controller = controller

        self.value_var_entry = tk.StringVar()

        self.btn_rb = tk.IntVar()
        self.btn_rb.set(1)

        self.var_check_box = tk.IntVar()
        self.var_check_box.set(1)
        self._make_main_frame()
        self._make_labels()
        self._make_entry()
        self._make_checkboxes()
        self._radio_buttons()
        self._make_button()


    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):  # single underscore is private method
        self.ent = ttk.Entry(self.main_frm, justify='right', textvariable=self.value_var_entry, state='enable')
        self.ent.insert(0,"5")
        self.ent.pack(fill='x')

    def _make_labels(self):  # single underscore is private method
        self.lab = ttk.Label(self.main_frm, justify='right', text="1nd spread", state='enable')
        self.lab.pack(fill='x')

    def _make_checkboxes(self):
        c1 = tk.Checkbutton(self.main_frm, text='From highest spread', variable=self.var_check_box, onvalue=1, offvalue=0)
        c1.pack()

    def _radio_buttons(self):

        r1 = ttk.Radiobutton(self.main_frm, text='All coins', value='1', variable=self.btn_rb)
        r1.pack()

        r2 = ttk.Radiobutton(self.main_frm, text='Only Perp', value='2', variable=self.btn_rb)
        r2.pack()
        #r3 = ttk.Radiobutton(self.main_frm, text='Not Perp', value='3', variable=self.btn_rb)
        #r3.pack()

    def _make_button(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
        btn = ttk.Button(outer_frm, text="Get Spread", command=self.controller.get_spread)
        btn.pack(side='left', pady=10,padx=10)

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)
        frm.pack()
        buttons_in_row = 0

        for caption in self.button_captions:
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack()
                buttons_in_row = 0

            btn = ttk.Button(frm, text=caption, command=(lambda button=caption: self.controller.on_button_click(button)))
            btn.pack(side='left')
            buttons_in_row += 1
