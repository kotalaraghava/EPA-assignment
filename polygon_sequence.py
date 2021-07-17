from polygon import Polygon


class Polygons:
    def __init__(self, edges, circumradius):
        if edges < 3:
            raise ValueError('edges/vertices must be greater than 3')
        self._edges = edges
        self._circumradius = circumradius
        self._polygons = [Polygon(i, circumradius) for i in range(3, edges + 1)]

    def __len__(self):
        return self._edges - 2

    def __repr__(self):
        return f'Polygons(m={self._edges}, R={self._circumradius})'

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]


polygons = Polygons(10, 10)

print([(p, p.area/p.perimeter) for p in polygons])

print(polygons.max_efficiency_polygon)

for p in polygons[2:5]:
    print(p)

for p in polygons[::-1]:
    print(p)