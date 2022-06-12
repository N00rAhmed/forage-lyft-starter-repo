from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light = warning_light_is_on

        if self.warning_light:
            return True
        else:
            return False
