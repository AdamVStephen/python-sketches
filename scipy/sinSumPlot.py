#!/usr/bin/env python
#
# Tested on python3.7  Ref

import scipy as sp
import matplotlib.pylab as plt

t = sp.arange(0, 10, 0.01)
signal = sp.sin(1.7*2*sp.pi*t) + sp.sin(1.9*2*sp.pi*t)
plt.plot(t, signal)
plt.show()

