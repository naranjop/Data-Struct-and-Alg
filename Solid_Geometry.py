# Geometry classes and methods for getting information about the relationship
# between spheres, cubes, and cylinders.

import math

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z 
    
    # create a string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

    # get distance to another Point object
    def distance (self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
  
    # test for equality between two points
    def __eq__ (self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))


class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.center = Point(x,y,z)
        self.radius = radius
  
    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return 'Center: ' + str(self.center) + ', Radius: ' + str(self.radius)
  
    # compute surface area of Sphere, returns a floating point number
    def area (self):
        return 4 * math.pi * self.radius**2
    
    # compute volume of a Sphere, returns a floating point number
    def volume (self):
        return 4/3 * math.pi * self.radius**3
  
    # determines if a Point is strictly inside the Sphere, p is Point object, returns a Boolean
    def is_inside_point (self, p):
        return self.center.distance(p) < self.radius
  
    # determine if another Sphere is strictly inside this Sphere, other is a Sphere object, returns a Boolean
    def is_inside_sphere (self, other):
        dist_centers = self.center.distance (other.center)
        return (dist_centers + other.radius) < self.radius
    
    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are inside the Sphere
    # a_cube is a Cube object, returns a Boolean
    def is_inside_cube (self, a_cube):
        for i in a_cube.corners():
            if not self.is_inside_point(i):
                return False
        return True
            
  
    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object, returns a Boolean
    def is_inside_cyl (self, a_cyl):
        for i in a_cyl.corners_of_bases():
            if not self.is_inside_point(i):
                return False
        return True
  
    # determine if another Sphere intersects this Sphere
    # there is a non-zero volume of intersection
    # other is a Sphere object, returns a Boolean
    def does_intersect_sphere (self, other):
        #tol= 1.0 e -6
        #dist_centers = self.center.distance(other.center)
        #radius_dif = abs(self.radius - other.radius)
        #is_inside = ((dist_centers + other.radius) < self.radius) or ((dist_centers + self.radius) < other.radius) 
        #is_outside = dist_centers > (self.radius + other.radius)
        #is_just_touching = abs(dist_centers - (self.radius + other.radius)) < tol or (dist_centers < tol and radius_dif < tol) # juuuuuuuust touching, is this right?
        #return (not is_inside) and (not is_outside) and (not is_just_touching)
        small = -1
        if self.radius > other.radius:
            small = other.radius
            big = self.radius
        elif other.radius > self.radius:
            small = self.radius
            big = other.radius
        if small == -1:
            if self.center == other.center: # does this already use the equality function for pts defined above?
                return False
            else:
                small = self.radius
                big = other.radius  # could be self or other as radii are equal
        dist_centers = self.center.distance(other.center)
        # To be completely inside or intersecting spheres must satisfy following condition
        condition = dist_centers < self.radius + other.radius
        # To ensure sphere is not completely inside
        not_compl_inside = dist_centers + small > big
        if condition and not_compl_inside:
            return True
        else:
            return False

        
    # determine if a Cube intersects this Sphere
    # there is a non-zero volume of intersection
    # there is at least one corner of the Cube in the Sphere
    # a_cube is a Cube object, returns a Boolean
    def does_intersect_cube (self, a_cube):
        number = 0
        for corner in a_cube.corners():
            if corner.distance(self.center) < self.radius:
                number += 1
        if number != 0 and number != 8:
            return True
        else:
            return False      #check function
  
    # return the largest Cube object that is circumscribed by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        cube_side = (self.radius * 2) / math.sqrt(3)
        return Cube(side = cube_side)

    def plane_points(self):
        north = Point(self.center.x, self.center.y, self.center.z + self.radius)
        south = Point(self.center.x, self.center.y, self.center.z - self.radius)
        east = Point(self.center.x + self.radius, self.center.y, self.center.z)
        west = Point(self.center.x - self.radius, self.center.y, self.center.z)
        top = Point(self.center.x, self.center.y + self.radius, self.center.z)
        bottom = Point(self.center.x, self.center.y - self.radius, self.center.z)
        return (north, south, east, west, top, bottom)


