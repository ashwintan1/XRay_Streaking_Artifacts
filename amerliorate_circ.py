import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftn, ifftn

def ameliorate_circ_v2(A):
    p = A.shape[0]
    x = np.arange(1, p+1)
    xi1, xi2, xi3 = np.meshgrid(x, x, x, indexing='ij')
    C = fftn(A)
    D1 = ifftn(xi1 * C)
    D2 = ifftn(xi2 * C)
    D3 = ifftn(xi3 * C)
    E = -p * ifftn((xi1**2 + xi2**2 + xi3**2)**(1/2) * C)
    B = (xi1 - p/2) * D1 + (xi2 - p/2) * D2 + (xi3 - p/2) * D3 + E
    Bb = B / np.max(B)
    Bb = Bb[:, :, p//2]
    
    plt.imshow(Bb, cmap='gray')
    plt.show()

# Example usage
p = 64
A = np.random.rand(p, p, p)  # Replace this with your actual 3D image data
ameliorate_circ_v2(A)
