'''with open(f"./users/{id_}_info.txt", "w") as user_file:
    user_file.write(f"NAME:{name}\n")
    user_file.write(f"ID:{id_}\n")
    user_file.write(f"PWD:{password}\n")
    user_file.write(f"SIGN_UP_TIME:{time[0:16]}\n")
    user_file.write(f"Surveyed:False")



new_content = ""
            with open(f"./users/{id_}_info.txt", "r") as file:
                lines = file.readlines()
                for i, l in enumerate(lines):
                    if list(l.split(":"))[0] == "Surveyed":
                        new_string = "Surveyed:True\n"
                    elif list(l.split(":"))[0] != "Surveyed":
                        new_string = l
                    if new_string:
                        new_content += new_string
                new_content += f"SleepTime:{night_or_day}\n" \
                               f"SleepHours:{sleep_hours}\n" \
                               f"WhySleep:{reason}\n" \
                               f"SleepingAtOnce:{once_or_not}\n" \
                               f"DreamingTimes:{dreaming_times}\n" \
                               f"GradeOfSleep:{quality_dream}\n" \
                               f"LightState:{light_state}"
            # Update the survey
            with open(f"./users/{id_}_info.txt", "w") as f:
                f.write(new_content)'''

import json
def read_data(id_):
    with open(f"./users/{id_}_info.json", "r") as json_file:
        json_data = dict(json.load(json_file))
        json_list = list(json_data.items())
    return json_list

print(read_data('whdtj9012'))