class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.center = Point(x,y,z)
        self.side = side

    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self):
        return 'Center: ' + str(self.center) + ', Side: ' + str(self.side)
  
    # compute the total surface area of Cube (all 6 sides), returns a floating point number
    def area (self):
        return 6 * self.side**2
  
    # compute volume of a Cube, returns a floating point number
    def volume (self):
        return self.side**3
  
    # determines if a Point is strictly inside this Cube
    # p is a point object, returns a Boolean
    def is_inside_point (self, p):
        x_values = []
        y_values = []
        z_values = []
        for corner in self.corners():
            x_values.append(corner.x)
            y_values.append(corner.y)
            z_values.append(corner.z)
        max_x = max(x_values)
        min_x = min(x_values)
        max_y = max(y_values)
        min_y = min(y_values)
        max_z = max(z_values)
        min_z = min(z_values)
        return max_x > p.x > min_x and max_y > p.y > min_y and max_z > p.z > min_z

  
    # determine if a Sphere is strictly inside this Cube or
    # a_sphere is a Sphere object, returns a Boolean
    def is_inside_sphere (self, a_sphere):
        for i in a_sphere.plane_points():
            if not self.is_inside_point(i):
                return False
        return True

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object, returns a Boolean
    def is_inside_cube (self, other):
        for i in other.corners():
            if not self.is_inside_point(i):
                return False
        return True
  
    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object, returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        for i in a_cyl.corners_of_bases():
            if not self.is_inside_point(i):
                return False
        return True
  
    # determine if another Cube intersects this Cube
    # there is a non-zero volume of intersection
    # there is at least one vertex of the other Cube in this Cube
    # other is a Cube object, returns a Boolean
    def does_intersect_cube (self, other):
        pass
        #

        
    # determine the volume of intersection if this Cube 
    # intersects with another Cube, other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        return -1
        #
  
    # return the largest Sphere object that is inscribed by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        sphere_radius = self.side / 2
        return Sphere(radius = sphere_radius)
        
    def corners(self):
        corner_1 = Point(self.center.x + self.side / 2, self.center.y + self.side / 2, self.center.z + self.side / 2)
        corner_2 = Point(corner_1.x - self.side, corner_1.y, corner_1.z)
        corner_3 = Point(corner_2.x, corner_2.y - self.side, corner_2.z)
        corner_4 = Point(corner_3.x + self.side, corner_3.y, corner_3.z)
        corner_5 = Point(corner_4.x, corner_4.y, corner_4.z - self.side)
        corner_6 = Point(corner_5.x - self.side, corner_5.y, corner_5.z)
        corner_7 = Point(corner_6.x, corner_6.y + self.side, corner_6.z)
        corner_8 = Point(corner_7.x + self.side, corner_7.y, corner_7.z)
        return (corner_1, corner_2, corner_3, corner_4, corner_5, corner_6, corner_7, corner_8)


