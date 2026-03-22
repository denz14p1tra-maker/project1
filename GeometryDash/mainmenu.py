from customtkinter import *
from PIL import Image, ImageTk
from levels import LevelsWindow   # імпортуємо клас з іншого файлу


class MainWindow:
    def __init__(self):
        self.mw = CTk()
        self.mw.geometry('2560x1440')
        self.mw.title('Dash')
        self.mw.configure(fg_color="#00994C")
        self.mw.resizable(False, False)

        image_1 = Image.open("dash.png")
        image_2 = Image.open("icons.png")
        image_3 = Image.open("levels.png")
        image_4 = Image.open("settings.png")

        self.name = ImageTk.PhotoImage(image_1)
        self.icon = ImageTk.PhotoImage(image_2)
        self.levels = ImageTk.PhotoImage(image_3)
        self.settings = ImageTk.PhotoImage(image_4)

        def open_levels():
            level_window = LevelsWindow()
            level_window.mainloop()

        self.text_label = CTkLabel(master=self.mw, image=self.name, text="")
        self.text_label.place(relx=0.5, rely=0.2, anchor="center")

        self.button_frame = CTkFrame(master=self.mw, width=300, height=400, fg_color="transparent")
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.btn1 = CTkButton(master=self.button_frame, text="", image=self.icon, fg_color="#00994C",
                              compound="top", width=150, height=150)
        self.btn1.grid(row=0, column=0, padx=100, pady=20)


        self.btn2 = CTkButton(master=self.button_frame, text="", image=self.levels, fg_color="#00994C",
                              compound="top", command=open_levels, width=150, height=150)
        self.btn2.grid(row=0, column=1, padx=100, pady=20)

        self.btn3 = CTkButton(master=self.button_frame, text="", image=self.settings, fg_color="#00994C",
                              compound="top", width=150, height=150)
        self.btn3.grid(row=0, column=2, padx=100, pady=20)

        self.mw.mainloop()

win = MainWindow()
