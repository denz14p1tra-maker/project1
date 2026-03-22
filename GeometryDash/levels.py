from customtkinter import *
from PIL import Image, ImageTk


class LevelsWindow:
    def __init__(self):
        self.lw = CTk()
        self.lw.geometry('2560x1440')
        self.lw.title('Levels')
        self.lw.configure(fg_color="#00994C")
        self.lw.resizable(False, False)

        self.image_1 = CTkImage(
            light_image=Image.open("levels.png"),
            size=(200, 200)
        )
        self.image_2 = CTkImage(
            light_image=Image.open("level_1.png"),
            size=(200, 200)  # размер картинки
        )
        self.image_3 = CTkImage(
            light_image=Image.open("level_2.png"),
            size=(200, 200)  # размер картинки
        )
        self.image_4 = CTkImage(
            light_image=Image.open("level_3.png"),
            size=(200, 200)  # размер картинки
        )


        self.text_label = CTkLabel(master=self.lw, image=self.image_1, text="")
        self.text_label.place(relx=0.5, rely=0.2, anchor="center")

        self.button_frame = CTkFrame(master=self.lw, width=300, height=400, fg_color="transparent")
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.btn1 = CTkButton(master=self.button_frame, text="", image=self.image_2, fg_color="#00994C",
                              compound="top", width=150, height=150)
        self.btn1.grid(row=0, column=0, padx=100, pady=20)

        self.btn2 = CTkButton(master=self.button_frame, text="", image=self.image_3, fg_color="#00994C",
                              compound="top", width=150, height=150)
        self.btn2.grid(row=0, column=1, padx=100, pady=20)

        self.btn3 = CTkButton(master=self.button_frame, text="", image=self.image_4, fg_color="#00994C",
                              compound="top", width=150, height=150)
        self.btn3.grid(row=0, column=2, padx=100, pady=20)

        self.lw.mainloop()

