from tkinter import *
from tkinter.ttk import *
from time import sleep
import locale
import os


class Main:
    def __init__(self):
        self.window = Tk(screenName='Mortgage Calculator', baseName='Mortgage Calculator')
        self.master = self.window.master
        self.window.title('Mortgage Calc')
        self.window.geometry('260x130')
        self.window.resizable(False, False)
        self.window.protocol('WM_DELETE_WINDOW', self.exit_handler)

        if os.path.isfile(os.getcwd() + '/icon.ico'):
            self.window.iconbitmap(os.getcwd() + '/icon.ico')

        self.edge_pad = 4
        self.closed = False
        self.window.mainloop = self.mainloop
        locale.setlocale(locale.LC_MONETARY, '')

        self.p = 0
        self.r = 0
        self.n = 0

        self.label_principal = Label(self.master, text='Principal:')
        self.label_principal.place(x=self.edge_pad, y=self.edge_pad)
        self.label_principal.update()

        self.label_interest = Label(self.master, text='Interest Rate (Annual):')
        self.label_interest.place(x=self.edge_pad, y=self.edge_pad + 30)
        self.label_interest.update()

        self.label_period = Label(self.master, text='Period (Years):')
        self.label_period.place(x=self.edge_pad, y=self.edge_pad + 60)
        self.label_period.update()

        self.label_payment = Label(self.master, text='Monthly Payment:')
        self.label_payment.place(x=self.edge_pad, y=self.edge_pad + 90)
        self.label_payment.update()

        self.entry_principal = Entry(self.master)
        self.entry_principal.place(x=self.label_interest.winfo_width() + 3 + self.edge_pad, y=self.edge_pad)

        self.entry_interest = Entry(self.master)
        self.entry_interest.place(x=self.label_interest.winfo_width() + 3 + self.edge_pad,
                                  y=self.label_interest.winfo_y())

        self.entry_period = Entry(self.master)
        self.entry_period.place(x=self.label_interest.winfo_width() + 3 + self.edge_pad,
                                y=self.label_period.winfo_y())

        self.entry_payment = Entry(self.master, state=DISABLED)
        self.entry_payment.place(x=self.label_interest.winfo_width() + 3 + self.edge_pad,
                                 y=self.label_payment.winfo_y())

    def exit_handler(self):
        self.closed = True

    def mainloop(self):
        while not self.closed:
            try:
                percent = 100
                months_in_year = 12

                p = float(self.entry_principal.get())
                r = float(self.entry_interest.get()) / percent / months_in_year
                n = float(self.entry_period.get()) * months_in_year

                if p != self.p or r != self.r or n != self.n:
                    m = p * ((r * ((1 + r) ** n)) / (((1 + r) ** n) - 1))

                    self.entry_payment.config(state=NORMAL)
                    self.entry_payment.delete(0, len(self.entry_payment.get()))
                    self.entry_payment.insert(1, str(locale.currency(m, grouping=True)))
                    self.entry_payment.config(state=DISABLED)

                    self.p, self.r, self.n = p, r, n
            except:
                pass

            try:
                self.window.update_idletasks()
                self.window.update()
            except:
                pass

            sleep(0.01)


def main():
    Main().window.mainloop()


if __name__ == '__main__':
    main()
