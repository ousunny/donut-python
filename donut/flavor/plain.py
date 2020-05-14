from macro import Macro


class Plain:
    def __init__(self):
        self.macro = Macro()

    def eat(self):
        pass

    def get_input(self):
        while True:
            print(f"[0]: Add waypoint")
            print(f"[1]: Edit waypoint")
            print(f"[2]: Delete waypoint")
            print(f"[3]: Show waypoints")
            print(f"[4]: Start donut")
            print(f"[5]: Quit")

            choice = int(input("What would you like to do: "))

            if choice == 0:
                self.macro.add_waypoint()
            elif choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                self.macro.show_waypoints()
            elif choice == 4:
                self.macro.start()
            elif choice == 5:
                break
