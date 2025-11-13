import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [10,15,12,18,20]
y2= [8,12,14,15,17]
y3 = [100,150,120,181,200]
y4= [18,120,14,150,17]

plt.plot(x,y1, label="Series1", color="blue", marker='o')

plt.plot(x,y2, label="Series2", color="red", marker='s')
plt.plot(x,y3, label="Series3", color="green", marker='o')
plt.plot(x,y4, label="Series4", color="black", marker='s')
plt.title("Customized grpah ")
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
plt.legend()
plt.show()