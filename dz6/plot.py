import matplotlib.pyplot as plt
import numpy as np
import json

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
data = np.array([[-4,-4,-23.2992],[-4,-3,-15.0474],[-4,-2,-5.8248],[-4,-1,4.3686],[-4,0,15.5328],[-4,1,27.6678],[-4,2,40.7736],[-4,3,54.8502],[-4,4,69.8976],[-3,-4,-25.2036],[-3,-3,-17.0295],[-3,-2,-7.49297],[-3,-1,3.40589],[-3,0,15.6671],[-3,1,29.2907],[-3,2,44.2766],[-3,3,60.6249],[-3,4,78.3356],[-2,-4,-20.3605],[-2,-3,-14.422],[-2,-2,-6.78683],[-2,-1,2.54506],[-2,0,13.5737],[-2,1,26.299],[-2,2,40.721],[-2,3,56.8397],[-2,4,74.6551],[-1,-4,-8.64477],[-1,-3,-6.72371],[-1,-2,-2.88159],[-1,-1,2.88159],[-1,0,10.5658],[-1,1,20.1711],[-1,2,31.6975],[-1,3,45.1449],[-1,4,60.5134],[0,-4,8],[0,-3,5],[0,-2,4],[0,-1,5],[0,0,8],[0,1,13],[0,2,20],[0,3,29],[0,4,40],[1,-4,25.9343],[1,-3,18.2501],[1,-2,12.4869],[1,-1,8.64477],[1,0,6.72371],[1,1,6.72371],[1,2,8.64477],[1,3,12.4869],[1,4,18.2501],[2,-4,40.721],[2,-3,29.6924],[2,-2,20.3605],[2,-1,12.7253],[2,0,6.78683],[2,1,2.54506],[2,2,0],[2,3,-0.848353],[2,4,0],[3,-4,48.3637],[3,-3,36.1025],[3,-2,25.2036],[3,-1,15.6671],[3,0,7.49297],[3,1,0.681179],[3,2,-4.76825],[3,3,-8.85533],[3,4,-11.58],[4,-4,46.5984],[4,-3,35.4342],[4,-2,25.2408],[4,-1,16.0182],[4,0,7.7664],[4,1,0.4854],[4,2,-5.8248],[4,3,-11.1642],[4,4,-15.5328]])
x = np.linspace(-4, 4, 9)
y = np.linspace(-4, 4, 9)
x, y = np.meshgrid(x, y)
z = data[:, 2].reshape(-1, 9)

# Plot the surface
ax.plot_surface(x, y, z, color='g')

 
with open('out', encoding="utf-8") as f:
	data = np.array(json.load(f))
	x = np.linspace(-4, 4, 9)
	y = np.linspace(-4, 4, 9)
	x, y = np.meshgrid(x, y)
	z = data[:, 2].reshape(9, 9)

	# Plot the surface
	ax.plot_surface(x, y, z)

# Set an equal aspect ratio
ax.set_aspect('auto')

plt.show()