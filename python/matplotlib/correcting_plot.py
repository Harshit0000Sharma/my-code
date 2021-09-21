import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
value=[1,2,3,4,5]
plt.plot(value,squares,linewidth=5)
## Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
## Set size of tick labels.
plt.tick_params(axis='both', which='major',labelsize=14)
plt.scatter(2,4,s=200)
plt.show()
