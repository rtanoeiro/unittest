"""Challenge for section 5"""

class Car:

    def __init__(self) -> None:
        self._speed = 0
        self._start_car = False

    def start_car(self):
        """
        This function will start the car
        """
        self._start_car = True

    def turn_off_car(self):
        """
        This function will stop the car
        """
        self._start_car = False

    def add_speed(self):
        """
        This function will add speed to the car
        """
        self._speed +=5

    def remove_speed(self):
        """
        This function will remove speed to the car, up until speed reaches 0
        """
        if self._speed == 0:
            self._speed = 0
        else:
            self._speed -= 5

    def stop(self):
        """
        This function will stop the car
        """
        self._speed = 0

    def current_speed(self):
        """
        This function will return the current speed of the car
        """
        return self._speed

    def current_status(self):
        """
        This function will return the current status of the car (Turned On, Turned Off)
        """
        return self._start_car
