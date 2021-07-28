# Import Libraries
import math

class regular_polygon:
    '''
    This class is used to define regular polygons of 'n' sides and 'r' circum_radius

    ### Attributes
    --------------
    #### num_of_sides : int
            Number of edges/vertices of a regular polygon

    #### circum_radius : float
            The circum radius of the regular polygon

    #### interior_angle : float
            Interior angle of the regular polygon

    #### edge_length : float
            Length of the sides of the regular polygon

    #### apothem : float
            The length of the perpendicular line drawn from the center of the polygon to one of its sides

    #### area : float
            The total area of the regular polygon

    #### perimeter : float
            The perimeter of the regular polygon

    ### Methods
    -----------
    #### __init__(self, num_of_sides, circum_radius)
            Used to initialize the regular_polygon objects

    #### __repr__(self)
            Overwrites the default class object representation

    #### __eq__(self, other: object)
            Checks the equality of the objects passed based on the number of vertices and circum radius

    #### __gt__(self, other: object)
            Checks if one object is '>' than the other based on the number of vertices
    '''

    def __init__(self, num_of_sides: int, circum_radius: float) -> None:
        '''
        This method initializes the class object with num_of_sides and circum_radius attribute
        ### input: num_of_sides: int and circum_radius: float
        ### return: None
        '''
        if not (isinstance(num_of_sides, int) and (isinstance(circum_radius, float) or isinstance(circum_radius, int))):
            raise TypeError("num_of_sides should be an integer and circum_radius float or integer")
        if num_of_sides <= 0 and circum_radius <= 0:
            raise ValueError("num_of_sides and circum_radius should be non-zero positive integers")
        self.num_of_sides  = num_of_sides
        self.circum_radius = circum_radius

    @property
    def set_polygon_property(self)-> None:
        '''
        This method computes the interior_angle, edge_length, apothem, area and perimeter
        Set each of the above as object property
        ### input: None (access object attribute num_of_sides: int and circum_radius: float)
        ### return: None
        '''
        self.interior_angle = (self.num_of_sides - 2) * (180/self.num_of_sides)
        self.edge_length = 2 * (self.circum_radius) * math.sin(math.pi/self.num_of_sides)
        self.apothem = self.circum_radius * math.cos(math.pi/self.num_of_sides)
        self.area = 0.5 * self.num_of_sides * self.edge_length * self.apothem
        self.perimeter  = self.num_of_sides * self.edge_length

    def __repr__(self)-> str:
        '''
        This method overwrites the class object representation
        ### input - None
        ### return - String - Class object representation
        '''
        return f'This is a regular polygon with {self.num_of_sides} sides and {self.circum_radius} unit circum_radius'

    def __eq__(self, other: object) -> bool:
        '''
        This method checks if the object passed and object referenced are same
        ### input - other, object to be compared
        ### return - bool, True if the two objects are same, else False
        '''
        if not isinstance(other, regular_polygon):
            raise TypeError("The object passed is not an instance of regular_polygon class")
        if (self.num_of_sides == other.num_of_sides) and (self.circum_radius == other.circum_radius):
            print("The polygons are equal")
            return True
        else:
            print("Different polygon")
            return False

    def __gt__(self, other: object) -> bool:
        '''
        This method computes larger polygons based on the num_of_sides
        ### input - other, object to be compared
        ### return - bool, True if the self is larger, else False
        '''
        if not isinstance(other, regular_polygon):
            raise TypeError("The object passed is not an instance of regular_polygon class")
        if (self.num_of_sides > other.num_of_sides):
            print(f'{self.num_of_sides} is bigger than {other.num_of_sides}')
            return True
        else:
            print(f'{self.num_of_sides} is smaller than {other.num_of_sides}')
            return False