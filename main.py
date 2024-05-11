from src import *
from time import sleep


def main():
    win = Window(480, 360)
    count = 0
    while win.alive:
        for y in range(win.height):
            for x in range(win.width):
                win.plot_unit(x, y, (x / win.width, int(count / 255) & 255, y / win.height))
        win.update()
        count += 1
        print(count & 255)
        sleep(0.033)


if __name__ == '__main__':
    main()
