from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        service_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if (service_date < datetime.today().date() or self.engine_should_be_serviced()):
            return True(service_date)
        else:
            return False(service_date)
