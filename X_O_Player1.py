from tkinter import *
from tkinter import messagebox
from functools import partial
from socket import *
from _thread import *

class TicTacToeClient:
    def __init__(self, host, port):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.host = host
        self.port = port
        self.s.connect((self.host, self.port))
        self.window = Tk()
        self.window.title("tic tac toe")
        self.window.geometry("300x300")
        self.player_symbol = 'X'
        self.opponent_symbol = 'O'
        self.lbl = Label(self.window, text="You play " + self.player_symbol)
        self.lbl.grid(row=1, column=0)
        self.my_turn = 1
        self.iteration = 1
        self.btns = [[0 for x in range(3)] for y in range(3)]

        for i in range(3):
            for j in range(3):
                self.btns[i][j] = Button(self.window, text=" ", bg="yellow", fg="black", width=8, height=4)
                self.btns[i][j].config(command=partial(self.clicked, self.btns[i][j], i, j))
                self.btns[i][j].grid(row=i + 10, column=j + 3)

        start_new_thread(self.recv_thread, ())

        self.window.mainloop()

    def clicked(self, btn, i, j):
        if btn["text"] == " " and self.my_turn == 1:
            btn["text"] = self.player_symbol
            button_number = i * 3 + j
            self.s.send(str(button_number).encode('utf-8'))
            self.my_turn = 0
            self.check(btn)

    def check(self, btn):
        win = 0
        for i in range(3):
            if ((self.btns[i][0]["text"] == self.btns[i][1]["text"] == self.btns[i][2]["text"] != " ")
                    or (self.btns[0][i]["text"] == self.btns[1][i]["text"] == self.btns[2][i]["text"] != " ")):
                if btn["text"] == self.player_symbol:
                    messagebox.showinfo("Congratulations! " + self.player_symbol, "Congratulations you won!")
                else:
                    messagebox.showinfo("Game over " + self.player_symbol, "You lost! better luck next time")
                win = 1
                self.reset()

        if win == 0:
            if ((self.btns[0][0]["text"] == self.btns[1][1]["text"] == self.btns[2][2]["text"] != " ")
                    or (self.btns[0][2]["text"] == self.btns[1][1]["text"] == self.btns[2][0]["text"] != " ")):
                if btn["text"] == self.player_symbol:
                    messagebox.showinfo("Congratulations! " + self.player_symbol, "Congratulations you won!")
                else:
                    messagebox.showinfo("Game over " + self.player_symbol, "You lost! better luck next time")
                win == 1
                self.reset()

        if win == 0 and self.iteration == 9:
            messagebox.showinfo("game over ", "no player won")
            self.reset()

        self.iteration += 1

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.btns[i][j].config(text=" ")
        self.my_turn = 1
        self.iteration = 0

    def recv_thread(self):
        while True:
            try:
                button_number = int(self.s.recv(1024).decode('utf-8'))
                row = int(button_number / 3)
                column = int(button_number % 3)
                self.btns[row][column]["text"] = self.opponent_symbol
                self.my_turn = 1
                self.check(self.btns[row][column])
            except ValueError:
                break

if __name__ == '__main__':
    client = TicTacToeClient("127.0.0.1", 7772)
