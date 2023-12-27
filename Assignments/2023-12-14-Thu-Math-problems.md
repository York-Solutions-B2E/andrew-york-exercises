1.
Normalize [1,1]mag of a = sqrt(a1^2 + a2^2)unit of a = a1/mag(a), a2/mag(a)sqrt(1^2 + 1^2) = sqrt(2)unit(a) = [1/sqrt(2), 1/sqrt(2)] 			NB. 1/sqrt(2) is equal to sqrt(2)/2
2.
Is v3 = [3,3] linearly dependent on v1 = [3,2], v2 = [-3,1]? If so, what linear combination of v1 and v2 results in v3?Find c1 and c2 such that v1c1 + v2c2 = v33c1 - 3c2 = 3 (do vector addition with the coefficients. top elements:2c1 + c2 = 3 (bottom elements:
Divide top eq by 3c1 - c2 = 1 ( add c2 to both sidesc1 = 1 + c2 ( sub this into 2nd eq2(1 + c2) + c2 = 3 ( simplify3c2 + 2 = 3 ( sub 23c2 = 1 ( div 3c2 = 1/3Use this to get c1:c1 = 1 + 1/3c1 = 4/3(4/3)v1 + (1/3)v2 = v3

3.Given the vectors v1 = [1,2,3] and v2 = [3,2,1], create a new vector that is linearly independent from them.The cross product is linearly independent.
a	b		1	3		a2b3 - a3b22	2		a3b1 - a1b33	1		a1b2 - a2b1
v1 x v2 = [2*1 - 3*2
3*3 - 1*1
1*2 - 2*3]=
2-6
9-1
2-6=
[-4,8,-4]

To do this not in R3 is somewhat harder…

4.
Create three vectors in R3 that do not span R3
[3,2,1]
[6,4,2]
[12,8,4]
There’s really only one vector here, ergo they all lie not only on the same plane but on the same line. v2 is v1 * 2; v3 is v1 * 4

5.
What are the requirements to claim something is a subspace?
- it must contain the zero vector
- it must have closure under multiplication, i.e. any vector in the set times any scalar must also be in the set
- it must have closure under addition, i.e. for any two set vectors a,b, a+b must also be in the set

6.
Is the span of any set of vectors a valid subspace?
Yes. Any span is a region that constitutes a valid subspace (e.g. line, plane, etc)


7.Does the set of all vectors of form [a + b, a] form a subspace of R2?
Yes

8.
What does it mean to be the basis of a subspace?
A set of linearly independent vectors whose span is the subspace

9.
Create two different bases for R3
(set of 3 3D vectors whose span is R3)

S1 = [1,0,0],[0,1,0],[0,0,1]
S2: find two that are LI and take cross product

10.
Do the vectors [1,2], [2,3], [3,4] form a basis for R2?
No. Any set of more than two 2D vectors will contain redundancy for R2.

11.
Is there any set of three vectors that form a basis for R2? Why or why not?
No. Scalar manipulations of two linearly independent 2D vectors always suffice to reach any point in R2. A third vector will always be redundant unless the first two already had a dependency.

12.
If some vector w is equal to 3v, and || v || = 1.5, what is v dot w?
v dot w (ie 3v) is v1 * 3v1 + v2 * 3v2… i.e. 3v1^2 + 3v2^2… i.e. 3(v1^2 + v2^2 …)
1.5 = sqrt(v1^2 + v2^2 …) ergo 1.5^2 = 2.25 = v1^2 + v2^2 … ergo v dot w = 2.25 * 3 = 6.75

13.
Given LI vectors v, w, what is v dot (v x w)?
Since the cross product of LI vectors is orthogonal to them, and the dot product of orthogonal vectors is 0, the answer is 0

14.
What does the vector triangle inequality claim?
The magnitude of x + y (the “hypotenuse”) will always be less than || x || + || y ||

15.
What is the angle between [1,0] and [2,2]?
arccos of ||a|| ||b|| over a dot b
||a|| = 1
||b|| = sqrt(8)
a dot b = 2

theta = arccos(sqrt(8)/2) = arccos(sqrt(2))

16.
Is cross products defined in R2? No

17.
What is [1,1,1] x [-2,3,1]?

[-2,-3,5]