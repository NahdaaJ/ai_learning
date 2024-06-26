# Tensors

Tensors are the Machine Learning generalisation of scalars, vectors, matrices and other dimensions.

## Vectors

Vectors are one-dimensional tensors. They represent a point in space, with a magnitude and direction.

In machine learning, data points can be represented as vectors. For example, a data point with with $n$ features can be represented as an $n$-dimensional vector. Each element of the vector corresponds to a feature value.

### Zero Vectors

A zero vector is a vector where all the elements are zero. Can be used for initialisation, as a reference point or for indication no change.

$$
\mathbf{0} = \begin{bmatrix}
0 \\
0 \\
\vdots \\
0
\end{bmatrix}
$$

### Unit Vectors

A vector where its length is equal to one.

## Vector Formulas

### Addition and Subtraction

This is used to combine two vectors to get a new vector. Useful for combining features or data points. For example, adding noise to data to create more training examples.

$$
\mathbf{u} + \mathbf{v} = \begin{bmatrix} 
u_1 \\ 
u_2 \\ 
\vdots \\ 
u_n 
\end{bmatrix} + \begin{bmatrix} 
v_1 \\ 
v_2 \\ 
\vdots \\ 
v_n 
\end{bmatrix} = \begin{bmatrix} 
u_1 + v_1 \\ 
u_2 + v_2 \\ 
\vdots \\ 
u_n + v_n 
\end{bmatrix}
$$

### Scalar Multiplication

This scales a vector by a constant factor. Used to change the scale of data. For example, scaling features so they fit within a specific range.

$$
\lambda \mathbf{u} = \lambda \begin{bmatrix} 
u_1 \\ 
u_2 \\ 
\vdots \\ 
u_n 
\end{bmatrix} = \begin{bmatrix} 
\lambda u_1 \\ 
\lambda u_2 \\ 
\vdots \\ 
\lambda u_n 
\end{bmatrix}
$$

### Dot Product (Inner Product)

This measures the cosine of the angle between two vectors and their magnitudes. Measures similarity between two vectors. Used in algorithms like cosine similarity in recommendation systems.

$$
\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n
$$

### Cross Product (in 3D)

 This finds a vector perpendicular to two given vectors.

$$
\mathbf{u} \times \mathbf{v} = \begin{bmatrix} 
u_2 v_3 - u_3 v_2 \\ 
u_3 v_1 - u_1 v_3 \\ 
u_1 v_2 - u_2 v_1 
\end{bmatrix}
$$

$$
\mathbf{a} \times \mathbf{b} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
$$

This can be expanded using the determinant of the matrix:

**2x2**

$$
\det(\mathbf{A}) = ad - bc
$$

**3x3**

$$
\det(\mathbf{A}) = aei + bfg + cdh - ceg - bdi - afh
$$

### Unit Vectors

A unit vector in direction $\mathbf{a}$  is given by:

$$
\hat{\mathbf{a}} = \frac{\mathbf{a}}{||\mathbf{a}||}
$$

### Euclidean Distance Formula

The Euclidean distance d between two points $\mathbf{p} = [p_1, p_2]$ and $\mathbf{q} = [q_1, q_2]$  is given by:

$$
d = \sqrt{(q_1 - p_1)^2 + (q_2 - p_2)^2}
$$

### Vector Projection

The projection of a vector $\mathbf {a}$ onto vector $\mathbf {b}$ is given by:

$$
proj_\mathbf{b} \mathbf{a} = \left( \frac{\mathbf{a} \cdot \mathbf{b}}{\mathbf{b} \cdot \mathbf{b}} \right) \mathbf{b}
$$

### $L^2$ Norm/Magnitude of a Vector

This measures the length of a vector, used in machine learning for normalization. Helps in normalizing data to ensure all features have the same scale, which improves the performance of many algorithms.

$$
\|\mathbf{u}\| = \sqrt{u_1^2 + u_2^2 + \cdots + u_n^2}
$$

### $L^1$ Norm

Another common norm in ML. Varies linearly at all locations whether near or far from origin. Used whenever difference between 0 and non 0 is key.

$$
\|\mathbf{u}\|_1 = \sum_i |u_i|
$$

### Squared $L^2$ Norm

Computationally cheaper to use. Same as multiplying the vector by its transpose. Grows slowly near the origin so can’t be used if distinguishing between 0 and non-zero is important.

$$
||\mathbf{x}||^2_2 = \sum_i x^2_i =  \mathbf{x}^T\mathbf{x} 
$$

### Max Norm

AKA $L^∞$ Norm. occurs frequently in Machine Learning. Returns the absolute value of the largest-magnitude element.

$$
||\mathbf{x}||_∞ = \max_i|x_i|
$$

## Matrices

In machine learning, data points can be represented as matrices. For example, a data point with with $n$ features can be represented as an $n$-dimensional matrix. Each element of each row in a matrix corresponds to a feature value.

Operations on matrices like scaling or combining is important for normalising data, or combining data from different sources.

### Linear Transformations

Linear transformations are a way to map one vector to another in such a way that the structure of the vector is maintained. 

**Transformation Matrices**

If $A$ is a transformation matrix and $\mathbf {v}$ is a vector, the transformation is applied by multiplying A by $\mathbf {v}$:

