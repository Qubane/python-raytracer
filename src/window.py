import tkinter as tk


class Window:
    """
    Tkinter window class
    """

    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

        # tkinter part
        self._tk_root = tk.Tk()
        self._tk_root.title("Raytracer")
        self._tk_root.protocol("WM_DELETE_WINDOW", lambda: self._die(self._tk_root))

        self._tk_canvas = tk.Canvas(self._tk_root, width=self.width, height=self.height)
        self._tk_canvas.pack(padx=0, pady=0, expand=True)
        self._tk_image = tk.PhotoImage(width=self.width, height=self.height)
        self._tk_canvas.create_image(self.width // 2, self.height // 2, image=self._tk_image, state='normal')

        self._tk_alive: bool = True

    def _die(self, win):
        """
        When window dies
        """

        self._tk_alive = False
        win.destroy()

    @property
    def alive(self):
        return self._tk_alive

    def update(self):
        """
        Updates the window
        """

        self._tk_root.update()
