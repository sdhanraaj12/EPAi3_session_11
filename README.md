# EPAi3 Session 11 Assignment 
## Iterators and Iterables 1
#### Goal 1: Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").
 

#### Goal 2:Refactor the `Polygons` (sequence) type, into an **iterable**. It should be make sure that the elements in the iterator are computed lazily - i.e. it can no longer use a list as an underlying storage mechanism for polygons.

#### implement both an iterable and an iterator

#### custom_polygon_iterable :
+ This class creates a iterable of polygon objects. It has the following attributes and methods

    ##### Attributes
    --------------
    * largest_num_of_sides : int
        - The polygon with largest number of sides in the sequence
    * circum_rad : float
        - The common circum radius of all the polygons in the sequence
    * area_peri_ratios : dict()
        - The dictionary to store the area and perimeter as values and vertices as keys

    ##### Methods
    -----------
    * __init__ (largest_num_of_sides, circum_rad)
        - This is a contructor for the custom_polygon_sequence class
        - The method takes largest_num_of_sides, circum_rad stores them as attribute to the class object
        - input - largest_num_of_sides: int, circum_rad: float
        - return - None
    * __iter__ ()
        - Defining a iterator method for the custom_polygon_iterable class
        - input - self - custom_polygon_iterable class object
        - return - iterator object of the custom_polygon_iterator class
    * __Class custom_polygon_iterator__
        - This internal class creates a iterator object for the custom_polygon_iterable class
        ##### Methods
        --------------
        * __init__ (self, iterable_obj)
            - This is a constructor method to the custom_polygon_iterator class
            - input - iterable_obj - Object of the iterable class
            - return - None
        * __iter__ ()
            - This is a iter method for the custom_polygon_iterator class
            - input - self object
            - return - self object
        * __next__ ()
            - This is the next method of the iterator object. It returns the next element in the sequence
            - input - self
            - return - next item in the index
    * __getitem__ (vertex)
        - This method implements getitem[index] for the sequence object, based on the vertex argument passed, the corresponding polygon object's  
        - input - vertex: integer index
        - return - custom_polygon_sequence._poly_ratio(vertex)
    * __len__ ()
        - This method implements in the len() function on the sequence object
        - input - sequence object
        - return - length of the sequence object integer
    * __repr__ ()
        - This method overrides the default class object representation to 'This is a polygon sequence with the largest polygon having {self.largest_num_of_sides} sides and each polygon having {self.circum_rad} unit circum_radius'
    * __max_efficiency_polygon__ ()
        - This method computes the polygon with maximum area-perimeter ratio
        - input - None
        - return - The area-permiter ratio of the max efficient polygon is {self.area_peri_ratios[key]} with {key} vertices
    * ___poly_ratio__ (int, circum_rad)
        - This is a static method which computes the ratio between area and perimeter of each of the polygon
        - input - vertex - number of sides of the polygon and circum_rad - the circumference radius of the regular polygon
        - return - area/perimeter - float

________________________________________________________________________________________________________________________________________________

#### __regular_polygon__ :
+ This class is used to define regular polygons of 'n' sides and 'r' circum_radius. They have the below attributes and methods defined. Additionally dunder functions __eq__, __gt__ and __repr__ have been overwritten
    
    ##### Attributes
    --------------
    * num_of_sides : int
        - Number of edges/vertices of a regular polygon
    * circum_radius : float
        - The circum radius of the regular polygo
    * interior_angle : float
        - Interior angle of the regular polygon
    * edge_length : float
        - Length of the sides of the regular polygon
    * apothem : float
        - The length of the perpendicular line drawn from the center of the polygon to one of its sides
    * area : float
        - The total area of the regular polygon
    * perimeter : float
        - The perimeter of the regular polygon
    
    ##### Methods
    --------------
    * __init__ (self, num_of_sides, circum_radius)
        - Used to initialize the regular_polygon objects, with the num_of_sides and circum_radius parameters passed.
        - input: num_of_sides: int and circum_radius: float
        - return: None
    * __set_polygon_property__ ()
        - This method computes the interior_angle, edge_length, apothem, area and perimeter
        - Set each of the above as object property
        - input: None (access object attribute num_of_sides: int and circum_radius: float)
        - return: None
    * __repr__ (self)
        - Overwrites the default class object representation to 'This is a regular polygon with {self.num_of_sides} sides and {self.circum_radius} unit circum_radius'
        - input - None
        - return - String - Class object representation
    * __eq__ (self, other: object)
        - Checks the equality of the objects passed based on the number of vertices and circum radius
        - input - other, object to be compared
        - return - bool, True if the two objects are same, else False
    * __gt__ (self, other: object)
        - Checks if one object is '>' than the other based on the number of vertices
        - This method computes larger polygons based on the num_of_sides
        - input - other, object to be compared
        - return - bool, True if the self is larger, else False
__________________________________________________________________________________________________________________
