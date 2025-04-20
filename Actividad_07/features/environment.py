# features/environment.py

from unittest.mock import MagicMock
from src.belly import Belly

def before_scenario(context, scenario):
    fake_clock = MagicMock()
    fake_clock.return_value = 10000.0
    context.current_time = fake_clock.return_value

    def advance_time(hours):
        context.current_time += (hours * 3600)
        fake_clock.return_value = context.current_time

    context.advance_time = advance_time
    context.belly = Belly(clock_service=fake_clock)
    context.exception = None
