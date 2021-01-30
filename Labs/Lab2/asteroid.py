from Labs.Lab2.vector import Vector
from random import randint
from math import pi
from copy import deepcopy


class Asteroid:

    id = 0

    def __init__(self, circumference: float, position: Vector, velocity: Vector) -> None:
        """
        Instantiate a new asteroid.

        :param circumference: circumference of the asteroid
        :param position: the current position of the asteroid
        :param velocity: the current velocity vector of the asteroid.
        """
        self._circumference = circumference
        self._position = position
        self._velocity = velocity
        self.id = Asteroid.generate_id()

    @staticmethod
    def generate_id() -> int:
        """
        Generate a unique ID for this asteroid.
        :return: a new unique sequential ID number.
        """
        Asteroid.id = Asteroid.id + 1
        return Asteroid.id

    def __repr__(self):
        return f"Asteroid {self.id} is currently at {self.position}, moving at {self.velocity} \
metres per second. it has circumference of {self.circumference}"

    @property
    def circumference(self) -> float:
        """
        Get the circumference of an Asteroid.

        :return: the circumference
        """
        return self._circumference

    @circumference.setter
    def circumference(self, new_circumference):
        """
        Set the circumference of an asteroid.

        :param new_circumference: the new value for circumference
        :returns:
        """
        self._circumference = new_circumference

    @property
    def position(self) -> Vector:
        """
        Get the current position of an asteroid.

        :return: the current position
        """
        return self._position

    @position.setter
    def position(self, new_position) -> None:
        """
        Set the current position of an asteroid.

        :param new_position: the new value for position as a Vector(x, y, z)
        :returns
        """
        self._position = new_position

    @property
    def velocity(self) -> Vector:
        """
        Get the velocity of an asteroid.

        :return: velocity
        """
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity) -> None:
        """
        Set the velocity of an asteroid.

        :param new_velocity:
        :return:
        """
        self._velocity = new_velocity

    def move(self) -> Vector:
        """
        Modify the position using velocity and return the new position as tuple.
        :return: the asteroids position after moving.
        """
        #old_position = deepcopy(self._position)
        old_position = Vector(self._position.x, self._position.y, self._position.z)
        self.position.add(self.velocity)

        print(f"Asteroid {self.id} has moved from {old_position} to {self.position}")
        return self.position

    @staticmethod
    def generate_random_asteroid():
        """
        Instantiate a new asteroid with randomly initialized velocity, position, and radius. (inside some constraints)
        :return: the asteroid.
        """
        radius = randint(1, 4)
        circumference = 2 * pi * radius
        vel = Vector(randint(0, 5), randint(0, 5), randint(0, 5))
        pos = Vector(randint(0, 100), randint(0, 100), randint(0, 100))

        return Asteroid(circumference=circumference, position=pos, velocity=vel)
