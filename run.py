import matplotlib.pyplot as plt

over=[5,10,15,20]
run=[45,79,145,234]
plt.plot(over,run)
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.title("Runs scored in overs")
plt.legend()
plt.show()