import main


class RenderThread:
    """
    Rendering thread
    """

    def __init__(self, width: int, height: int, buffer: list[float]):
        # buffer
        self.buffer = buffer
        self.width: int = width
        self.height: int = height

    def plot(self, x: int, y: int, r: float, g: float, b: float):
        """
        Plots pixel with given rgb parameters
        :param x: x pos
        :param y: y pos
        :param r: red channel (unit)
        :param g: green channel (unit)
        :param b: blue channel (unit)
        """

        self.buffer[(x + y * self.width) * 3 - 2] = r
        self.buffer[(x + y * self.width) * 3 - 1] = g
        self.buffer[(x + y * self.width) * 3] = b

    def render_frame(self):
        """
        Renders the frame
        """

        for y in range(self.height):
            for x in range(self.width):
                self.plot(x, y, x / self.width, 0, y / self.height)
