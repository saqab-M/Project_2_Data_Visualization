import matplotlib.pyplot as plt

x_values = range(1, 5_001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

#set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqare of value", fontsize=14)

#set size of tick labels
#ax.tick_params(axis="both",which="major", labelsize=14)

ax.axis([0, 5_010, 0, 25000000])

plt.savefig("squares_plot.png", bbox_inches="tight")
