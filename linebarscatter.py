import matplotlib.pyplot as plt


x = [5,7,8,7,2]
y=[99,86,87,88,60]

plt.scatter(x,y, color='red', s=10)
plt.title("Scatter plot example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# categories =  ['A', 'B', 'C','D']
# values= [10,15,7,12]

# plt.bar(categories, values, color="green")
# plt.title("Bar Chart")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()



# x = [1,2,3,4,5]
# y=[10,20,2,40,60]

# plt.plot(x,y, marker='o', color='blue', linestyle='--')
# plt.title("Line pLot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()