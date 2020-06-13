import pyautogui
from pynput import keyboard
from random import randint, uniform
from listener import Listener
from search import Search


class Macro:
    def __init__(self):
        pyautogui.PAUSE = round(uniform(1.5, 2.3), 2)
        self.listener = Listener()
        self.search = Search()
        self.bglistener = None
        self.waypoints = []
        self.end = False

    def __repr__(self):
        return f"{len(self.waypoints)} waypoint(s) in macro"

    def _on_release(self, key):
        if key == keyboard.Key.esc:
            self.end = True
            self.bglistener.stop()
            print("Ending macro ...")

            return False

    def start(self):
        self.end = False
        self.bglistener = keyboard.Listener(on_release=self._on_release)
        self.bglistener.start()

        print("Macro started ...")
        while not self.end:
            for waypoint in self.waypoints:
                while True:
                    is_success = self.moveTo(waypoint)
                    if is_success:
                        break

        print("Macro ended ...")

    def show_waypoints(self):
        print(f"Current waypoints:")
        print(f"---------------------------------")
        for i in range(0, len(self.waypoints)):
            print(f"{i} : {self.waypoints[i]}")
        print(f"---------------------------------")

    def add_waypoint(self):
        region = self.listener.listen()
        if not None in region:
            image = self.search.find_image(region=region)
            if image:
                self.waypoints.append(
                    {
                        "position": (region[0], region[1]),
                        "box": (region[2], region[3]),
                        "image": image,
                    }
                )

    def moveTo(self, waypoint, random=True):
        try:
            pyautogui.PAUSE = round(uniform(1.5, 3.0), 2)
            print(pyautogui.PAUSE)
            if not random:
                pyautogui.moveTo(waypoint["position"], duration=0.2)

            if self.search.find_image(image=waypoint["image"]):
                randX = randint(
                    waypoint["position"][0],
                    waypoint["position"][0] + waypoint["box"][0],
                )
                randY = randint(
                    waypoint["position"][1],
                    waypoint["position"][1] + waypoint["box"][1],
                )

                randPosition = (randX, randY)
                pyautogui.moveTo(randPosition, duration=0.2)
                return True
            else:
                print("\033[91mWaypoint image not found ...\033[0m")
                return False
        except:
            pass
