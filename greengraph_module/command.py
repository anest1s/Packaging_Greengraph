
from matplotlib import pyplot as plt
mygraph = Greengraph('New York','Chicago')
data = mygraph.green_between(21)
plt.plot(data)