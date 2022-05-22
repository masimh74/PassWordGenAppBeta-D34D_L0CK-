from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import PassGenMod, web_checker, FileStorage, Encryption
current_user = ''
def generate_password(window, password_len, special_char=None, special_word=None):

    if special_char is not None: generated_password = PassGenMod.Generate(int(password_len),special_char)
    else: generated_password = PassGenMod.Generate(int(password_len))
    password_checker(window,generated_password)

def web_checking(window, password):
    database_check = "Not found in data base"
    cracking_time = "not possible to dertermine"
    with web_checker.web_checker() as online_check:
        if online_check.check_password_data_base(password):database_check = "It has been found in data base"
        if online_check.check_cracking_time(password): cracking_time = online_check.check_cracking_time(password)

    strength_password(window,cracking_time.split()[3] +" "+ cracking_time.split()[4], database_check, [f"{password= }","Database used: haveIbeenPwned.com", "Cracking time source: passwordmonster.com"])


def database_checking(window, password):
    database_response = ["Not Found in data base"]
    with web_checker.web_checker() as online_check:
        if online_check.check_password_data_base(password):
            database_response[0] = "Found in Data Base"
            database_response.append("Yes, It's been Found!!")
            database_response.append("HaveIbeenPwned.com")

    data_breach(window,database_response, "bad_checkmark.png") if len(database_response) > 2 else data_breach(window)

