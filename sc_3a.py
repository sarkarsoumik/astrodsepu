import numpy as np
import pylab as plt
from scipy.integrate import odeint

H=70
def diff (a,t):
    diff = H/ np.sqrt(a)
    return diff

a0 = 1e-10

t = np.linspace(0, 1000, 100)
a = odeint(diff, a0, t)
aa = (1.5*H*t)**(2/3)

plt.title("3.a (CRN-34)")
plt.plot(t,aa, 'b.', label="Numerical")
plt.plot(t, aa, 'r-', label= "Analytical")
plt.xlabel("t")
plt.ylabel("a(t)")
plt.legend()
plt.show()
