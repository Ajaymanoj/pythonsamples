import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
earth = [56, 44, 55]
location = ['venizula', 'nottigham', 'london']

# Setting up graph
plt.scatter(earth, location)
plt.xlabel("Earth Temperature")
plt.ylabel("Location")

# Showing graph
plt.show()




