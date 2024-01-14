from tkinter import *


def arrow_left():
    right_exchange = right_currency_E.get()
    currency_text = right_currency_l.cget('text')
    currency_num = currency_text.split("-")[1].split()[0]
    if right_exchange.isaplha() and len(right_exchange == 0):
        return

    result = int(right_exchange) * int(currency_num)
    left_currency_E.delete(0, END)
    left_currency_E.insert(0, result)
    print(result)


def arrow_right():
    left_exchange = left_currency_E.get()
    currency_text_2 = left_currency_2_l.cget('text')
    currency_num_2 = currency_text_2.split("-")[1].split()[0]

    answer = int(left_exchange) * float(currency_num_2)
    right_currency_E.delete(0, END)
    right_currency_E.insert(0, answer)
    print(answer)


root = Tk()
root.title("exchange")
root.geometry("500x250")

left_currency_l = Label(text="currency: UAH")
left_currency_l.place(x=50, y=40)

left_currency_2_l = Label(text="Exchange: 1UAH - 0.032 EUR")
left_currency_2_l.place(x=10, y=60)

left_currency_E = Entry(root, width=25, bd=2)
left_currency_E.place(x=10, y=80)

right_currency_l = Label(text="Exchange: 1 EUR - 32 UAH")
right_currency_l.place(x=340, y=60)

right_currency_2_l = Label(text="currency: EUR")
right_currency_2_l.place(x=370, y=40)

right_currency_E = Entry(root, width=25, bd=2)
right_currency_E.place(x=340, y=80)

clean_b = Button(root, text="Clean", width=10, height=1)
clean_b.place(x=70, y=150)

exchange_b = Button(root, text="Change", width=10, height=1)
exchange_b.place(x=360, y=150)

left_photo = PhotoImage(file="arrow_left.png")
left_photo = left_photo.subsample(10, 10)

right_photo = PhotoImage(file="arrow_right.png")
right_photo = right_photo.subsample(10, 10)

from_exchange_b = Button(root, image=left_photo, height=40, width=60, command=arrow_left).place(x=210, y=40)
from_currency_b = Button(root, image=right_photo, height=40, width=60, command=arrow_right).place(x=210, y=100)

root.mainloop()
