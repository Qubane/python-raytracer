from time import perf_counter, sleep
from .window import Window
from .rendering import RenderThread


class Application:
    """
    Main application class
    """

    def __init__(self, **kwargs):
        # application window
        self.window: Window = Window(**kwargs)

        # rendering thread
        self.render: RenderThread = RenderThread(buffer=self.window.buffer, **kwargs)

        self.framerate: float = 1 / kwargs.get("framerate", 30)

    def run(self):
        """
        Run loop of the application
        """

        while self.window.alive:
            start = perf_counter()
            self.render.render_frame()
            self.window.update()
            end = perf_counter()
            sleep(self.framerate - (end - start))
