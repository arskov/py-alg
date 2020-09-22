import numpy as np

input_vals = [3, 3, 3, 0]
K, N, M, P = 3, 3, 3, 0
print(np.stack([np.zeros((N, M, P), dtype = np.int) for _ in range(K)]))
print(np.stack([np.ones((N, M, P), dtype = np.int) for _ in range(K)]))
