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
