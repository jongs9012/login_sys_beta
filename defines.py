import json
from os import listdir
from datetime import datetime

def read_data(id_):
    with open(f"./users/{id_}_info.json", "r") as json_file:
        json_data = json.load(json_file)
    return json_data


def checking_account(id_, pwd):
    try:
        with open(f"./users/{id_}_info.json", "r") as json_file:
            json_data = json.load(json_file)
            if json_data["id"] == id_ and json_data["pwd"] == pwd:
                if json_data["surveyed"] == "False":
                    return True, False
                else:
                    return True, True
            else:
                return False, False
    except FileNotFoundError:
        return False, False


def find_values(index):
    info_list = []
    value_list = []

    for filename in listdir("./users"):
        info_list.append(read_data(filename[0:-9]))

    for i, value in enumerate(info_list):
        # If after surveyed user
        if value[4][1] == "True":
            value_list.append(value[index][1])
        else:
            pass
    return value_list


def find_average(index):
    info_list = []
    value_list = []
    count = {}

    for filename in listdir("./users"):
        info_list.append(read_data(filename[0:-9]))
    for i, value in enumerate(info_list):
        # If after surveyed user
        if value[4][1] == "True":
            value_list.append(value[index][1])
    for j in value_list:
        try:
            count[j] += 1
        except:
            count[j] = 1
    return count


def compare_days(user_id):
    format_ = '%Y-%m-%d %H:%M'
    user_date = read_data(user_id)[3][1]

    date = datetime.strptime(user_date, format_)
    now = datetime.now()
    date_diff = now - date
    return date_diff.days, int(date_diff.seconds / 3600)


def get_curr_time():
    return datetime.now()


