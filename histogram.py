import matplotlib.pyplot as plt

marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(marks, bins=[0, 5,10,15], color='black', edgecolor='blue')
plt.xlabel('Marks')
plt.ylabel('No. of students')
plt.title('Histogram of marks')
plt.show()

