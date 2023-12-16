import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

def Psi(A):
    C = fft(A)
    p, q = A.shape
    D = np.zeros_like(A)

    ind1 = np.arange(1, p+1)

    A1 = np.zeros((p, q))
    for i in range(p):
        A1[i, :] = ind1

    A2 = np.zeros((p, q))
    for i in range(p):
        A2[i, :] = i + 1

    A3 = A1**2 + A2**2

    D = -C * A3 * 4 * (np.pi**2) / (p**2)

    B = ifft(D)
    Bb = B[p//2, :, :]
    Bbb = np.squeeze(Bb)
    
    plt.imshow(Bbb, cmap='gray')
    plt.show()

# Example usage
p = 64
q = 64
A = np.random.rand(p, q)  # Replace this with your actual 2D array
Psi(A)
