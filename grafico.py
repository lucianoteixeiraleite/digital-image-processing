import matplotlib.pyplot as plt
import numpy as np

# def f(x,y):
    # return x**2 + y**2 

# x = np.linspace(-6,6,30)
# y = np.linspace(-6,6,30)

# X , Y = np.meshgrid(x,y)

# Z = f(X,Y)

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.plot_wireframe(X,Y,Z,color = 'orange')
# ax.plot_wireframe(X,Y,Z,color = 'orange')
# plt.show()

x=np.arange(-1,10,1)
y=(x*x)-(5*x)+6 
plt.plot(x,y,color='green',linewidth=1.0)
plt.show()
