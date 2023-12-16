import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom

from Normal_circ import Normal_circ
from ameliorate_circ import amerliorate_circ

from Psi import Psi

# Equivalent Python code
def main():
    p = 64

    A = shepp_logan_phantom()[:p, :p, :p]

    t = 30
    B = Normal_circ_v2(A, t)

    C = ameliorate_circ_v2(B)

    alpha = -1
    D = Psi(C, alpha)

if __name__ == "__main__":
    main()
