1. What is a linear transformation?
    A function operating on vectors where:
        1. T(v1 + v2) = T(v1) + T(v2)
        2. T(cv) = cT(v)
    In a plane:
        Origin does not move
        Any straight lines imposable on plane remain straight

2. Is the following a LT? T[x, y] = [x + y, y]
    T(v + w) must = T(v) + T(w)
        T([x1 + x2, y1 + y2]) =         [x1+x2+y1+y2, y1+y2]
        [x1 + y1, y1] + [x2 + y2, y2] = [x1+x2+y1+y2, y1+y2]
           
    
    T(cv) must = cT(v)
        T(c[x, y]) = T(cx, cy) =    [cx + cy, cy]
        cT([x, y]) = c(x + y, y) =  [cx + cy, cy]

    Yes

3. Consider the linear transformation T(v) = Av where A =     
    [-1 0]
    [-1 0]
    What does this transformation do to a vector in R2?
    T[x,y] = (-x + 0y, -x + 0y)
    Replaces both components with the inverse of x.
    Visually it would flip the vector about the y axis and then set y = x.

4. Create a matrix that corresponds with rotating a vector in R2 90 degrees then halving the x
    Rotate 90 (CW): 
    [0  1]  
    [-1 0]  
    halve x:
    [0.5 0]
    [0   1]
    =
    [0  0.5]
    [-1   0]

5. Inverse of D = 
[4 7]
[2 6]

D^-1 = 1/(4*6 - 7*2) i.e. 1/10 *
[6 -7]
[-2 4] = 

[.6 -.7]
[-.2 .4]

6. What is the inverse of the 7x7 identity matrix?
    The inverse of every identity matrix is itself.

7. Determinant of E = 
[3 2 3]
[4 3 4]
[5 4 5]
    Det. of 2x2: ad-bc
    Det(E)  = 3(det(3 4 _ 4 5) - 2(det(4 4 _ 5 5)) + 3(det(4 3 _ 5 4)))
            = 3(-1) - 2(0) + 3(1)
            = -3 + 3
            = 0

8. Create a matrix that is not invertible.
    [1 2 3 4]
    [5 6 7 8]

    [6 10 6]
    [5  2 5]
    [3  1 3]