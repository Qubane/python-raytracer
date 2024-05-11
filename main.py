from src import *
from time import sleep


def main():
    win = Window(480, 360)
    count = 0
    while win.alive:
        for y in range(win.height):
            for x in range(win.width):
                win.plot(x, count % win.height, (255, count & 255, 0))
            count += 1
            win.update()
        # sleep(0.033)


if __name__ == '__main__':
    main()