$$
T(\mathbf{v}) = A \mathbf{v}
$$

1. **Additivity (Preserves Addition)**
If $T$ is a linear transformation, and $\mathbf {u}$ and $\mathbf {v}$ are vectors, then:
    
$$
T(\mathbf{u}+\mathbf{v}) = T(\mathbf{u})+T(\mathbf{v})
$$
    
2. **Homogeneity (Preserves Scalar Multiplication)**
If $T$ is a transformation, and $c$ is a scalar, then:
    
$$
T(c\mathbf{u}) = cT(\mathbf{u})
$$
    
### Scaling

Scaling stretches or shrinks vectors by a constant factor.

$$
T(\mathbf{v}) = k \begin{pmatrix}
x \\
y
\end{pmatrix} = \begin{pmatrix}
kx \\
ky
\end{pmatrix}
$$

### Rotation

A rotation rotates vectors by a certain angle around the origin. If we rotate a vector by an angle $\theta$ , the transformation can be represented by the following matrix:

$$
T(\mathbf{v}) = \begin{pmatrix} 
\cos \theta & -\sin \theta \\ 
\sin \theta & \cos \theta 
\end{pmatrix} \begin{pmatrix} 
x \\ 
y 
\end{pmatrix}
$$

### Reflection

Reflections flip vectors over a line or plane (2D or 3D). For example, reflecting over the x-axis:

$$
T(\mathbf{v}) = \begin{pmatrix} 
1 & 0 \\ 
0 & -1 
\end{pmatrix} \begin{pmatrix} 
x \\ 
y 
\end{pmatrix} = \begin{pmatrix} 
x \\ 
-y 
\end{pmatrix}
$$


### Identity Matrix

Multiplying any matrix by an identity matrix results in the original matrix. This property is akin to multiplying a number by 1. In machine learning, identity matrices are used in various operations such as scaling or transforming data without changing its content, applying certain types of regularization in algorithms like neural networks, or initializing weights in neural networks.

In machine learning, diagonal matrices are used in operations like scaling features or applying different weights to different features in algorithms like linear regression or regularization techniques.

$$
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{bmatrix}
$$

### Diagonal Matrix

Diagonal matrices are useful for scaling other matrices. When you multiply a matrix by a diagonal matrix, you scale each corresponding row of the original matrix by the diagonal elements of the diagonal matrix.

$$
\begin{bmatrix}
2&0&0\\
0&3&0\\
0&0&5
\end{bmatrix}
$$

## Matrix Formulas

### Matrix Multiplication

This combines two matrices to produce a new matrix. Used in neural networks to combine weights and inputs or to transform data.

$$
\mathbf{C} = \mathbf{A} \mathbf{B}, \quad c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

### Transpose of a Matrix

This flips a matrix over its diagonal, swapping rows with columns. Used in various operations, like switching between rows and columns in data or weight matrices in machine learning models.

$$
\mathbf{A}^\top = \begin{bmatrix} 
a_{11} & a_{21} & \cdots & a_{m1} \\ 
a_{12} & a_{22} & \cdots & a_{m2} \\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{1n} & a_{2n} & \cdots & a_{mn} 
\end{bmatrix}
$$

### Determinant of a Matrix

For 2x2 and 3x3 matrices. A number that helps determine if a matrix has an inverse. In machine learning, you need invertible matrices for solving certain problems, like finding exact solutions in linear regression.

**For 2x2 matrix** where:

$$
\mathbf{A} = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$


The determinent is:

$$
\det(\mathbf{A}) = ad - bc
$$

**For 3x3 matrix** where:

$$
\mathbf{A} = \begin{bmatrix} 
a & b & c \\ 
d & e & f \\ 
g & h & i 
\end{bmatrix}
$$

The determinent is:

$$
\det(\mathbf{A}) = aei + bfg + cdh - ceg - bdi - afh
$$

### Inverse of a Matrix

For square matrices 

$$
\mathbf{A} = \begin{bmatrix} 
a & b \\ 
c & d 
\end{bmatrix}
$$ 

where $\det(\mathbf{A}) \neq 0$. Finds a matrix that, when multiplied with the original, gives the identity matrix. Used in solving linear equations and inverting transformations, like reversing changes applied to data.

$$
\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \text{adj}(\mathbf{A})
$$

$$
\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \begin{bmatrix} 
d & -b \\ 
-c & a \end{bmatrix}
$$

### Solving Linear Equations Using Matrices

You can solve linear equations using matrices. Given the system of linear equations:

$$
\begin{cases}
2x + 3y = 5 \\
4x + 6y = 10
\end{cases}
$$

We can represent this system using matrix notation as: 

$$
\mathbf{Ax} = \mathbf{b}
$$

Where: 

$$
\mathbf{A} = \begin{bmatrix} 
2 & 3 \\ 
4 & 6 
\end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} 
x \\ 
y 
\end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 
5 \\ 
10 \end{bmatrix}
$$

Find the determinant of $\mathbf {A}$ to see if it can be inversed.

If $\det(\mathbf {A}) = 0$, it cannot be inversed and there are no/infinite solutions. 

If $\det(\mathbf {A}) ≠ 0$, multiply $\mathbf {b}\mathbf {A}^{-1}$ to find $\mathbf {x}$.
