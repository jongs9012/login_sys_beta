from os import path
import streamlit as st
from defines import read_data, checking_account, find_values, find_average, compare_days, get_curr_time
from PIL import Image
import json
from collections import OrderedDict

st.set_page_config(layout='wide')


# User survey
def survey(id_):
    # Sleeping Day or Night ?
    st.subheader("Are you sleeping at Night or Day ?", anchor=False)
    night_or_day = st.radio("Night or Day", ("Day", "Night"))
    # Sleeping Hours
    st.subheader(f"How many hours you sleep at {night_or_day}?")
    sleep_hours = st.radio("Hours you sleep", ("4 ~ 5 hours", "5 ~ 6 hours", "6 ~ 7 hours", "Others"))
    # Reason about sleeping that hours
    temp = "Why do you sleep not normally?" if sleep_hours == "Others" else f"Why do you sleeping {sleep_hours}"
    st.subheader(temp)
    reason = str(st.text_input("Please enter reason"))
    if len(reason) >= 1:
        temp = "Are you sleeping at Once?" if sleep_hours == "Others" else f"Are you sleeping {sleep_hours} at Once?"
        st.subheader(temp)
        once_or_not = st.radio("Once at a day?", ("Yes, I usually sleep once at a day.",
                                                  "No, I'm not sleep once at a day."))

        st.subheader("How many times a week do you dream ?")
        dreaming_times = st.radio("Times you dreaming", ("0 ~ 1 times", "2 ~ 3 times", "4 ~ 5 times", "Others"))
        st.subheader("If you were to grade your sleep?")
        quality_dream = st.slider("Score", 0, 100, 70)
        st.write(f"[ Score : {quality_dream} ]")

        light_state = st.radio("Do you sleep with the lights on?", ("Turn on", "Turn off"))
        st.subheader("")
        div()
        st.write("Do you agree to provide information?")
        st.write("It's not used for commercial purpose and is used for information analysis.")
        submit_btn = st.button("Submit")

        # When the survey is finished
        if submit_btn:
            file_path = f"./users/{id_}_info.json"
            with open(file_path, "r") as json_file:
                json_data = dict(json.load(json_file))

            json_data['surveyed'] = "True"

            json_data['sleep_time'] = night_or_day

            json_data['sleep_hours'] = sleep_hours

            json_data['why_sleep'] = reason

            json_data['sleeping_at_once'] = once_or_not

            json_data['dreaming_times'] = quality_dream

            json_data['light_state'] = light_state

            st.success("Finished ! \n Please Logout and Login again :)")

            with open(file_path, 'w') as outfile:
                json.dump(json_data, outfile, indent=4)

def create_account(name, id_, password, time):
    file_path = f"./users/{id_}_info.json"
    data = {}
    data["name"] = name
    data["id"] = id_
    data["pwd"] = password
    data["sign_up"] = time
    data["surveyed"] = "False"
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
    st.success("Successfully finished !")
    st.write("Go to login menu to login.")


def div():
    st.subheader("___________________________")


def sign_up():
    st.subheader("Thanks for joining us", anchor=False)
    st.header("Name")
    user_name = str(st.text_input("Enter your name"))
    st.header("ID / PW", anchor=None)
    user_id = str(st.text_input("Make wonderful ID"))
    user_pwd = str(st.text_input("Ridicules password is the best", type="password"))
    if len(user_pwd) <= 8 and user_pwd is not None:
        st.info("We recommend you to make long password")
    if (len(user_id) >= 2) and (len(user_pwd) >= 2) and (len(user_name) >= 2):
        if st.checkbox("Agree to save my info"):
            # Save and register user
            if st.button("Sign UP!"):
                # Make user file
                if path.exists(f"./users/{user_id}_info.txt"):
                    st.warning("This id is already using. Please use another ID.")
                else:
                    create_account(user_name, user_id, user_pwd, str(f"{get_curr_time()}"))


def load_image(image_file):
    img = Image.open(image_file)
    return img


def short_div():
    st.subheader("________")


