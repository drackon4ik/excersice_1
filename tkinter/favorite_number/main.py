# from tkinter import *
#
# import json_use
#
#
# def correct_data(data):
#     if "a" in list(data.keys())[0] and int((list(data.values())[0])) % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def not_in_data(data, file_data):
#     if list(data.keys())[0] in file_data:
#         return True
#     else:
#         return False
#
#
# def main(data):
#     file_data = json_use.load_data(file="favorite_numbers.json")
#     b = correct_data(data)
#     c = not_in_data(data, file_data)
#     if not c and b:
#         try:
#             file_data.update(data)
#             with open("json_alphabet", "w") as file:
#                 json_use.dump_data(file_data, file="favorite_numbers.json")
#         except:
#             print("Smth goes wrong!")
#
#         print("Data successfuly dumped!")
#     else:
#         print("Incorrect data")
#
#
# root = Tk()
# root.title("user_info")
# root.geometry("300x300")
#
# name_e = Entry(root, width=11)
# name_e.place(x=90, y=50)
#
# number_e = Entry(root, width=11)
# number_e.place(x=90, y=90)
#
# instructions_l = Label(root, text="put name, number")
# instructions_l.place(x=65, y=0)
#
# name_l = Label(root, text="name->")
# name_l.place(x=40, y=48)
#
# number_l = Label(root, text="number->")
# number_l.place(x=31, y=88)
#
# submit_b = Button(root, text="submit", width=10, command=lambda: main({name_e.get(): number_e.get()}))
# submit_b.place(x=100, y=130)
#
# root.mainloop()