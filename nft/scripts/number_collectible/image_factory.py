from __future__ import division
 
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

 
m = 480

n = 320
 
s = 300  # Scale.

def factory(num):
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))
    Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
    
    #C = np.full((n, m), -.49 + 0.64j)
    if num < 50:
        C = np.full((n, m), -(num/2*num)/100 + num/100j)
    else:
        C = np.full((n, m), -(num)/100 + (num-49)/100j)
    M = np.full((n, m), True, dtype=bool)
    N = np.zeros((n, m))
    for i in range(256):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        N[M] = i
    
    
    # Save with Matplotlib using a colormap.
    fig = plt.figure()
    fig.set_size_inches(m / 100, n / 100)
    ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
    ax.set_xticks([])
    ax.set_yticks([])

    if num % 10 ==0:
        col = 'hsv'
    elif num % 13 == 0:
        col = 'Accent'
    elif num % 2 == 0:
        col = 'flag'
    else:
        col = 'hot'
    plt.imshow(np.flipud(N), cmap=col)
    #plt.savefig('nft/img/' + str(num) + '.png')
    plt.savefig('img/' + str(num) + '.png')
    plt.close()

"""factory(2)
factory(12)
factory(13)
factory(51)
factory(82)
factory(80)
factory(99)"""
