from src import *
from time import sleep


def main():
    win = Window(1280, 720)
    while win.alive:
        win.update()
        sleep(0.033)
    print(1)


if __name__ == '__main__':
    main()
