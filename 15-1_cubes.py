import matplotlib.pyplot as plt

#set values
x_values = range(1, 5_001)
y_values = [x**3 for x in x_values]

#create plot
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

#setup chart
ax.set_title("Cubes", fontsize= 24)
ax.set_xlabel("Values", fontsize= 14)
ax.set_ylabel("Cubed Values", fontsize= 14)
#ax.tick_params(axis="both", labelsize=14)
#set chart limits

ax.axis([0, 5_010, 0, 25000000])

plt.savefig("cubes_plot.png", bbox_inches="tight")
