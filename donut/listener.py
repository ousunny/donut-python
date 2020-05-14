from pynput import keyboard, mouse


class Listener:
    def __init__(self):
        self._listener = None
        self._mouse = mouse.Controller()
        self.region = [None, None, None, None]
        self.record = False

    def _start(self):
        print("Starting recording...")
        print("Press q to set a point ...")
        print("Press esc to stop recording ...")

        with keyboard.Listener(on_release=self._on_release) as self._listener:
            self._listener.join()

    def _on_release(self, key):
        try:
            if key.char == "q":
                x, y = self._mouse.position
                if not self.record:
                    self.region[0] = x
                    self.region[1] = y
                    self.record = True
                    print(f"Top Left set to ({x}, {y})")
                else:
                    self.region[2] = x
                    self.region[3] = y
                    print(f"Bottom Right set to ({x}, {y})")
                    self.record = False
        except AttributeError:
            pass

        if key == keyboard.Key.esc:
            print("Failed to add waypoint ...")
            return False

        if not None in self.region and not self.record:
            self.region[2] = abs(self.region[2] - self.region[0])
            self.region[3] = abs(self.region[3] - self.region[1])
            print("Ending recording...")
            return False

    def listen(self):
        self.region = [None, None, None, None]
        self.record = False

        self._start()

        return self.region
