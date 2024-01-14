import json


def dump_data(data, file):
    try:
        with open(file, "w") as file:
            json.dump(data, file)
    except:
        print("Smth goes wrong!")



def load_data(file):
    try:
        with open(file, "r") as file:
            file_data = json.load(file)
    except:
        print("Smth goes wrong")

    return file_data
!

