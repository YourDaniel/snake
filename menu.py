from tkinter import *
import main
main_menu = Tk()
main_menu.title('Snake')
font = 'Consolas'

class MenuButton:
    def __init__(self, master, text):
        self.w = Button(master, text=text, bg='black', fg='white', height=3, width=30, activebackground='gray', activeforeground='white', font=('Consolas', 10, 'normal'))
        self.w.pack()

Label(text='Snake', font=("Consolas", 20, 'bold')).pack()
Label(text='Main Menu', font=("Consolas", 16, 'normal')).pack()

start_button = MenuButton(main_menu, 'Start New Game')
scores_button = MenuButton(main_menu, 'High Scores')
exit_button = MenuButton(main_menu, 'Exit')


def start_game():
    main.root


start_button.w.config(command=start_game)
main_menu.mainloop()
