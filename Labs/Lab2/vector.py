class Vector:
    def __init__(self, x, y, z):

        self._x = x
        self._y = y
        self._z = z

    def __repr__(self):
        return f" x,y,z = {self.x},{self.y},{self.z}"

    def __str__(self):
        return (self.x, self.y, self.y).__str__()

    def return_vector_as_tuple(self):
        return self.x, self.y, self.z

    def add(self, vector):
        self.x = self.x + vector.x
        self.y = self.y + vector.y
        self.z = self.z + vector.z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, new_z):
        self._z = new_z