def main():
    # Title message
    st.title("Welcome", anchor=False)

    # Sidebar Menu
    menu = ["Main", "Login", "Sign Up"]
    choose = st.sidebar.selectbox("Menu", menu)
    div()

    # Main page
    if choose == "Main":
        st.write("Click the button on left top to open sidebar")

    # Login page
    if choose == "Login":
        st.subheader("Sign in to see fancy data!", anchor=False)

        user_id = str(st.sidebar.text_input("Enter ID"))
        user_pwd = str(st.sidebar.text_input("Enter Password", type="password"))

        st.sidebar.subheader("Click the box to login \nIf click check box again you will logout")
        login_check_box = st.sidebar.checkbox("Login")
        check_login = checking_account(user_id, user_pwd)  # Receive a value from userinfo.txt
        if login_check_box:

            # Correct ID / PW
            if check_login[0]:
                # If user doesn't have survey data.
                if check_login[1] is False:
                    survey(user_id)

                # After Surveyed
                else:
                    user_data = read_data(user_id)

                    # Beta alarm
                    st.warning("This is beta version. Many things are not working :(")
                    c1, c2, c3, c4 = st.columns(4)

                    with c1:
                        st.subheader(f"Hi ! {user_data[0][1]}")
                        select_bar = ["Home", "Main", "My info", "BETA"]
                        main_select_box = st.selectbox("Choose menu", select_bar)

                    with c2:
                        # Home Menu
                        if main_select_box == "Home":
                            st.subheader("This is Home Menu")

                        # Main Menu
                        if main_select_box == "Main":
                            # with c2:
                            st.subheader("Sleep night or day")
                            average_5 = find_average(5)
                            for key in average_5:
                                st.write(f"{key} : {average_5[key]} people")
                            short_div()

                            st.subheader("Average Sleep time")
                            average_6 = find_average(6)
                            for key in average_6:
                                st.write(f"{key} : {average_6[key]} people")
                            short_div()

                            st.subheader("Dreaming Times")
                            average_9 = find_average(9)
                            for key in average_9:
                                st.write(f"{key} : {average_9[key]} people")
                            with c3:
                                st.subheader("Reason of Sleeping hours")
                                values_7 = find_values(7)
                                with st.container():
                                    for i in values_7:
                                        st.write(i)
                                short_div()

                                st.subheader("Quality of sleep")
                                average_8 = find_average(8)
                                for key in average_8:
                                    st.write(f"{key} : {average_8[key]} people")

                            with c4:
                                st.subheader("Grade of Sleep")
                                values_10 = find_values(10)
                                with st.container():
                                    for i in values_10:
                                        st.write(i)

                                values = find_values(10)
                                score = 0
                                for i in values:
                                    score += int(i)
                                st.write(f"Average Score : {float(score / len(values))}")

                                short_div()
                                st.subheader("Light state")
                                average_11 = find_average(11)
                                for key in average_11:
                                    st.write(f"{key} : {average_11[key]} people")

                        # My info
                        if main_select_box == "My info":

                            with c1:
                                info_menu = ["Account", "Survey Info"]
                                info_choose = st.selectbox("Menu", info_menu)
                            # with c2:
                            if info_choose == "Account":
                                short_div()
                                st.subheader(f"User Id")
                                st.subheader(f"{user_data[1][1]}")
                                with c3:
                                    date_diff = compare_days(user_id)
                                    short_div()
                                    st.subheader(f"Day we spend together")
                                    st.subheader(f"{date_diff[0]} Days, {date_diff[1]} Hours")
                            if info_choose == "Survey Info":
                                short_div()
                                st.subheader("Sleep type")
                                st.subheader(f"{user_data[5][1]}")
                                short_div()
                                st.subheader("Sleeping Hours")
                                st.subheader(f"{user_data[6][1]}")
                                with c3:
                                    short_div()
                                    st.subheader("Reason about sleeping hours")
                                    st.subheader(f"{user_data[7][1]}")
                                    short_div()
                                    st.subheader("Sleeping at once ?")
                                    st.subheader(f"{user_data[8][1][0:3]}.")
                                with c4:
                                    short_div()
                                    st.subheader("How often you dreaming ?")
                                    st.subheader(f"{user_data[9][1]} times")
                                    short_div()
                                    st.subheader("Grade of sleeping")
                                    st.subheader(f"Score : {user_data[10][1]}")
                                    short_div()
                                    st.subheader("Turn on light when sleeping ?")
                                    st.subheader(f"{user_data[11][1]}")
                        if main_select_box == "BETA":
                            st.subheader("Image")
                            st.write("You can upload images on here.")

                            with c3:
                                image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
                                if image_file is not None:
                                    # To See details
                                    file_details = {"filename": image_file.name, "filetype": image_file.type,
                                                    "file size": image_file.size}
                                    st.write(file_details)
                                    # To View Uploaded Image
                                    st.image(load_image(image_file), width=250)

            # Wrong password
            else:
                st.sidebar.write("ID or Password is wrong")

    # Sign up page
    if choose == "Sign Up":
        sign_up()


if __name__ == '__main__':
    main()
