import numpy as np

# Matrisleri tanımla
A = np.array([
    [9, 7, 1],
    [8, 3, 6],
    [5, 10, 4],
    [2, 1, 15]
])

B = np.array([
    [2, 7],
    [6, 5],
    [3, 11]
])

C = np.array([
    [8, 1],
    [3, 20],
    [17, 9]
])

D = np.array([-1, 1, 2])

# (a) Matrix multiplication A x B
AxB = np.matmul(A, B)
print("A x B (Matrix multiplication):")
print(AxB)

# (b) Transpose of C
C_T = np.transpose(C)
print("\nC^T (Transpose of C):")
print(C_T)

# (c) Element-wise multiplication B ∘ C
B_elementwise_C = B * C
print("\nB ∘ C (Element-wise multiplication):")
print(B_elementwise_C)

# (d) 3B - 5C
result_3B_5C = 3 * B - 5 * C
print("\n3B - 5C:")
print(result_3B_5C)

# (e) C + D^T
# D'yi yayın için bir sütun vektörü olacak şekilde yeniden şekillendirin
D_T = D.reshape(-1, 1)
C_plus_D_T = C + D_T
print("\nC + D^T:")
print(C_plus_D_T)

# Indexing and slicing
# (a) A[1:3, 0]
A_slice_1 = A[1:3, 0]
print("\nA[1:3, 0]:")
print(A_slice_1)

# (b) A[:, 1:]
A_slice_2 = A[:, 1:]
print("\nA[:, 1:]:")
print(A_slice_2)

# (c) A[3, 1]
A_slice_3 = A[3, 1]
print("\nA[3, 1]:")
print(A_slice_3)

# (d) A[2, :2]
A_slice_4 = A[2, :2]
print("\nA[2, :2]:")
print(A_slice_4)

# (e) A[1:2, 0:1]
A_slice_5 = A[1:2, 0:1]
print("\nA[1:2, 0:1]:")
print(A_slice_5)
