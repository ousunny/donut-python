import pyautogui


class Search:
    def __init__(self):
        self.image = None

    def show(self):
        self.image.show()

    def _set_image_region(self, region):
        self.image = pyautogui.screenshot(region=(region))

    def find_image(self, region=None, image=None):
        print("Looking for image ...")

        if image:
            self.image = image
        else:
            self._set_image_region(region)

        try:
            center = pyautogui.locateCenterOnScreen(self.image, confidence=0.9)
            if center:
                print("\033[92mImage found ...\033[0m")
                return self.image
        except:
            pass

        print("Image not found ...")
        return None
