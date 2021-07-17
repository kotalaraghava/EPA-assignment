import math


class Polygon:
    def __init__(self, edges, circumradius):
        if edges < 3:
            raise ValueError('Polygon must have at least three vertices/edges.')
        self._edges = edges
        self._circumradius = circumradius

    def __repr__(self):
        return f'Polygon(n={self._edges}, R={self._circumradius})'

    @property
    def count_vertices(self):
        return self._edges

    @property
    def count_edges(self):
        return self._edges

    @property
    def circumradius(self):
        return self._circumradius

    @property
    def interior_angle(self):
        return (self._edges - 2) * 180 / self._edges

    @property
    def side_length(self):
        return 2 * self._circumradius * math.sin(math.pi / self._edges)

    @property
    def apothem(self):
        return self._circumradius * math.cos(math.pi / self._edges)

    @property
    def area(self):
        return self._edges / 2 * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._edges * self.side_length

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