class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.center = Point(x,y,z)
        self.radius = radius
        self.height = height
    
    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return 'Center: ' + str(self.center) + ', Radius: ' + str(self.radius) + ', Height: ' + str(self.height)
    
    # compute surface area of Cylinder, returns a floating point number
    def area (self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius**2
    
    # compute volume of a Cylinder, returns a floating point number
    def volume (self):
        return math.pi * self.radius**2 * self.height
    
    # determine if a Point is strictly inside this Cylinder HEEELP TO UNDERSTAND THISSSSSSSSSSSSSSSSSSSSSSSSS
    # p is a Point object, returns a Boolean
    def is_inside_point (self, p):
        top = self.centers_of_bases()[0]
        bottom = self.centers_of_bases()[1]
        centered_point = Point(p.x, self.center.y, p.z)    
        
        # checks the y-value first then checks the x and z values while ignoring the y value
        return (top.y > p.y) and (p.y > bottom.y) and (self.center.distance(centered_point) > self.radius)
    
    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object, returns a Boolean
    def is_inside_sphere (self, a_sphere):
        for i in a_sphere.plane_points():
            if not self.is_inside_point(i):
                return False
        return True
    
    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are in the Cylinder
    # a_cube is a Cube object, returns a Boolean
    def is_inside_cube (self, a_cube):
        for i in a_cube.corners():
            if not self.is_inside_point(i):
                return False
        return True
    
    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object, returns a Boolean
    def is_inside_cylinder (self, other):
        for i in other.corners_of_bases():
            if not self.is_inside_point(i):
                return False
        return True
    
    # determine if another Cylinder intersects this Cylinder
    # there is a non-zero volume of intersection
    # other is a Cylinder object, returns a Boolean
    def does_intersect_cylinder (self, other):
         top1 = self.centers_of_base()[0].z
         bot1 = self.centers_of_base()[1].z
         top2 = other.centers_of_base()[0].z
         bot2 = other.centers_of_base()[1].z
         # Case1
         height_req_case1 = (top1 > bot2 and bot1 > top2) or (top2 > bot1\
                            and bot2 < top1)
         if self.sphere_intersect() and height_req_case1:
             return True
         # Case2
         planar_case2 = self.radius + other.radius > self.center.distance(other)
         if bot2 < top1 < top2:
             return planar_case2 and bot1 < bot2
         elif bot1 < top2 < top1:
             return planar_case2 and bot2 < bot1
         else:
             return False

        
    def centers_of_bases(self):
        # returns a point object for the center points of each base
        top = Point(self.center.x, self.center.y, self.center.z + self.height/2)
        bottom = Point(self.center.x, self.center.y, self.center.z - self.height/2)
        return (top, bottom)

    def corners_of_bases(self):
        # calculates 4 different points on the each base circle, and returns 8 different point objects
        top_center = self.centers_of_bases()[0]
        bottom_center = self.centers_of_bases()[1]

        top_east = Point(top_center.x + self.radius, top_center.y, top_center.z)
        top_west = Point(top_center.x - self.radius, top_center.y, top_center.z)
        top_north = Point(top_center.x, top_center.y + self.radius, top_center.z)
        top_south = Point(top_center.x, top_center.y - self.radius, top_center.z)
        bottom_east = Point(bottom_center.x + self.radius, bottom_center.y, bottom_center.z)
        bottom_west = Point(bottom_center.x - self.radius, bottom_center.y, bottom_center.z)
        bottom_north = Point(bottom_center.x, bottom_center.y + self.radius, bottom_center.z)
        bottom_south = Point(bottom_center.x, bottom_center.y - self.radius, bottom_center.z)
        return (top_east ,top_west, top_north, top_south, bottom_east, bottom_west, bottom_north, bottom_south)


    def sphere_intersect(self, other):
        small = -1
        if self.radius > other.radius:
            small = other.radius
            big = self.radius
        elif other.radius > self.radius:
            small = self.radius
            big = other.radius
        if small == -1:
            if self.center == other.center: # does this already use the equality function for pts defined above?
                return False
            else:
                small = self.radius
                big = other.radius  # could be self or other as radii are equal
        dist_centers = self.center.distance(other.center)
        # To be completely inside or intersecting spheres must satisfy following condition
        condition = dist_centers < self.radius + other.radius
        # To ensure sphere is not completely inside
        not_compl_inside = dist_centers + small > big
        if condition and not_compl_inside:
            return True
        else:
            return False


def read_input():
    # read data from standard input
    memory0 = input()
    return list(map(float, memory0.strip().split()))
    

def main():
    
    def testing():

        # Object creations:
        origin = Point(0.0, 0.0, 0.0)
        p = Point(-3.0, 2.0, 1.0)
        q = Point(2.0, -1.0, 3.0)
        sphereA = Sphere(2.0, 1.0, 3.0, 4.0)
        sphereB = Sphere(-1.0, -2.0, -3.0, 5.0)
        cubeA = Cube(2.0, 1.0, -3.0, 4.0)
        cubeB = Cube(3.0, 2.0, -4.0, 3.0)
        cylA = Cylinder(-2.0, 1.0, -3.0, 5.0, 4.0)
        cylB = Cylinder(1.0, 5.0, 3.0, 4.0, 2.0)

        
        # Tests required by HackerRank                                      # Expected Results
        print('0:', origin.distance(p) > origin.distance(q))         
        print()
        print('1:', sphereA.is_inside_point(p))                             # False
        print('2:', sphereA.is_inside_sphere(sphereB))                      # False
        print('3:', sphereA.is_inside_cube(cubeA))                          # False
        print('4:', sphereA.is_inside_cyl(cylA))                            # False
        print('5:', sphereB.does_intersect_sphere(sphereA))                 # True
        print('6: FIXME!', sphereB.does_intersect_cube(cubeB))                   # True  - 
        print('7:', sphereA.circumscribe_cube().volume() > cylA.volume())   # False 
        print()
        print('8:', cubeA.is_inside_point(p))                               # False
        print('9:', cubeA.is_inside_sphere(sphereA))                        # False
        print('10:', cubeA.is_inside_cube(cubeB))                           # False
        print('11:', cubeA.is_inside_cylinder(cylA))                        # False
        print('12: FIXME!', cubeA.does_intersect_cube(cubeB))                    # True  - 
        print('13: FIXME!', cubeA.intersection_volume(cubeB) > sphereA.volume()) # False - 
        print('14:', cubeA.inscribe_sphere().area() > cylA.area())          # False
        print()
        print('15:', cylA.is_inside_point(p))                               # False
        print('16:', cylA.is_inside_sphere(sphereA))                        # False
        print('17:', cylA.is_inside_cube(cubeB))                            # False
        print('18:', cylA.is_inside_cylinder(cylB))                         # False
        print('19: FIXME!', cylA.does_intersect_cylinder(cylB))                  # False - 
        
    testing()

    '''
    # read the coordinates of the first Point p
    memo1 = read_input()
    # create a Point object 
    p = Point(memo1[0], memo1[1], memo1[2])
    # read the coordinates of the second Point q
    memo2 = read_input()
    # create a Point object 
    q = Point(memo2[0], memo2[1], memo2[2])
    # read the coordinates of the center and radius of sphereA
    memo3 = read_input()
    # create a Sphere object 
    sphereA = Sphere(memo3[0], memo3[1], memo3[2], memo3[3])
    # read the coordinates of the center and radius of sphereB
    memo4 = read_input()
    # create a Sphere object
    sphereB = Sphere(memo4[0], memo4[1], memo4[2], memo4[3])
    # read the coordinates of the center and side of cubeA
    memo5 = read_input()
    # create a Cube object 
    cubeA = Cube(memo5[0], memo5[1], memo5[2], memo5[3])
    # read the coordinates of the center and side of cubeB
    memo6 = read_input()
    # create a Cube object 
    cubeB = Cube(memo6[0], memo6[1], memo6[2], memo6[3])
    # read the coordinates of the center, radius and height of cylA
    memo7 = read_input()
    # create a Cylinder object 
    cylA = Cylinder(memo7[0], memo7[1], memo7[2], memo7[3], memo7[4])
    # read the coordinates of the center, radius and height of cylB
    memo8 = read_input()
    # create a Cylinder object
    cylB = Cylinder(memo8[0], memo8[1], memo8[2], memo8[3], memo8[4])
    '''

    '''
    print(p)
    print(q)
    print(sphereA)
    print(sphereB)
    print(cubeA)
    print(cubeB)
    print(cylA)
    print(cylB)
    '''

    '''
    # print if the distance of p from the origin is greater 
    # than the distance of q from the origin
    origin = Point(0.0, 0.0, 0.0)
    result0 = 'is' if origin.distance(p) > origin.distance(q) else 'is not'
    print('Distance of Point p from the origin ' + result0 + ' greater than the distance of Point q from the origin')
    print()

    # print if Point p is inside sphereA
    result1 = 'is' if sphereA.is_inside_point(p) else 'is not'
    print('Point p ' + result1 + ' inside sphereA')
    # print if sphereB is inside sphereA
    result2 = 'is' if sphereA.is_inside_sphere(sphereB) else 'is not'
    print('sphereB ' + result2 + ' inside sphereA')
    # print if cubeA is inside sphereA
    result3 = 'is' if sphereA.is_inside_cube(cubeA) else 'is not'
    print('cubeA ' + result3 + ' inside sphereA')
    # print if cylA is inside sphereA
    result4 = 'is' if sphereA.is_inside_cyl(cylA) else 'is not'
    print('cylA ' + result4 + ' inside sphereA')
    # print if sphereA intersects with sphereB
    result5 = 'does' if sphereB.does_intersect_sphere(sphereA) else 'does not'
    print('sphereA ' + result5 + ' intersect sphereB')
    # print if cubeB intersects with sphereB
    result6 = 'does' if sphereB.does_intersect_cube(cubeB) else 'does not'
    print('!!! FIXME !!! <<<cubeB ' + result6 + ' intersect sphereB')
    # print if the volume of the largest Cube that is circumscribed 
    # by sphereA is greater than the volume of cylA
    result7 = 'is' if sphereA.circumscribe_cube().volume() > cylA.volume() else 'is not'
    print('Volume of the largest Cube that is circumscribed by sphereA ' + result7 + ' greater than the volume of cylA')
    print()

    # print if Point p is inside cubeA
    result8 = 'is' if cubeA.is_inside_point(p) else 'is not'
    print('Point p ' + result8 + ' inside cubeA')
    # print if sphereA is inside cubeA
    result9 = 'is' if cubeA.is_inside_sphere(sphereA) else 'is not'
    print('sphereA ' + result9 + ' inside cubeA')
    # print if cubeB is inside cubeA
    result10 = 'is' if cubeA.is_inside_cube(cubeB) else 'is not'
    print('cubeB ' + result10 + ' inside cubeA')
    # print if cylA is inside cubeA
    result11 = 'is' if cubeA.is_inside_cylinder(cylA) else 'is not'
    print('cylA ' + result11 + ' inside cubeA')
    # print if cubeA intersects with cubeB
    result12 = 'does' if cubeB.does_intersect_cube(cubeA) else 'does not'
    print('!!! FIXME !!! <<<cubeA ' + result12 + ' intersect cubeB')
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    result13 = 'is' if cubeA.intersection_volume(cubeB) > sphereA.volume() else 'is not'
    print('!!! FIXME !!! <<<Intersection volume of cubeA and cubeB ' + result13 + ' greater than the volume of sphereA')
    # print if the surface area of the largest Sphere object inscribed 
    # by cubeA is greater than the surface area of cylA
    result14 = 'is' if cubeA.inscribe_sphere().area() > cylA.area() else 'is not'
    print('Surface area of the largest Sphere object inscribed by cubeA ' + result14 + ' greater than the surface area of cylA')
    print()

    # print if Point p is inside cylA
    result15 = 'is' if cylA.is_inside_point(p) else 'is not'
    print('Point p ' + result15 + ' inside cylA')
    # print if sphereA is inside cylA
    result16 = 'is' if cylA.is_inside_sphere(sphereA) else 'is not'
    print('sphereA ' + result16 + ' inside cylA')
    # print if cubeA is inside cylA
    result17 = 'is' if cylA.is_inside_cube(cubeB) else 'is not'
    print('cubeA ' + result17 + ' inside cylA')
    # print if cylB is inside cylA
    result18 = 'is' if cylA.is_inside_cylinder(cylB) else 'is not'
    print('cylB ' + result18 + ' inside cylA')
    # print if cylB intersects with cylA
    result19 = 'does' if cylA.does_intersect_cylinder(cylB) else 'does not'
    print('!!! FIXME !!! <<<cylB ' + result19 + ' intersect cylA')
    '''
    pass

if __name__ == "__main__":
    main()
