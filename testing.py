from pollo import Loop, Trigger
from time import sleep

class MyTrigger(Trigger):
    def __init__(self) -> None:
        super().__init__()
        self.my_val = 0

    def get(self):
        return {"temp": self.my_val}

    def set(self):
        self.my_val = 1

trigger = MyTrigger()
my_loop = Loop(1, trigger, print, "temp == 0")
sleep(2)
trigger.set()
