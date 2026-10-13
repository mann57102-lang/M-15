import matplotlib.pyplot as plt

time = [0, 5, 10, 15, 20, 25, 30]

temp1 = [20, 25, 30, 30, 40, 25, 10]
temp2 = [20, 22, 25, 22, 30, 20, 10]

plt.plot(time, temp1, linestyle='dashed', marker='D', label='Day 1')
plt.plot(time, temp2, linestyle='dashed', marker='D', label='Day 2')

plt.title('Temperature-Time Graph')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')

plt.xlim(5, 25)
plt.ylim(5, 45)

plt.legend()
plt.show()
