from dataclasses import dataclass
import sys


def except_hook(exc_type, exc_value, tb):
    pass


sys.excepthook = except_hook


@dataclass
class Coordinates:
    x: int
    y: int


class IsTaken(BaseException):
    pass


class Win(BaseException):
    pass


class Draw(BaseException):
    pass


class Field:
    def __init__(self, **kwargs) -> None:
        if kwargs:
            self.field = kwargs['field']
            return
        self.field = [['.', '.', '.', ], ['.', '.', '.', ], ['.', '.', '.', ]]

    def mark(self, sign: str, number: int = None, coords: Coordinates = None) -> None:
        f = False
        if coords:
            if self.field[coords.x][coords.y] == '.':
                self.field[coords.x][coords.y] = sign
                try:
                    self.check_win()
                except Win as w:
                    f = True
            else:
                print("cell is taken")
                raise IsTaken
        elif number:
            c = 0
            for i in range(3):
                for j in range(3):
                    if c == number-1:
                        if self.field[i][j] == '.':
                            self.field[i][j] = sign
                            try:
                                self.check_win()
                            except Win as w:
                                f = True
                        else:
                            print("cell is taken")
                            raise IsTaken
                    c += 1
        if f:
            print("WIN")
            raise Win
        if self.__check_draw():
            raise Draw

    def clear(self):
        self.field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def check_win(self) -> tuple:
        try:
            self.__check_rows()
        except Win as e:
            raise Win
        try:
            self.__check_diags()
        except Win as e:
            raise Win
        try:
            self.__check_columns()
        except Win as e:
            raise Win

    def __check_rows(self) -> None:
        '''
            0
            1
            2
        '''
        comb = [['+', '+', '+'], ['0', '0', '0']]
        if self.field[0] in comb:
            raise Win(0)
        elif self.field[1] in comb:
            raise Win(1)
        elif self.field[2] in comb:
            raise Win(2)


    def __check_diags(self) -> None:
        ''' 3 or 4'''
        main_d = []
        comb = [['+', '+', '+'], ['0', '0', '0']]
        for i in range(3):
            main_d.append(self.field[i][i])
        if main_d in comb:
            raise Win(3)
        sub_d = []
        for i in range(0, 3):
            sub_d.append(self.field[2-i][i])
        if sub_d in comb:
            raise Win(4)

    def __check_columns(self) -> None:
        '''5 6 7'''
        comb = [['+', '+', '+'], ['0', '0', '0']]
        for i in range(3):
            if self.__get_column(i) in comb:
                raise Win(i + 5)

    def __get_column(self, index: int) -> list:
        c = []
        for i in range(3):
            c.append(self.field[i][index])
        return c

    def __check_draw(self):
        for i in self.field:
            for j in i:
                if j == '.':
                    return False
        return True

class Game:
    def __init__(self):
        self.c = 0
        self.f = Field()
        self.sign = '+'
        self.runnning = False

    def turn(self) -> None:
        self.c += 1
        if self.c % 2 == 0:
            self.sign = '0'
        else:
            self.sign = '+'
        cell = input()
        if len(cell) > 1:
            cell = list(map(int, cell.split()))
            cell = Coordinates(cell[0], cell[1])
            try:
                self.f.mark(sign=self.sign, coords=cell)
            except Exception as e:
                if type(e) == Win:
                    print("WIN")
                    raise Win
                elif type(e) == IsTaken:
                    print("Cell Is taken")
                    raise IsTaken
                elif type(e) == Draw:
                    print("DRAW")
                    raise Draw
                else:
                    print(e)
        else:
            try:
                self.f.mark(sign=self.sign, number=int(cell))
            except Exception as e:
                if type(e) == Win:
                    print("WIN")
                    raise Win
                elif type(e) == IsTaken:
                    print("Cell Is taken")
                    raise IsTaken
                elif type(e) == Draw:
                    print("DRAW")
                    raise Draw
                else:
                    print(e)

    def new_game(self) -> None:
        self.f.clear()
        self.run()

    def exit(self) -> None:
        self.runnning = False

    def run(self):
        self.runnning = True
        while self.runnning:
            for i in self.f.field:
                for j in i:
                    print(j, end=' ')
                print()
            try:
                self.turn()
            except Exception as e:
                if type(e) == Win:
                    return
                elif type(e) == IsTaken:
                    self.f.c -= 1
                    self.turn() 
                elif type(e) == Draw:
                    return 


g = Game()
g.run()
