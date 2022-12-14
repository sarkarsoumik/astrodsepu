import numpy as np
import matplotlib.pyplot as plt

H = 70 / 3.086e19
wm = 0.3
wr = 5e-5
wde = 0.7
w1 = -2./3.
w2 = -1./2.
a0 = 1e-10
a1 = 1.0
n = 1000

def f(a, t, w):
    return 1 / (H * (wm / a + wr / a ** 2 + wde / a ** (3 * w + 1)) ** 0.5)

h = (a1 - a0) / (n - 1)
a = np.linspace(a0, a1, n)
t1 = np.zeros(n)
t2 = np.zeros(n)
t1[0] = 0
t2[0] = 0
for i in range(n - 1):
    t1[i + 1] = t1[i] + h * f(a[i] + 0.5 * h, t1[i] + 0.5 * h * f(a[i], t1[i], w1), w1)
    t2[i + 1] = t2[i] + h * f(a[i] + 0.5 * h, t2[i] + 0.5 * h * f(a[i], t2[i], w2), w2)

plt.title("3.e  (CRN- 34)")
plt.plot(t1, a,'r-', label="ω = -2/3")
plt.plot(t2, a,'b--', label="ω = -1/2")
plt.xlabel("t (sec.)")
plt.ylabel("a(t)")
plt.legend()
plt.show()
