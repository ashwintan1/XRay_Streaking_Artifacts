from phantominator import shepp_logan
import matplotlib.pyplot as plt
ph = shepp_logan(128)

# MR phantom (returns proton density, T1, and T2 maps)
M0, T1, T2 = shepp_logan((128, 128, 20), MR=True)

plt.imshow(M0[:,:,10], cmap='gray')
plt.show()