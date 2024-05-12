from src import *
from time import sleep


def main():
    win = Window(480, 360)
    while win.alive:
        win.update()
        # sleep(0.033)


if __name__ == '__main__':
    main()
