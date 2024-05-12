import tkinter as tk


class Window:
    """
    Tkinter window class
    """

    def __init__(self, width: int, height: int):
        # window things
        self.width: int = width
        self.height: int = height
        self.buffer: list[float] = [0 for _ in range(width * height * 3)]

        # tkinter part
        self._tk_root = tk.Tk()
        self._tk_root.title("Raytracer")
        self._tk_root.protocol("WM_DELETE_WINDOW", lambda: self._die(self._tk_root))

        self._tk_canvas = tk.Canvas(self._tk_root, width=self.width, height=self.height, bg="#000000")
        self._tk_canvas.pack(padx=0, pady=0, expand=True)
        self._tk_image = tk.PhotoImage(width=self.width, height=self.height)
        self._tk_canvas.create_image((self.width // 2, self.height // 2), image=self._tk_image, state='normal')

        self._tk_alive: bool = True

        # make the window appear
        self.semi_update()

    def _die(self, win):
        """
        When window dies
        """

        self._tk_alive = False
        win.destroy()

    @property
    def alive(self):
        """
        Is the window still alive
        """

        return self._tk_alive

    def semi_update(self):
        """
        Updates the window, but just so it wouldn't freeze
        """

        self._tk_root.update()

    def update(self):
        """
        Actual window update, updates the image
        """

        self._tk_image.configure(
            data=f'P6 {self.width} {self.height} 255 '.encode() +
                 bytearray(map(lambda x: int(min(255, max(0, x * 255))), self.buffer)))
        self._tk_root.update()
