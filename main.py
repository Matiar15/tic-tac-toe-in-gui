from tkinter import *
import random


def creating_buttons():
    button_0 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_0),
                      bd=3)

    button_1 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_1),
                      bd=3)

    button_2 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_2),
                      bd=3)

    button_3 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_3),
                      bd=3)

    button_4 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_4),
                      bd=3)

    button_5 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_5),
                      bd=3)

    button_6 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_6),
                      bd=3)

    button_7 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_7),
                      bd=3)

    button_8 = Button(board,
                      height=5,
                      width=5,
                      command=lambda: button_clicked(button_8),
                      bd=3)
    return button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8


def game_ended():
    winner_label.place(x=50, y=75)
    player_turn_label.pack_forget()
    end_label.place(x=50, y=100)
    reset_button.place(x=50, y=125)
    quit_button.place(x=150, y=125)
    for b in btns:
        b.config(text=" ",
                 state=NORMAL)


def reset_game():
    winner_label.place_forget()
    end_label.place_forget()
    reset_button.place_forget()
    quit_button.place_forget()
    list_of_current_score_O.clear()
    list_of_current_score_X.clear()
    list_of_total_score.clear()
    player_turn_label.pack()
    board.pack()


def player_turn():
    global count
    if count % 2 == 0:
        count += 1
        return players[0], players[1]
    else:
        count += 1
        return players[1], players[0]


def new_window():
    intro_button.destroy()
    window_2 = Toplevel()
    window_2.title("Intro")
    window_2.geometry("270x100")
    Label(window_2, text="Welcome to the Tic-Tac-Toe game\nRules are the same as in every tic-tac-toe game\n"
                         "The game is intended for two players\nGood luck!").pack()
    Button(window_2, text="Close", command=window_2.destroy).pack()


def button_clicked(button_number):
    win_con = 0
    plr = player_turn()
    button_number.configure(text=plr[0],
                            state=DISABLED)
    player_turn_label.configure(text="It's Player {} turn".format(plr[1]))  # zmiana tury
    if intro_button.winfo_exists() == 1:    # jeżeli gracz nie kliknął w intro to samo sie usuwa po 1 turze
        intro_button.destroy()
    for btn in list_of_buttons:
        if btn == button_number:
            btn = list_of_buttons.index(btn)
            if plr[0] == "X":
                list_of_current_score_X.append(btn)
                list_of_total_score.append(btn)
            elif plr[0] == "O":
                list_of_current_score_O.append(btn)
                list_of_total_score.append(btn)
    for win_con in list_of_winners:
        if win_con.issubset(list_of_current_score_X):
            board.pack_forget()
            winner_label.config(text="Player X won!")
            game_ended()
        elif win_con.issubset(list_of_current_score_O):
            board.pack_forget()
            winner_label.config(text="Player O won!")
            game_ended()
    if not win_con.issubset(list_of_current_score_O) and not win_con.issubset(list_of_current_score_X) and \
            len(list_of_total_score) == 9:
        board.pack_forget()
        winner_label.config(text="Draw!")
        game_ended()


window = Tk()
window.geometry("250x370")
window.title("Tic-Tac-Toe")

players = ["X", "O"]
random.shuffle(players)
count = 0

board = Frame(window)

intro_button = Button(window,
                      text="Welcome, click this button to see the intro",
                      command=new_window,
                      bd=3)

player_turn_label = Label(window,
                          bd=3,
                          relief=RAISED,
                          text="It's Player {} turn".format(players[0]))
btns = creating_buttons()
list_of_total_score = []
list_of_current_score_X = []  # list that summs up player X choices
list_of_current_score_O = []  # list that summs up player O choices
list_of_buttons = [btns[0], btns[1], btns[2], btns[3], btns[4], btns[5], btns[6], btns[7], btns[8]]
list_of_winners = [{0, 4, 8},
                   {6, 4, 2},
                   {0, 1, 2},
                   {3, 4, 5},
                   {6, 7, 8},
                   {0, 3, 6},
                   {1, 4, 7},
                   {2, 5, 8}]
winner_label = Label(window,
                     bd=3,
                     relief=RAISED,
                     text="")
reset_button = Button(window,
                      bd=3,
                      relief=RAISED,
                      text="Yes",
                      command=reset_game)
quit_button = Button(window,
                     bd=3,
                     relief=RAISED,
                     text="No",
                     command=window.destroy)
end_label = Label(window,
                  text="Do you want to play again?",
                  bd=3,
                  relief=RAISED)
btns[0].grid(row=0, column=0)  # pakowanie wszystkich rzeczy do okna
btns[1].grid(row=0, column=1)
btns[2].grid(row=0, column=2)
btns[3].grid(row=1, column=0)
btns[4].grid(row=1, column=1)
btns[5].grid(row=1, column=2)
btns[6].grid(row=2, column=0)
btns[7].grid(row=2, column=1)
btns[8].grid(row=2, column=2)
player_turn_label.pack()
intro_button.pack()
board.pack()
window.mainloop()
