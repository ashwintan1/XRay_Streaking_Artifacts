import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from s_integral_circ import s_integral_circ
from phantominator import shepp_logan

def iscube(A):
    return len(A.shape) == 3 and A.shape[0] == A.shape[1] == A.shape[2]

#def s_integral_circ(t, A, X, Y, Z, W):
    # Implementation of s_integral_circ function goes here
#    pass

def Normal_circ(A, nt):
    assert iscube(A), 'Image is not a cube.'

    p = A.shape[0]
    x, y, z = np.meshgrid(np.arange(1, p+1), np.arange(1, p+1), np.arange(1, p+1))
    Z = z - (p/2)
    ts = np.linspace(0, 2*np.pi, nt)
    B = np.zeros_like(A)
    v = np.zeros((nt, p**3))

    for t in range(nt):
        X = x - (p/2) * (1 + 2 * np.cos(ts[t]))
        Y = y - (p/2) * (1 + 2 * np.sin(ts[t]))
        W = np.sqrt(X**2 + Y**2 + Z**2)
        Wlin = W.flatten()
        v[t, :] = s_integral_circ(ts[t], A, X, Y, Z, W) / (Wlin**2)

    B[:, :, :] = np.sum(v, axis=0) * 2 * np.pi / (nt - 1)
    Aa = A[:, :, p//2] / np.max(A[:, :, p//2])
    Bb = B[:, :, p//2] / np.max(B[:, :, p//2])
    C = np.transpose(Bb)

    plt.figure()
    plt.imshow(Aa, cmap='gray')
    plt.figure()
    plt.imshow(C, cmap='gray')
    plt.show()

# Example usage
p = 64
A = shepp_logan(p)
nt = 30
Normal_circ(A, nt)
