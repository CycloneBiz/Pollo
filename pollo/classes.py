from threading import Event, Timer

class Project:
    """
    Made for Organizing Loops
    """
    def __init__(self, name, loops = []) -> None:
        self.name = name
        self.loops = loops

class Trigger:
    def __init__(self) -> None:
        pass

    def get(self):
        """If set to true in `eval`, will pass into a event. If `false` or `None`, voids event."""
        return True # This will always run

    def outputs(self):
        return None

class Loop:
    def __init__(self, check : float, trigger, event, filter = None) -> None:
        self.trigger = trigger
        self.event = event
        self.check = check
        self.filter = filter
        self.thread_event = Event()
        self.worker()

    def worker(self):
        if not self.thread_event.is_set():
            val = self.trigger.get()

            if self.filter:
                val = self.do_filter(val)

            if val:
                self.event(val)

            timer = Timer(self.check, self.worker)
            timer.name = "Pollo Thread"
            timer.start()

    def purge(self):
        self.thread_event.set()

    def do_filter(self, data):
        if type(data) == dict:
            return eval(self.filter, data)
        else:
            return eval(self.filter, {"x": data})