from customtkinter import *
from PIL import Image, ImageTk
import pygame
from random import randint

from Макан.main import running


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

        self.text_label = CTkLabel(master=self.mw, image=self.name, text="")
        self.text_label.place(relx=0.5, rely=0.2, anchor="center")

        self.button_frame = CTkFrame(master=self.mw, width=300, height=400, fg_color="transparent")
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.btn1 = CTkButton(master=self.button_frame, text="", image=self.icon, fg_color="#00994C",
                              compound="top", width=150, height=150, command=self.start_game)
        self.btn1.grid(row=0, column=0, padx=100, pady=20)

        self.btn2 = CTkButton(master=self.button_frame, text="", image=self.levels, fg_color="#00994C",
                              compound="top", width=150, height=150)
        self.btn2.grid(row=0, column=1, padx=100, pady=20)

        self.btn3 = CTkButton(master=self.button_frame, text="", image=self.settings, fg_color="#00994C",
                              compound="top", width=150, height=150)
        self.btn3.grid(row=0, column=2, padx=100, pady=20)

        self.mw.mainloop()

    def start_game(self):
        run_game()

def generate_pipes(count, pipe_width=140, gap=280, min_height=50, max_height=440, distance=300, window_size=(800,600)):
    pipes = []
    start_x = window_size[0]
    for i in range(count):
        height = randint(min_height, max_height)
        top_pipe = pygame.Rect(start_x, 0, pipe_width, height)
        bottom_pipe = pygame.Rect(start_x, height + gap, pipe_width, window_size[1] - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes


def run_game():
    pygame.init()
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Flappy Pipes")

    pipes = generate_pipes(10, window_size=window_size)
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for pipe in pipes[:]:
            pipe.x -= 5
            pygame.draw.rect(screen, (0, 255, 0), pipe)
            if pipe.x < -150:
                pipes.remove(pipe)

        if len(pipes) < 6:
            pipes += generate_pipes(5, window_size=window_size)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

win = MainWindow()

