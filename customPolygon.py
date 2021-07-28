# Import packages
from polygon import regular_polygon
from functools import lru_cache

class custom_polygon_iterable:
    '''
    This class creates a sequence of polygon objects

    ### Attributes
    --------------
    #### largest_num_of_sides : int
            The polygon with largest number of sides in the sequence

    #### circum_rad : float
            The common circum radius of all the polygons in the sequence

    #### area_peri_ratios : dict()
            The dictionary to store the area and perimeter as values and vertices as keys

    ### Methods
    -----------
    #### __init__(largest_num_of_sides, circum_rad)
            This is a contructor for the custom_polygon_iterable class

    #### __getitem__(vertex)
            This method implements getitem[index] for the sequence object

    #### __len__()
            This method implements in the len() function on the sequence object

    #### __repr__()
            This method overrides the default class object representation

    #### max_efficiency_polygon()
            This method computes the polygon with maximum area-perimeter ratio

    #### _poly_ratio(int, circum_rad)
            This is a static method which computes the ratio between area and perimeter of each of the polygon
    '''
    def __init__(self, largest_num_of_sides: int, circum_rad: float) -> None:
        '''
        This is a contructor for the custom_polygon_iterable class.
        #### input
            largest_num_of_sides, circum_rad
        #### return
            None
        '''
        self.largest_num_of_sides = largest_num_of_sides
        self.circum_rad = circum_rad
        self.area_peri_ratios = dict()

    def __getitem__(self, vertex: int) -> "custom_polygon_iterable._poly_ratio":
        '''
        This method implements getitem[index] for the sequence object
        #### input
            vertex: integer index
        #### return
            custom_polygon_iterable._poly_ratio(vertex)
        '''
        if not isinstance(vertex, int):
            raise TypeError("Index should be an integer")
        if vertex < 0:
            vertex = self.largest_num_of_sides + 1 + vertex
        if vertex < 0 or vertex > self.largest_num_of_sides:
            raise IndexError("Index out of bounds")
        if vertex > 2:
            return custom_polygon_iterable._poly_ratio(vertex, self.circum_rad)
        else:
            return "Not a polygon"

    def __len__(self)-> "largest_num_of_sides":
        '''
        This method implements in the len() function on the sequence object
        #### input
            None
        #### return
            largest_num_of_sides
        '''
        return self.largest_num_of_sides

    def __repr__(self)-> str:
        '''
        This method overrides the default class object representation
        #### input
            None
        #### return
            largest_num_of_sides and circum_rad
        '''
        return f'This is a polygon sequence with the largest polygon having {self.largest_num_of_sides} sides and each polygon having {self.circum_rad} unit circum_radius'

    @property
    def max_efficiency_polygon(self)-> str:
        '''
        This method computes the polygon with maximum area-perimeter ratio
        #### input
            None
        #### return
            The area-permiter ratio of the max efficient polygon is {self.area_peri_ratios[key]} with {key} vertices
        '''
        for i in range(3, self.largest_num_of_sides + 1):
            self.area_peri_ratios[i] = self.__getitem__(i)
        key = max(self.area_peri_ratios, key = self.area_peri_ratios.get)
        return f'The area-perimeter ratio of the max efficient polygon is {round(self.area_peri_ratios[key],2)} with {key} vertices'

    @staticmethod
    @lru_cache(2**10)
    def _poly_ratio(vertex: int, circum_rad: float)-> float:
        '''
        This method computes the ratio between area and perimeter of each of the polygon
        #### input
            vertex - number of sides of the polygon
            circum_rad - the circumference radius of the regular polygon
        #### return
            area/perimeter - float
        '''
        polygon = regular_polygon(vertex, circum_rad)
        polygon.set_polygon_property
        return polygon.area/polygon.perimeter

    #Converting Custom polygon sequence into to an iterable
    def __iter__(self):
        '''
        Defining a iterator method for the custom_polygon_iterable class
        #### input
            self - custom_polygon_iterable class object
        #### return
            iterator object of the custom_polygon_iterator class
        '''
        return self.custom_polygon_iterator(self)

    class custom_polygon_iterator:
        '''
        This internal class creates a iterator object for the custom_polygon_iterable class
        '''
        def __init__(self, iterable_obj):
            '''
            This is a constructor method to the custom_polygon_iterator class
            #### input
                iterable_obj - Object of the iterable class
            #### return
                None
            '''
            self._iterable_obj = iterable_obj
            self._index = 0

        def __iter__(self):
            '''
            This is a iter method for the custom_polygon_iterator class
            #### Input
                self object
            #### return
                self object
            '''
            return self

        def __next__(self):
            '''
            This is the next method of the iterator object. It returns the next element in the sequence
            #### Input
                self
            #### return
                next item in the index
            '''
            if self._index >= len(self._iterable_obj):
                raise StopIteration("Way past the index buddy!")
            else:
                item = self._iterable_obj.__getitem__(self._index)
                self._index += 1
                return item