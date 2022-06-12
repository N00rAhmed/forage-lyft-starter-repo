from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        current_date = self.last_service_date.replace(year = self.last_service_date.year + 2)
        if (current_date < datetime.today().date() or self.engine_should_be_serviced()):
            return True(current_date)
        else:
            return False(current_date)
