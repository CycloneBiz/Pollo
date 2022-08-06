from pollo import Loop, Trigger
from time import sleep

class MyTrigger(Trigger):
    def __init__(self) -> None:
        super().__init__()
        self.my_val = False

    def get(self):
        return self.my_val

    def set(self):
        self.my_val = True

trigger = MyTrigger()
my_loop = Loop(1, trigger, print)
sleep(10)
trigger.set()
