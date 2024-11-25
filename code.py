import matplotlib.pyplot as plt
import numpy as np




x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 2, 3, 5, 8, 13, 20])

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Line Chart')
plt.title('Line Chart Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


plt.figure(figsize=(8, 6))


plt.plot(x, y, label='Normal', marker='o', markersize=10, linestyle='dashed', linewidth=3)


y2 = np.array([2, 3, 4, 6, 10, 15, 22])
plt.plot(x, y2, label='Fast', marker='o', markersize=10, linestyle='dashed', linewidth=3)

plt.title('Two Line Chart Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


fig, axs = plt.subplots(1, 3, figsize=(15, 5))

#  First Chart
axs[0].plot(x, y, label='First Chart')
axs[0].set_title('First Chart')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')

#  Second Chart
axs[1].plot(np.array([0, 1, 2, 3, 4, 5, 6]), np.array([2, 4, 6, 8, 10, 12, 14]), label='Second Chart')
axs[1].set_title('Second Chart')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')

#  Third Chart
axs[2].plot(np.array([0, 1, 3, 4]), np.array([4, 6, 3, 4]), label='Third Chart')
axs[2].set_title('Third Chart')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')


plt.suptitle('My data visualization assignment')


plt.tight_layout()
plt.show()
