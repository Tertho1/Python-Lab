import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

add=arr1+arr2
print(f"Addition of two arrays: {add}")

sub=arr2-arr1
print(f"Subtraction of arr2 from arr1: {sub}")

mul=arr1*arr2
print(f"Multiplication of two arrays: {mul}")

div=arr2/arr1
print(f"Division of arr2 by arr1: {div}")

exp=np.power(arr1,2)
print(f"Exponential of arr1: {exp}")

exp = arr2**3
print(f"Exponential of arr2: {exp}")

log = np.log(arr2)
print(f"Logarithm of arr1: {log}")

expo=np.exp(arr2)
print(f"Exponential of arr2: {expo}")

mean=np.mean(arr2)
print(f"Mean of arr1: {mean}")

median=np.median(arr2)
print(f"Median of arr1: {median}")

std_deviation=np.std(arr1)
print(f"Standard deviation of arr1: {std_deviation}")

product=np.prod(arr1)
print(f"Product of arr1: {product}")

minimum=np.min(arr2)
print(f"Minimum of arr2: {minimum}")

maximum=np.max(arr2)
print(f"Maximum of arr2: {maximum}")

angles=np.array([0,np.pi/6,np.pi/4,np.pi/3,np.pi/2,np.pi])
sin_values=np.sin(angles)
print(f"Sine of angles: {np.round(sin_values,2)}")
cos_values=np.cos(angles)
print(f"Cosine of angles: {np.round(cos_values,2)}")
tan_values=np.tan(angles)
print(f"Tangent of angles: {np.round(tan_values,2)}")

ceiling=np.ceil(arr1/2)

print(f"Ceiling of arr1: {ceiling.astype(int)}")
floor=np.floor(arr1/2)
print(f"Floor of arr1: {floor}")

arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
sliced=arr3[:2,1:]
print(f"Original array: {arr3}")
print(f"Sliced array: {sliced}")

for it in arr3:
    print(it,end=",")

reshaped=np.reshape(arr3,(9,1))
print(f"Reshaped array: {reshaped}")

matrix_a=np.array([[1,2],[3,4]])
matrix_b=np.array([[5,6],[7,8]])
mat_add=np.add(matrix_a,matrix_b)
mat_add2=matrix_a+matrix_b
print(f"Addition of two matrices: {mat_add}")
print(f"Addition of two matrices: {mat_add2}")

mat_sub=np.subtract(matrix_a,matrix_b)
mat_sub2=matrix_b-matrix_a
print(f"Subtraction of two matrices: {mat_sub}")
print(f"Subtraction of two matrices: {mat_sub2}")

mat_mul=np.matmul(matrix_a,matrix_b)
mat_mul2=matrix_a.dot(matrix_b)
mat_mul3=matrix_a@matrix_b
mat_mul6=np.dot(matrix_a,matrix_b)
print(f"Multiplication of two matrices: {mat_mul}")
print(f"Multiplication of two matrices: {mat_mul2}")
print(f"Multiplication of two matrices: {mat_mul3}")
print(f"Multiplication of two matrices: {mat_mul6}")

mat_mul4=np.multiply(matrix_a,matrix_b)
mat_mul5=matrix_a*matrix_b
print(f"Multiplication of two matrices: {mat_mul4}")
print(f"Multiplication of two matrices: {mat_mul5}")

mat_div=np.divide(matrix_b,matrix_a)
mat_div2=matrix_b/matrix_a
print(f"Division of two matrices: {mat_div}")
print(f"Division of two matrices: {mat_div2}")

mat_det=np.linalg.det(matrix_a)
print(f"Determinant of matrix_a: {mat_det}")

mat_inv=np.linalg.inv(matrix_a)
print(f"Inverse of matrix_a: {mat_inv}")

mat_exp=np.exp(matrix_a)
print(f"Exponential of matrix_a: {mat_exp}")
mat_pow=np.linalg.matrix_power(matrix_a,2)
print(f"Power of matrix_a: {mat_pow}")

mat_trans=np.transpose(matrix_a)
print(f"Transpose of matrix_a: {mat_trans}")

