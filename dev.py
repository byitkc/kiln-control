# Imports
import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(10,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

# Plot sine using green color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

# Set x limits
# plt.xlim(-4.0,4.0)
plt.xlim(X.min()*1.1, X.max()*1.1)

# Set x ticks
#plt.xticks(np.linspace(-4,4,9,endpoint=True))
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# Set y limits
# plt.ylim(-1.0,1.0)
plt.ylim(C.min()*1.1, C.max()*1.1)

# Set y ticks
# plt.yticks(np.linspace(-1,1,5,endpoint=True))
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

# Save figure using 72 dots per inch
# savefig("../figures/exercice_2.png",dpi=72)

# Show result on screen
plt.show()