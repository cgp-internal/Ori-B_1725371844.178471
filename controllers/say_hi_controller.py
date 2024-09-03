from services.greeting_service import get_greeting

class SayHiController:
    def __init__(self):
        pass

    def say_hi(self, name: str = 'World') -> str:
        return get_greeting(name)

say_hi_controller = SayHiController()