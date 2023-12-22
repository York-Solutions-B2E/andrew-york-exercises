1. Calculate the eigenvalues and eigenvectors of the following matrix:
   A = [2 2]
       [1 3]

    det(λI_2-A) = 0
    det([λ-2 -2]) = 0
        [-1 λ-3]

    det = ad-bc
    (λ-2)(λ-3) - 2 = 0

    λ^2 - 3λ -2λ + 6 - 2 = 0
    λ^2 - 5λ + 4 = 0

    Mults to 4, Sums to -5: -1 and -4

    (λ-4)(λ-1) = 0
    λ = 4 or 1

    Eigenvectors: 4
    0vector = (λI_n-A)v
    E_λ = N(λI_n-A)
    E_4 = N([4 0] - [2 2]) = N([2  -2])
            [0 4]   [1 3]      [-1  1]

    rref =  [1 -1][v1] = [0]
            [0  0][v2]   [0]
    v2 = t
    v1 - t = 0
    v1 = t

    E_4 = {[v1,v2] = t[1,1]}
    E_4 = span[1,1]

    Eigenvectors: 1
    E_1 = N([1 0] - [2 2]) = N([-1 -2])
            [0 1]   [1 3]      [-1 -2]

    rref =  [1 2][v1] = [0]
            [0 0][v2] = [0]
    v2 = t
    v1 + 2t = 0
    v1 = -2t
    
    E_1 = {[v1,v2] = t[-2,1]}
    E_1 = span([-2,1])

2. Calculate eigenvalues and eigenvectors of 
A = [2 -3 0]    λI_3 =  [λ 0 0]   
    [2 -5 0]            [0 λ 0]
    [0  0 3]            [0 0 λ]

    λI_3 - A = B =  
    [λ-2 -3   0]
    [-2 λ+5   0]
    [0    0 λ-3]
    
    a(ei-fh) - b(di-fg) + c(dh-eg) = (λ+4)(λ-1)(λ-3)
    λ = -4 or 1 or 3

    Vector at λ = -4:
    A - λI:
    [6 -3 0]    6x-3y = 0
    [2 -1 0]    2x-y = 0
    [0  0 7]    7z = 0
    rref
    [1 -1/2 0]  x-1/2y = 0      [1]
    [0 0 0]     x = 1/2y        [2]
    [0 0 1]     z = 0           [0]

    Vector at 1:
    A - λI = 
    [1 -3 0]   
    [2 -6 0]   
    [0  0 2]   
    rref
    [1 -3 0]    x-3y = 0 x = 3y [3]
    [0  0 0]                    [1]
    [0  0 1]    z = 0           [0]

    Vector at 3:
    A - λI = 
    [-1 -3 0]
    [ 2 -8 0]
    [ 0  0 0]
    rref
    [1 0 0]     x = 0   [0]
    [0 1 0]     y = 0   [0]
    [0 0 0]     z = t   [1]

3. If a 3x3 matrix has two eigenvalues, how many eigenvectors does it have?
    Infinite. However, it has at most two linearly independent eigenvectors. If the two eigenvalues are equal, it has one


4. The matrix has at least one eigenvalue that is 2. Find a basis for the corresponding eigenspace.
[4 -1 6] 
[2  1 6]
[2 -1 8]

    For eigenvalue 2:
    A - λI = 
    [2 -1 6]
    [2 -1 6]
    [2 -1 6]
    rref:
    [2 -1 6]  2x - y + 6z = 0
    [0  0 0]  
    [0  0 0]                   

    Calling y 1 and z 0
    2x - 1 + 0 = 0
    2x = 1
    x = 1/2

    Calling z 1 and y 0
    2x - 0 + 6 = 0
    2x = -6
    x = -3

    E_2 = {[1 2 0], [-3 0 1]}

5. A matrix has an eigenvalue of 0. Is that matrix invertible?
    No. det(A - λI) = 0. If λ = 0, then det(A) = 0, making A singular. Singular matrices are non-invertible.