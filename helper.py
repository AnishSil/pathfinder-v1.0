class Helper():
    def __init__(self) -> None:
        pass

    def h(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)



    def get_clicked_pos(self, pos, rows, width):
        gap = width //rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col

