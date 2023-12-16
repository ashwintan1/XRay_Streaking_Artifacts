import numpy as np

def s_integral_circ(t, A, X, Y, Z, W):
    p = A.shape[0]
    v = np.zeros(p**3)

    for s in range(1, int(np.ceil(np.sqrt(11) * p / 2)) + 1):
        Xworld = (p / 2) * (1 + 2 * np.cos(t)) + s * X / W
        Yworld = (p / 2) * (1 + 2 * np.sin(t)) + s * Y / W
        Zworld = (p / 2) + s * Z / W

        Xl = np.clip(np.floor(Xworld).astype(int), 1, p)
        Xu = np.clip(Xl + 1, 1, p)
        ax = np.maximum(0, Xworld - Xl).flatten()

        Yl = np.clip(np.floor(Yworld).astype(int), 1, p)
        Yu = np.clip(Yl + 1, 1, p)
        ay = np.maximum(0, Yworld - Yl).flatten()

        Zl = np.clip(np.floor(Zworld).astype(int), 1, p)
        Zu = np.clip(Zl + 1, 1, p)
        az = np.maximum(0, Zworld - Zl).flatten()

        lindlll = p * p * (Zl - 1) + p * (Yl - 1) + Xl - 1
        lindull = p * p * (Zl - 1) + p * (Yl - 1) + Xu - 1
        lindlul = p * p * (Zl - 1) + p * (Yu - 1) + Xl - 1
        lindllu = p * p * (Zu - 1) + p * (Yl - 1) + Xl - 1
        linduul = p * p * (Zl - 1) + p * (Yu - 1) + Xu - 1
        lindulu = p * p * (Zu - 1) + p * (Yl - 1) + Xu - 1
        lindluu = p * p * (Zu - 1) + p * (Yu - 1) + Xl - 1
        linduuu = p * p * (Zu - 1) + p * (Yu - 1) + Xu - 1

        v += (1 - ax) * (1 - ay) * (1 - az) * A[lindlll] + \
             ax * (1 - ay) * (1 - az) * A[lindull] + \
             (1 - ax) * ay * (1 - az) * A[lindlul] + \
             (1 - ax) * (1 - ay) * az * A[lindllu] + \
             ax * ay * (1 - az) * A[linduul] + \
             (1 - ax) * ay * az * A[lindluu] + \
             ax * (1 - ay) * az * A[lindulu] + \
             ax * ay * az * A[linduuu]

    return v