def login_screen(window):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/login")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # def retrieve_information(username, password):
    # window.destroy()
    # window = Tk()
    #
    # window.geometry("700x450")
    # window.configure(bg="#FFFFFF")

    window.geometry("700x450")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(window, bg="#FFFFFF", height=450, width=700, bd=0, highlightthickness=0, relief="ridge")

    canvas.place(x=0, y=0)
    canvas.create_rectangle(0.0, 1.0, 700.0, 452.0, fill="#5376F5", outline="")

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(546.0, 200.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(548.0, 201.0, image=image_image_2)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(203.0, 223.0, image=image_image_3)

    canvas.create_text(158.0, 65.0, anchor="nw", text="Introducing....", fill="#172C79",
                       font=("EncodeSansCondensed Regular", 16 * -1))

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(206.0, 259.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#F1F1F1", highlightthickness=0)
    entry_1.place(x=59.0, y=248.0, width=294.0, height=21.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(206.0, 319.5, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#F1F1F1", highlightthickness=0)
    entry_2.place(x=59.0, y=308.0, width=294.0, height=21.0)

    canvas.create_text(49.0, 222.0, anchor="nw", text="UserName", fill="#162C79",
                       font=("EncodeSansCondensed Regular", 16 * -1))

    canvas.create_text(49.0, 285.0, anchor="nw", text="Password", fill="#162C79",
                       font=("EncodeSansCondensed Regular", 16 * -1))

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: click_buttom(window,1,entry_1.get(), entry_2.get()), relief="flat")
    button_1.place(x=209.0, y=343.0, width=142.03125, height=47.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: click_buttom(window,2,entry_1.get(), entry_2.get()), relief="flat")
    button_2.place(x=49.0, y=343.0, width=142.03125, height=47.0)

    canvas.create_rectangle(0.0, 0.0, 700.0, 17.0, fill="#FFFFFF", outline="")

    canvas.create_rectangle(1.0, 429.0, 701.0, 450.0, fill="#FFFFFF", outline="")

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(201.0, 124.0, image=image_image_4)

    canvas.create_text(406.0, 346.0, anchor="nw", text="Security does not need to be inconvenient", fill="#FFFFFF",
                       font=("Timmana", 16 * -1))

    canvas.create_text(496.0, 371.0, anchor="nw", text="Anymore...", fill="#FFFFFF", font=("Timmana", 24 * -1))

    canvas.create_text(593.0, 430.0, anchor="nw", text="Copywrite 2022", fill="#172C79",
                       font=("EncodeSansCondensed Regular", 16 * -1))

    window.resizable(False, False)
    window.mainloop()

def click_buttom(window, button_number, *args):
    values = list(args)
    global current_user
    current_user = values[0]

    response = True
    if button_number == 1:
        with FileStorage.file_handler() as database:
            response = database.user_exists(values[0], values[1])
        print("user exists") if response else print("user doesn't exist")
        # print(button_number, values[0],values[1])
        password_checker(window) if response else login_screen(window)

    elif button_number == 2:
        sign_up_screen(window)

    elif button_number == 3:
        if not(values[0] and values[1] and values[2]):
            sign_up_screen(window)
        ##add user with name, username and password
        with FileStorage.file_handler() as database:
            response = database.add_user(values[0], values[1], values[2])
        print("User has been added",values[0], values[1], values[2]) if response else print("User exists",values[0], values[1], values[2])
        if response:
            with FileStorage.file_handler() as database:
                database.add_password(values[1], "a", "b", "c")
            login_screen(window)
        else:
            sign_up_screen(window)
    else:
        pass
    ## it is a user

def sign_up_screen(window):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/sign_up")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    # window.destroy()
    # window = Tk()
    #
    # window.geometry("700x450")
    # window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=450,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        1.0,
        700.0,
        452.0,
        fill="#5376F5",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        546.0,
        200.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        548.0,
        201.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        203.0,
        223.0,
        image=image_image_3
    )

    canvas.create_text(
        158.0,
        65.0,
        anchor="nw",
        text="Introducing....",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        206.0,
        259.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_1.place(
        x=59.0,
        y=248.0,
        width=294.0,
        height=21.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        206.0,
        201.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_2.place(
        x=59.0,
        y=190.0,
        width=294.0,
        height=21.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        206.0,
        319.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_3.place(
        x=59.0,
        y=308.0,
        width=294.0,
        height=21.0
    )

    canvas.create_text(
        49.0,
        222.0,
        anchor="nw",
        text="UserName",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )

    canvas.create_text(
        49.0,
        164.0,
        anchor="nw",
        text="Name",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )

    canvas.create_text(
        49.0,
        285.0,
        anchor="nw",
        text="Password",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: click_buttom(window,3,entry_2.get(),entry_1.get(),entry_3.get()),
        relief="flat"
    )
    button_1.place(
        x=135.0,
        y=345.0,
        width=142.03125,
        height=47.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        17.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        1.0,
        429.0,
        701.0,
        450.0,
        fill="#FFFFFF",
        outline="")

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        201.0,
        124.0,
        image=image_image_4
    )

    canvas.create_text(
        406.0,
        346.0,
        anchor="nw",
        text="Security does not need to be inconvinient",
        fill="#FFFFFF",
        font=("Timmana", 16 * -1)
    )

    canvas.create_text(
        496.0,
        371.0,
        anchor="nw",
        text="Anymore...",
        fill="#FFFFFF",
        font=("Timmana", 24 * -1)
    )

    canvas.create_text(
        593.0,
        430.0,
        anchor="nw",
        text="Copywrite 2022",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

def password_checker(window, response="Password Length"):
    global current_user
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/password_checker")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # window.destroy()
    # window = Tk()
    #
    # window.geometry("700x450")
    # window.configure(bg="#FFFFFF")

    canvas = Canvas(window, bg="#FFFFFF", height=450, width=700, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_text(
        379.0,
        23.0,
        anchor="nw",
        text="Password Generator",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 24 * -1)
    )

    entry_image_1_PC = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        485.0,
        103.5,
        image=entry_image_1_PC
    )
    entry_1_PC = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_1_PC.place(
        x=301.0,
        y=92.0,
        width=368.0,
        height=21.0
    )

    entry_image_2_PC = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        485.0,
        219.5,
        image=entry_image_2_PC
    )
    entry_2_PC = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_2_PC.place(
        x=301.0,
        y=207.0,
        width=368.0,
        height=23.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("squared.png"))
    image_1 = canvas.create_image(
        485.0,
        390.0,
        image=image_image_1
    )

    canvas.create_text(
        310.0,
        368.0,
        anchor="nw",
        text="The password generated is:(20 digits should do the trick)",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )
    canvas.create_text(
        310.0,
        393.0,
        anchor="nw",
        text=response,
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )
    # button_image_1_PC = PhotoImage(
    #     file=relative_to_assets("button_1.png"))
    # button_1_PC = Button(
    #     image=button_image_1_PC,
    #     borderwidth=0,
    #     highlightthickness=0,command=lambda: print("button_whatever clicked"),
    #     relief="flat"
    # )
    # button_1_PC.place(
    #     x=291.0,
    #     y=378.0,
    #     width=391.375,
    #     height=53.0
    # )

    canvas.create_text(
        291.0,
        72.0,
        anchor="nw",
        text="Password Length",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    entry_image_3_PC = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        485.0,
        162.5,
        image=entry_image_3_PC
    )
    entry_3_PC = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_3_PC.place(
        x=301.0,
        y=151.0,
        width=368.0,
        height=21.0
    )

    canvas.create_text(
        291.0,
        188.0,
        anchor="nw",
        text="Special Word",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    canvas.create_text(
        291.0,
        130.0,
        anchor="nw",
        text="Special characters",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    button_image_2_PC = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2_PC = Button(
        image=button_image_2_PC,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: generate_password(window, entry_1_PC.get(),entry_2_PC.get(),entry_3_PC.get()),
        relief="flat"
    )
    button_2_PC.place(
        x=429.1458435058594,
        y=250.0,
        width=142.03128051757812,
        height=47.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        268.0,
        450.0,
        fill="#5376F5",
        outline="")

    image_image_1_PC = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        133.0,
        253.0,
        image=image_image_1_PC
    )

    button_image_3_PC = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3_PC = Button(
        image=button_image_3_PC,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: help(window),
        relief="flat"
    )
    button_3_PC.place(
        x=197.0,
        y=406.0,
        width=54.0,
        height=23.0
    )

    button_image_4_PC = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4_PC = Button(
        image=button_image_4_PC,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_4_PC.place(
        x=19.87640380859375,
        y=86.80889129638672,
        width=225.0,
        height=45.00000762939453
    )

    button_image_5_PC = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5_PC = Button(
        image=button_image_5_PC,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: strength_password(window),
        relief="flat"
    )
    button_5_PC.place(
        x=20.0,
        y=141.0,
        width=225.0,
        height=45.0
    )

    button_image_6_PC = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6_PC = Button(
        image=button_image_6_PC,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: passwords(window),
        relief="flat"
    )
    button_6_PC.place(
        x=20.0,
        y=194.0,
        width=225.0,
        height=45.0
    )

    button_image_7_PC = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7_PC = Button(
        image=button_image_7_PC,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: data_breach(window),
        relief="flat"
    )
    button_7_PC.place(
        x=20.0,
        y=248.0,
        width=225.0,
        height=45.0
    )

    image_image_2_PC = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        167.0,
        35.0,
        image=image_image_2_PC
    )

    image_image_3_PC = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        37.0,
        36.0,
        image=image_image_3_PC
    )

    canvas.create_text(
        120.0,
        36.0,
        anchor="nw",
        text= current_user,
        fill="#000000",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )

    canvas.create_text(
        100.0,
        13.0,
        anchor="nw",
        text="Welcome Back !!",
        fill="#000000",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

def strength_password(window, time_to_crack = "Enter password", web_check_database = "", summary = ["This might take a minute", "Please give it some time to check", "we are checking reputable websites for you"]):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/strength_password")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # window.destroy()
    # window = Tk()
    #
    # window.geometry("700x450")
    # window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=450,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        402.0,
        22.0,
        anchor="nw",
        text="Strength Checker",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 24 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        485.0,
        103.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_1.place(
        x=301.0,
        y=92.0,
        width=368.0,
        height=21.0
    )

    canvas.create_text(
        291.0,
        72.0,
        anchor="nw",
        text="Password",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: web_checking(window, entry_1.get()),
        relief="flat"
    )
    button_1.place(
        x=414.0,
        y=126.0,
        width=142.03125,
        height=47.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        268.0,
        450.0,
        fill="#5376F5",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        133.0,
        253.0,
        image=image_image_1
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: help(window),
        relief="flat"
    )
    button_2.place(
        x=197.0,
        y=406.0,
        width=54.0,
        height=23.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: password_checker(window),
        relief="flat"
    )
    button_3.place(
        x=19.87640380859375,
        y=86.80889892578125,
        width=225.0,
        height=45.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=20.0,
        y=141.0,
        width=225.0,
        height=45.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: passwords(window),
        relief="flat"
    )
    button_5.place(
        x=20.0,
        y=194.0,
        width=225.0,
        height=45.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: data_breach(window),
        relief="flat"
    )
    button_6.place(
        x=20.0,
        y=248.0,
        width=225.0,
        height=45.0
    )

    canvas.create_text(
        291.0,
        193.0,
        anchor="nw",
        text="Time to brute force",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    canvas.create_text(
        291.0,
        227.0,
        anchor="nw",
        text="Web Check",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    canvas.create_text(
        291.0,
        258.0,
        anchor="nw",
        text="Summary",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        521.0,
        234.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        521.0,
        200.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        554.0,
        348.0,
        image=image_image_4
    )

    canvas.create_text(
        422.0,
        191.0,
        anchor="nw",
        text=time_to_crack,
        fill="#000000",
        font=("EncodeSansCondensed Regular", 13 * -1)
    )

    canvas.create_text(
        422.0,
        225.0,
        anchor="nw",
        text="Not found in a data base.. Yet..." if web_check_database == "" else "It has been found! Congrats!:D/... Perfect...",
        fill="#000000",
        font=("EncodeSansCondensed Regular", 13 * -1)
    )
    size = 265
    for element in summary:
        canvas.create_text(418,size,anchor="nw",text=element,fill="#000000",font=("EncodeSansCondensed Regular", 13 * -1))
        size += 20
    #
    # canvas.create_text(
    #     423.0,
    #     289.0,
    #     anchor="nw",
    #     text="Minimun legth check ",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     423.0,
    #     307.0,
    #     anchor="nw",
    #     text="Reused Password",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     582.0,
    #     271.0,
    #     anchor="nw",
    #     text=" // pass",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     582.0,
    #     289.0,
    #     anchor="nw",
    #     text="Yes or No",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     582.0,
    #     307.0,
    #     anchor="nw",
    #     text="Yes or No",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     503.0,
    #     338.0,
    #     anchor="nw",
    #     text="Recommendations",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     423.0,
    #     357.0,
    #     anchor="nw",
    #     text="Contains Special characters",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     419.0,
    #     374.0,
    #     anchor="nw",
    #     text="Contains Special characters",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     419.0,
    #     391.0,
    #     anchor="nw",
    #     text="Contains Special characters",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     419.0,
    #     408.0,
    #     anchor="nw",
    #     text="Contains Special characters",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        169.0,
        35.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        39.0,
        36.0,
        image=image_image_6
    )

    canvas.create_text(
        113.0,
        37.0,
        anchor="nw",
        text="Is the beginning...",
        fill="#000000",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )

    canvas.create_text(
        108.0,
        14.0,
        anchor="nw",
        text="A strong password",
        fill="#000000",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

def passwords(window):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/passwords")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # window.destroy()
    # window = Tk()
    #
    # window.geometry("700x450")
    # window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=450,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        379.0,
        23.0,
        anchor="nw",
        text="Passwords",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 24 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        484.0,
        77.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F1F1F1",
        highlightthickness=0
    )
    entry_1.place(
        x=347.0,
        y=65.0,
        width=274.0,
        height=23.0
    )

    canvas.create_text(
        286.0,
        68.0,
        anchor="nw",
        text="Search",
        fill="#162C79",
        font=("EncodeSansCondensed Regular", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 Main Fucntion here"),
        relief="flat"
    )
    button_1.place(
        x=636.0,
        y=62.0,
        width=50.0,
        height=33.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 Previous page"),
        relief="flat"
    )
    button_2.place(
        x=492.0,
        y=401.0,
        width=66.0,
        height=29.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 Next page"),
        relief="flat"
    )
    button_3.place(
        x=420.0,
        y=401.0,
        width=66.0,
        height=29.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        268.0,
        450.0,
        fill="#5376F5",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        133.0,
        253.0,
        image=image_image_1
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: help(window),
        relief="flat"
    )
    button_4.place(
        x=197.0,
        y=406.0,
        width=54.0,
        height=23.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: password_checker(window),
        relief="flat"
    )
    button_5.place(
        x=19.87640380859375,
        y=86.80889129638672,
        width=225.00006103515625,
        height=45.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: strength_password(window),
        relief="flat"
    )
    button_6.place(
        x=20.0,
        y=141.0,
        width=225.0,
        height=45.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    button_7.place(
        x=20.0,
        y=194.0,
        width=225.0,
        height=45.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: data_breach(window),
        relief="flat"
    )
    button_8.place(
        x=20.0,
        y=248.0,
        width=225.0,
        height=45.0
    )

    canvas.create_text(
        326.0,
        100.0,
        anchor="nw",
        text="Page",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 13 * -1)
    )

    canvas.create_text(
        453.0,
        100.0,
        anchor="nw",
        text="Username",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 13 * -1)
    )

    canvas.create_text(
        606.0,
        100.0,
        anchor="nw",
        text="Password",
        fill="#172C79",
        font=("EncodeSansCondensed Regular", 13 * -1)
    )

    #
    # image_image_3 = PhotoImage(
    #     file=relative_to_assets("image_3.png"))
    # image_3 = canvas.create_image(
    #     339.0,
    #     169.0,
    #     image=image_image_3
    # )
    #
    # image_image_4 = PhotoImage(
    #     file=relative_to_assets("image_4.png"))
    # image_4 = canvas.create_image(
    #     339.0,
    #     203.0,
    #     image=image_image_4
    # )
    #
    # image_image_5 = PhotoImage(
    #     file=relative_to_assets("image_5.png"))
    # image_5 = canvas.create_image(
    #     339.0,
    #     238.0,
    #     image=image_image_5
    # )
    #
    # image_image_6 = PhotoImage(
    #     file=relative_to_assets("image_6.png"))
    # image_6 = canvas.create_image(
    #     339.0,
    #     273.0,
    #     image=image_image_6
    # )
    #
    # image_image_7 = PhotoImage(
    #     file=relative_to_assets("image_7.png"))
    # image_7 = canvas.create_image(
    #     339.0,
    #     306.0,
    #     image=image_image_7
    # )
    #
    # image_image_8 = PhotoImage(
    #     file=relative_to_assets("image_8.png"))
    # image_8 = canvas.create_image(
    #     339.0,
    #     339.0,
    #     image=image_image_8
    # )
    #
    # image_image_9 = PhotoImage(
    #     file=relative_to_assets("image_9.png"))
    # image_9 = canvas.create_image(
    #     339.0,
    #     373.0,
    #     image=image_image_9
    # )
    #
    #
    # image_image_11 = PhotoImage(
    #     file=relative_to_assets("image_11.png"))
    # image_11 = canvas.create_image(
    #     475.0,
    #     169.0,
    #     image=image_image_11
    # )
    #
    # image_image_12 = PhotoImage(
    #     file=relative_to_assets("image_12.png"))
    # image_12 = canvas.create_image(
    #     475.0,
    #     203.0,
    #     image=image_image_12
    # )
    #
    # image_image_13 = PhotoImage(
    #     file=relative_to_assets("image_13.png"))
    # image_13 = canvas.create_image(
    #     475.0,
    #     238.0,
    #     image=image_image_13
    # )
    #
    # image_image_14 = PhotoImage(
    #     file=relative_to_assets("image_14.png"))
    # image_14 = canvas.create_image(
    #     475.0,
    #     273.0,
    #     image=image_image_14
    # )
    #
    # image_image_15 = PhotoImage(
    #     file=relative_to_assets("image_15.png"))
    # image_15 = canvas.create_image(
    #     475.0,
    #     306.0,
    #     image=image_image_15
    # )
    #
    # image_image_16 = PhotoImage(
    #     file=relative_to_assets("image_16.png"))
    # image_16 = canvas.create_image(
    #     475.0,
    #     339.0,
    #     image=image_image_16
    # )
    #
    # image_image_17 = PhotoImage(
    #     file=relative_to_assets("image_17.png"))
    # image_17 = canvas.create_image(
    #     475.0,
    #     373.0,
    #     image=image_image_17
    # )
    #
    #
    # image_image_19 = PhotoImage(
    #     file=relative_to_assets("image_19.png"))
    # image_19 = canvas.create_image(
    #     625.0,
    #     169.0,
    #     image=image_image_19
    # )
    #
    # image_image_20 = PhotoImage(
    #     file=relative_to_assets("image_20.png"))
    # image_20 = canvas.create_image(
    #     625.0,
    #     203.0,
    #     image=image_image_20
    # )
    #
    # image_image_21 = PhotoImage(
    #     file=relative_to_assets("image_21.png"))
    # image_21 = canvas.create_image(
    #     625.0,
    #     238.0,
    #     image=image_image_21
    # )
    #
    # image_image_22 = PhotoImage(
    #     file=relative_to_assets("image_22.png"))
    # image_22 = canvas.create_image(
    #     625.0,
    #     273.0,
    #     image=image_image_22
    # )
    #
    # image_image_23 = PhotoImage(
    #     file=relative_to_assets("image_23.png"))
    # image_23 = canvas.create_image(
    #     625.0,
    #     306.0,
    #     image=image_image_23
    # )
    #
    # image_image_24 = PhotoImage(
    #     file=relative_to_assets("image_24.png"))
    # image_24 = canvas.create_image(
    #     625.0,
    #     339.0,
    #     image=image_image_24
    # )
    #
    # image_image_25 = PhotoImage(
    #     file=relative_to_assets("image_25.png"))
    # image_25 = canvas.create_image(
    #     625.0,
    #     373.0,
    #     image=image_image_25
    # )
    password_list = []
    with FileStorage.file_handler() as database:
        password_list = database.get_password(current_user)
    for display,element in enumerate(password_list):
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            339.0,
            135.0 + display*35,
            image=image_image_2
        )
        image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        image_10 = canvas.create_image(
            475.0,
            135.0+display*35,
            image=image_image_10
        )
        image_image_18 = PhotoImage(
            file=relative_to_assets("image_18.png"))
        image_18 = canvas.create_image(
            625.0,
            135.0+display*35,
            image=image_image_18
        )

        canvas.create_text(
            286.0,
            128.0,
            anchor="nw",
            text=element.split(",")[0],
            fill="#000000",
            font=("EncodeSansCondensed Regular", 13 * -1)
        )

        canvas.create_text(
            414.0,
            128.0,
            anchor="nw",
            text=element.split(",")[1],
            fill="#000000",
            font=("EncodeSansCondensed Regular", 13 * -1)
        )
        canvas.create_text(
            564.0,
            128.0,
            anchor="nw",
            text=element.split(",")[2],
            fill="#000000",
            font=("EncodeSansCondensed Regular", 13 * -1)
        )

    # canvas.create_text(
    #     414.0,
    #     162.0,
    #     anchor="nw",
    #     text="Username1",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     414.0,
    #     195.0,
    #     anchor="nw",
    #     text="Username2",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     414.0,
    #     231.0,
    #     anchor="nw",
    #     text="Username3",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )

    # canvas.create_text(
    #     414.0,
    #     266.0,
    #     anchor="nw",
    #     text="Username4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     414.0,
    #     299.0,
    #     anchor="nw",
    #     text="Username4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     414.0,
    #     332.0,
    #     anchor="nw",
    #     text="Username4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     414.0,
    #     366.0,
    #     anchor="nw",
    #     text="Username4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    #
    # canvas.create_text(
    #     564.0,
    #     162.0,
    #     anchor="nw",
    #     text="Password 1",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     564.0,
    #     195.0,
    #     anchor="nw",
    #     text="Password 2",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     564.0,
    #     231.0,
    #     anchor="nw",
    #     text="Password 3",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     564.0,
    #     266.0,
    #     anchor="nw",
    #     text="Password 4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     564.0,
    #     296.0,
    #     anchor="nw",
    #     text="Password 4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     564.0,
    #     329.0,
    #     anchor="nw",
    #     text="Password 4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     564.0,
    #     363.0,
    #     anchor="nw",
    #     text="Password 4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     286.0,
    #     161.0,
    #     anchor="nw",
    #     text="Name1",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     286.0,
    #     194.0,
    #     anchor="nw",
    #     text="Name2",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     286.0,
    #     229.0,
    #     anchor="nw",
    #     text="Name3",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     286.0,
    #     264.0,
    #     anchor="nw",
    #     text="Name4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     286.0,
    #     297.0,
    #     anchor="nw",
    #     text="Name4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )
    #
    # canvas.create_text(
    #     286.0,
    #     330.0,
    #     anchor="nw",
    #     text="Name4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )

    # canvas.create_text(
    #     286.0,
    #     364.0,
    #     anchor="nw",
    #     text="Name4",
    #     fill="#000000",
    #     font=("EncodeSansCondensed Regular", 13 * -1)
    # )

    image_image_26 = PhotoImage(
        file=relative_to_assets("image_26.png"))
    image_26 = canvas.create_image(
        168.0,
        36.0,
        image=image_image_26
    )

    image_image_27 = PhotoImage(
        file=relative_to_assets("image_27.png"))
    image_27 = canvas.create_image(
        38.0,
        37.0,
        image=image_image_27
    )

    canvas.create_text(
        114.0,
        26.0,
        anchor="nw",
        text="Saved Passwords",
        fill="#000000",
        font=("EncodeSansCondensed Regular", 16 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

def data_breach(window, response= ["Not Found in DataBase", "Enter password", "check"], image_Chk = "image_6.png"):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/data_breach")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    # window.destroy()
    # window = Tk()
    #
    # window.geometry("700x450")
    # window.configure(bg="#FFFFFF")
    canvas = Canvas(window, bg="#FFFFFF", height=450, width=700, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_text(400.0, 21.0, anchor="nw", text="Data Breach Checker", fill="#172C79",
                       font=("EncodeSansCondensedRegular", 24 * -1))
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(485.0, 103.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#F1F1F1", highlightthickness=0)
    entry_1.place(x=301.0, y=92.0, width=368.0, height=21.0)
    canvas.create_text(291.0, 72.0, anchor="nw", text="Password", fill="#162C79",
                       font=("EncodeSansCondensedRegular", 14 * -1))
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                      command=lambda: database_checking(window, entry_1.get()), relief="flat")
    button_1.place(x=414.0, y=126.0, width=142.03125, height=47.0)
    canvas.create_rectangle(0.0, 0.0, 268.0, 450.0, fill="#5376F5", outline="")
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(133.0, 253.0, image=image_image_1)
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: help(window), relief="flat")
    button_2.place(x=197.0, y=406.0, width=54.0, height=23.0)
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda:password_checker(window), relief="flat")
    button_3.place(x=19.87640380859375, y=86.80889892578125, width=225.0, height=45.0)
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                      command=lambda: strength_password(window), relief="flat")
    button_4.place(x=20.0, y=141.0, width=225.0, height=45.0)
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: passwords(window), relief="flat")
    button_5.place(x=20.0, y=194.0, width=225.0, height=45.0)
    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(image=button_image_6, borderwidth=0, highlightthickness=0, relief="flat")
    button_6.place(x=20.0, y=248.0, width=225.0, height=45.0)
    canvas.create_text(291.0, 193.0, anchor="nw", text="Pwned?", fill="#172C79",
                       font=("EncodeSansCondensedRegular", 14 * -1))
    canvas.create_text(291.0, 227.0, anchor="nw", text="Database Checker", fill="#172C79",
                       font=("EncodeSansCondensedRegular", 14 * -1))
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(530.0, 234.0, image=image_image_2)
    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(530.0, 200.0, image=image_image_3)
    canvas.create_text(431.0, 191.0, anchor="nw", text=response[1], fill="#000000",
                       font=("EncodeSansCondensedRegular", 13 * -1))
    canvas.create_text(431.0, 225.0, anchor="nw", text=response[2], fill="#000000",
                       font=("EncodeSansCondensedRegular", 13 * -1))
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(169.0, 35.0, image=image_image_4)
    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(39.0, 36.0, image=image_image_5)
    canvas.create_text(113.0, 37.0, anchor="nw", text="Is the beginning...", fill="#000000",
                       font=("EncodeSansCondensedRegular", 16 * -1))
    canvas.create_text(108.0, 14.0, anchor="nw", text="A strong password", fill="#000000",
                       font=("EncodeSansCondensedRegular", 16 * -1))
    image_image_6 = PhotoImage(file=relative_to_assets(image_Chk))
    image_6 = canvas.create_image(396.0, 349.0, image=image_image_6)
    canvas.create_text(515.0, 331.0, anchor="nw", text=response[0], fill="#000000",
                       font=("EncodeSansCondensedRegular", 16 * -1))
    window.resizable(False, False)
    window.mainloop()

def help(window):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets/help")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    # window.destroy()
    # window = Tk()
    #
    # window.geometry("700x450")
    # window.configure(bg="#FFFFFF")

    canvas = Canvas(window, bg="#FFFFFF", height=450, width=700, bd=0, highlightthickness=0, relief="ridge")

    canvas.place(x=0, y=0)
    canvas.create_text(465.0, 16.0, anchor="nw", text="Help", fill="#172C79",
                       font=("EncodeSansCondensed Regular", 24 * -1))

    canvas.create_rectangle(0.0, 0.0, 268.0, 450.0, fill="#5376F5", outline="")

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(133.0, 253.0, image=image_image_1)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, relief="flat"
                      )
    button_1.place(x=197.0, y=406.0, width=54.0, height=23.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: password_checker(window), relief="flat")
    button_2.place(x=19.87640380859375, y=86.80889129638672, width=225.0, height=45.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,
                      command=lambda: strength_password(window), relief="flat")
    button_3.place(x=20.0, y=141.0, width=225.0, height=45.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0,
                      command=lambda: passwords(window), relief="flat")
    button_4.place(x=20.0, y=194.0, width=225.0, height=45.0)

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0,
                      command=lambda: data_breach(window), relief="flat")
    button_5.place(x=20.0, y=248.0, width=225.0, height=45.0)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(386.0, 194.0, image=image_image_2)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(390.0, 337.0, image=image_image_3)

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(597.0, 194.0, image=image_image_4)

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(601.0, 337.0, image=image_image_5)

    canvas.create_text(305.0, 186.0, anchor="nw", text="1: Select An Option", fill="#172C79",
                       font=("EncodeSansCondensed Regular", 13 * -1))

    canvas.create_text(309.0, 329.0, anchor="nw", text="3: Click and wait", fill="#172C79",
                       font=("EncodeSansCondensed Regular", 13 * -1))

    canvas.create_text(516.0, 186.0, anchor="nw", text=" 2: Enter Input", fill="#172C79",
                       font=("EncodeSansCondensed Regular", 13 * -1))

    canvas.create_text(520.0, 329.0, anchor="nw", text=" 4: Enjoy", fill="#172C79",
                       font=("EncodeSansCondensed Regular", 13 * -1))

    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(169.0, 35.0, image=image_image_6)

    image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(39.0, 36.0, image=image_image_7)

    canvas.create_text(113.0, 37.0, anchor="nw", text="Is the beginning...", fill="#000000",
                       font=("EncodeSansCondensed Regular", 16 * -1))

    canvas.create_text(108.0, 14.0, anchor="nw", text="A strong password", fill="#000000",
                       font=("EncodeSansCondensed Regular", 16 * -1))

    image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(388.0, 125.0, image=image_image_8)

    image_image_9 = PhotoImage(file=relative_to_assets("image_10.png"))
    image_9 = canvas.create_image(392.0, 268.0, image=image_image_9)

    image_image_10 = PhotoImage(file=relative_to_assets("image_9.png"))
    image_10 = canvas.create_image(599.0, 125.0, image=image_image_10)

    image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(603.0, 268.0, image=image_image_11)

    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(image=button_image_6, borderwidth=0, highlightthickness=0,
                      command=lambda: print("button_6 clicked"), relief="flat")
    button_6.place(x=376.0, y=377.0, width=229.0, height=29.0)

    window.resizable(False, False)
    window.mainloop()

def main():
    encryptor = Encryption.encryption()
    try:
        encryptor.__decrypt__("database.db")
    except:
        pass

    window = Tk()
    login_screen(window)
    try:
        encryptor.__encrypt__("database.db")
    except:
        pass

if __name__ == "__main__":
    main()