

class InternalDurationNotSet(Exception):
    
    def __init__(self):
        super().__init__("The Duration of the Timer has not been set.")

