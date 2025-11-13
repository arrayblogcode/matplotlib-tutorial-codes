import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 15, 12, 18, 20]
y2 = [8, 12, 14, 15, 17]
y3 = [5, 7, 6, 8, 10]
y4 = [20, 18, 25, 22, 19]

fig,axs = plt.subplots(2,2, figsize=(10,8) )

#top-left subplot
axs[0,0].plot(x,y1, color='blue')
axs[0,0].set_title("Plot 1")

# top rightj corner
axs[0,1].plot(x,y2, color='green')
axs[0,1].set_title("Plot 1")


# bottom-0left corner
axs[1,0].plot(x,y3, color='red')
axs[1,0].set_title("Plot 1")

# bottom right corner
axs[1,1].plot(x,y4, color='purple')
axs[1,1].set_title("Plot 1")

plt.tight_layout()
plt.show()