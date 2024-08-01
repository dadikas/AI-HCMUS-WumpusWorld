from enum import Enum

class ActionAgent(Enum):
    Moveforward = "M"
    TurnLeft = "L"
    TurnRight = "R"
    Grab = "G"
    Shoot = "S"
    Climb = "C"
    Heal = "H"

    
    def __str__(self):
        return self.value