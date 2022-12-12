import tkinter as tk
from tkinter.messagebox import showinfo
from dataclasses import dataclass
from functools import partial
import sys


@dataclass
class Res:
    background: tk.PhotoImage
    zero: tk.PhotoImage
    cross: tk.PhotoImage


class MyButton(tk.Button):
    filled = None


class Field:
    def __init__(self, debug=False) -> None:
        self.DEBUG = debug
        self.turn = 0
        self.__init_window()
        self.__load_assets()
        self.__init_cells()
        self.__init_exit_button()
        self.__init_restart_button()

    def run(self) -> None:
        self.window.mainloop()

    def restart(self) -> None:
        self.turn = 0
        for i in self.cells:
            for j in i:
                j.destroy()
        self.__init_cells()

    def quit(self) -> None:
        sys.exit()

    def __check_draw(self) -> None:
        f = True
        for row in self.cells:
            for button in row:
                if button.filled == None:
                    f = False
                    break
        if f:
            showinfo(message='DRAW')
    
    def __check_win(self) -> bool:
        return self.__check_columns() or self.__check_diags() or self.__check_rows()

    def __check_diags(self) -> bool:
        win_comb = [['cross', 'cross', 'cross'], ['zero', 'zero', 'zero']]
        main_d = []
        for i in range(3):
            main_d.append(self.cells[i][i].filled)
        if main_d in win_comb:
            showinfo(message="WIN")
            return True
        sub_d = []
        for i in range(3):
            sub_d.append(self.cells[2-i][i].filled)
        if sub_d in win_comb:
            showinfo(message="WIN")
            return True
        return False

    def __check_rows(self) -> bool:
        win_comb = [['cross', 'cross', 'cross'], ['zero', 'zero', 'zero']]
        for i in self.cells:
            row = []
            for j in i:
                row.append(j.filled)
            if row in win_comb:
                showinfo(message="WIN")
                return True
        return False

    def __check_columns(self) -> bool:
        win_comb = [['cross', 'cross', 'cross'], ['zero', 'zero', 'zero']]
        for i in range(3):
            c = self.__get_column(i)
            if c in win_comb:
                showinfo(message="WIN")
                return True
        return False
    
    def __get_column(self, idx: int) -> list[bool]:
        r = []
        for i in self.cells:
            r.append(i[idx].filled)
        return r

    def __place_sign(self, button_idx: list[int, int]) -> None:
        if self.DEBUG:
            print(self.turn)
        self.turn += 1
        x, y = button_idx
        if self.turn % 2 == 0:
            self.cells[x][y]['image'] = self.pict.cross
            self.cells[x][y]['command'] = self.__empty_command
            self.cells[x][y].filled = 'cross'
            if not self.__check_win():
                self.__check_draw()
            return
        self.cells[x][y]['image'] = self.pict.zero
        self.cells[x][y]['command'] = self.__empty_command
        self.cells[x][y].filled = 'zero'
        if not self.__check_win():
            self.__check_draw()
        return 

    def __empty_command(self) -> None:
        pass

    def __load_assets(self) -> None:
        try:
            self.pict = Res(background = tk.PhotoImage(file='cell_bg.png'),
                        zero = tk.PhotoImage(file='zero.png'),
                        cross = tk.PhotoImage(file='cross.png')
                        )
            print("assets loaded")
        except Exception as e:
            print("Error occured while loading assests")
    
    def __init_window(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("155x200")
        self.window.title = "TIC-TAC-TOE"

    def __init_cells(self) -> None:
        self.cells = []
        for i in range(3):
            self.cells.append([])
            for j in range(3):
                cmd = partial(self.__place_sign, [i, j])
                self.cells[-1].append(MyButton(image=self.pict.background,
                                                height='50',
                                                width='50',
                                                command=cmd))
                self.cells[-1][-1].place(x=50*i + 1*(i+1), y=50*j + 1 * j)

    def __init_exit_button(self) -> None:
        self.exit_button = tk.Button(text='EXIT', command=self.quit)
        self.exit_button.place(y=170, x=20)

    def __init_restart_button(self) -> None:
        self.restart_button = tk.Button(text='RESTART', command=self.restart)
        self.restart_button.place(x=70, y=170)
