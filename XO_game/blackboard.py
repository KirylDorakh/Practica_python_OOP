MARK_X = 'X'
MARK_O = 'O'
MARK_UNKNOWN = ' '


class Cell:
    def __init__(self):
        self.mark = MARK_UNKNOWN

    def set_state(self, mark):
        self.mark = mark

    def get_state(self):
        return self.mark


class Board:
    def __init__(self, r=3, c=3):
        self.cells = []
        self.rowsCount = r
        self.columnsCount = c
        for i in range(r*c):
            self.cells.append(Cell())

    def get_rows_count(self):
        return self.rowsCount

    def get_columns_count(self):
        return self.columnsCount

    def is_cell_available(self, index):
        return self.cells[index-1].get_state() == MARK_UNKNOWN

    def get_state_in_cell(self, index):
        return self.cells[index-1].get_state()

    def set_cell(self, index, mark):
        self.cells[index-1].set_state(mark)

    def get_cells(self):
        return self.cells


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark


def win_condition(board):
    win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    cells = board.cells

    win_mark = MARK_UNKNOWN
    for combo in win_combo:
        s1 = board.get_state_in_cell(combo[0])
        s2 = board.get_state_in_cell(combo[1])
        s3 = board.get_state_in_cell(combo[2])
        if s1 == s2 == s3:
            win_mark = s1
            break

    return win_mark


def render(board):
    rc = board.get_rows_count()
    cc = board.get_columns_count()

    for r in range(rc):
        row = []
        for c in range(cc):
            row.append(board.get_state_in_cell(r*cc + c + 1))
        print("|".join(row))


if __name__ == '__main__':
    # get_users
    # switch_turns
    # get_action

    p1 = Player(name='1', mark=MARK_X)
    p2 = Player(name='2', mark=MARK_O)

    board = Board()
    board.set_cell(2, p1.get_mark())
    board.set_cell(4, p2.get_mark())
    board.set_cell(7, p1.get_mark())
    render(board)
    print('------------')
    board.set_cell(1, p2.get_mark())
    board.set_cell(5, p1.get_mark())
    board.set_cell(8, p2.get_mark())
    render(board)
    print('------------')
    board.set_cell(9, p1.get_mark())
    board.set_cell(6, p2.get_mark())
    board.set_cell(3, p1.get_mark())
    render(board)
    print('------------')
    print(win_condition(board))
