import matplotlib.pyplot as plt
match=[1,2,3,4]
scores=[45,79,145,234]
plt.barh(match,scores)
plt.xlabel("Match")
plt.ylabel("Scores")
plt.title("Scores in matches")
plt.show()