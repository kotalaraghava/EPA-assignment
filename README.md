# Session10_Kotala raghavendra

### Objective 1 :

Create a Polygon Class:
where initializer takes in:
number of edges/vertices
circumradius
that can provide these properties:
1. edges
2. vertices
3. interior angle
4. edge length
5. apothem
6. area
7. perimeter

That has these functionalities:
1. a proper __repr__ function
2. implements equality (==) based on # vertices and circumradius (__eq__)
```python
   def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented

```
3. implements > based on number of vertices only (__gt__)
```python
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
```

### Objective 2:
Implement a Custom Polygon sequence type:
where initializer takes in:
1. number of vertices for largest polygon in the sequence
2. common circumradius for all polygons
That can provide these properties:
1. max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
That has these functionalities:
1. functions as a sequence type (__getitem__)
2. supports the len() function (__len__)
3. has a proper representation (__repr__)

## Regular Polygon
A regular strictly convex polygon is a polygon that has the following characteristics:
all interior angles are less than 180
all sides have equal length 
For a regular strictly convex polygon with:
* n edges (= n vertices)
* R circumradius
* interiorAngle = (n-2)*180/n
```python
    def interior_angle(self):
        return (self._edges - 2) * 180 / self._edges
```
* edgeLength,s = 2*R*sin(pi/n)
```python
def side_length(self):
        return 2 * self._circumradius * math.sin(math.pi / self._edges)
```
* apothem,a = R*cos(pi/n)
```python
def apothem(self):
        return self._circumradius * math.cos(math.pi / self._edges)

```
* area = 1/2*n*s*a
```python
   def area(self):
        return self._edges / 2 * self.side_length * self.apothem
```
* perimeter = n*s
```python
    def perimeter(self):
        return self._edges * self.side_length
```

max efficiency polygon = max(area:perimeter ratio)
```python
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]
```

Objective1:
```python
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
```

Objective2: 
```python
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

```
