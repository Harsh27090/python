import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
y = [10,15,12,20,14]

plt.plot(x,y) #plot the graph
plt.title("Bakery sales this week!") # title of the graph
plt.xlabel("Day of the week") # label for x-axis
plt.ylabel("Sales per day") # label for y-axis
plt.show() # display the graph
