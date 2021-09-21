import matplotlib.pyplot as plt
x_values = list(range(1, 100))
y_values = [x**2 for x in x_values]
#plt.plot(x_values, y_values)
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=40)
# Set the range for each axis.
plt.axis([0, 100, 0, 10001])
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()
