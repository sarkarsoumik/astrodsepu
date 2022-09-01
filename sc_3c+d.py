import numpy as np
import matplotlib.pyplot as plt

H = 70 / 3.086e19
wm = 0.3
wr = 5e-5
wk1 = -0.3
wk2 = -0.5
a0 = 1e-10
a1 = 1.0
n = 1000

# question part 4

def f(a, t, wk):
    return 1 / (H ** 2 * (wm / a + wr / a ** 2 - wk))

h = (a1 - a0) / (n - 1)
a = np.linspace(a0, a1, n)
t1 = np.zeros(n)
t2 = np.zeros(n)
t1[0] = 0
t2[0] = 0
for i in range(n - 1):
    t1[i + 1] = t1[i] + h * f(a[i] + 0.5 * h, t1[i] + 0.5 * h * f(a[i], t1[i], wk1), wk1)
    t2[i + 1] = t2[i] + h * f(a[i] + 0.5 * h, t2[i] + 0.5 * h * f(a[i], t2[i], wk2), wk2)
    


# question part 3

H = 70 / 3.086e19
wm = 0.3
wr = 5e-5

wde = 0.7
w = -1.0

a0 = 1e-10
a1 = 1.0
n = 1000


def g(a, t):
    return 1 / (H * (wm / a + wr / a ** 2 + wde / a ** (3 * w + 1)) ** 0.5)

h = (a1 - a0) / (n - 1)
a = np.linspace(a0, a1, n)
t = np.zeros(n)
t[0] = 0
for i in range(n - 1):
    t[i + 1] = t[i] + h * g(a[i] + 0.5 * h, t[i] + 0.5 * h * g(a[i], t[i]))

plt.title("3.d (CRN-34)")
plt.grid()
plt.plot(t,a,'r-',label='Λ CDM')
plt.plot(t1,a,'g-',label='ωk = -0.3')
plt.plot(t2,a,'b-',label='ωk = -0.5')
plt.xlabel('t (sec.)')
plt.ylabel('a(t)')
plt.legend()
plt.show()
