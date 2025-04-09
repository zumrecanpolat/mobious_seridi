#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
theta=np.linspace(0,2*np.pi,100)
w = np.linspace(-0.3,0.3,10)
theta,w =np.meshgrid(theta,w)

phi = 0.5*theta
r = 1+ w*np.cos(phi)
x = r*np.cos(theta)
y = r*np.sin(theta)
z = w*np.sin(phi)

fig=plt.figure(figsize=(10,6))
ax = fig.add_subplot(111,projection='3d')

ax.plot_surface(x,y,z,cmap='coolwarm',edgecolor='k',linewidth=0.3)
ax.set_axis_off()
plt.show()


# In[ ]:




