import matplotlib.pyplot as plt
import numpy as np
import meshing


d1 = int(input("Enter x range: "))
d2 = int(input("Enter y range: "))
p = int(input("How many elements in x: "))
m = int(input("How many elemenets in y: "))
element_type = input("If you want triangular elements type 'triangular': ")
node_list, element_list = meshing.uniform_mesh(d1, d2, p, m, element_type)
number_of_nodes = np.size(node_list, 0)
number_of_elements = np.size(element_list, 0)

plt.figure(1)

count = 1

for i in range(0, number_of_nodes):
    plt.annotate(count, xy=(node_list[i, 0], node_list[i, 1]))
    count += 1

if element_type != "triangular":
    x_0, y_0 = node_list[element_list[:, 0] - 1, 0], node_list[element_list[:, 0] - 1, 1]
    x_1, y_1 = node_list[element_list[:, 1] - 1, 0], node_list[element_list[:, 1] - 1, 1]
    x_2, y_2 = node_list[element_list[:, 2] - 1, 0], node_list[element_list[:, 2] - 1, 1]
    x_3, y_3 = node_list[element_list[:, 3] - 1, 0], node_list[element_list[:, 3] - 1, 1]

    plt.plot(np.array([x_0, x_1]), np.array([y_0, y_1]), 'red', linewidth=3)
    plt.plot(np.array([x_1, x_2]), np.array([y_1, y_2]), 'red', linewidth=3)
    plt.plot(np.array([x_2, x_3]), np.array([y_2, y_3]), 'red', linewidth=3)
    plt.plot(np.array([x_3, x_0]), np.array([y_3, y_0]), 'red', linewidth=3)

if element_type == "triangular":
    x_0, y_0 = node_list[element_list[:, 0] - 1, 0], node_list[element_list[:, 0] - 1, 1]
    x_1, y_1 = node_list[element_list[:, 1] - 1, 0], node_list[element_list[:, 1] - 1, 1]
    x_2, y_2 = node_list[element_list[:, 2] - 1, 0], node_list[element_list[:, 2] - 1, 1]

    plt.plot(np.array([x_0, x_1]), np.array([y_0, y_1]), 'red', linewidth=3)
    plt.plot(np.array([x_1, x_2]), np.array([y_1, y_2]), 'red', linewidth=3)
    plt.plot(np.array([x_2, x_0]), np.array([y_2, y_0]), 'red', linewidth=3)
plt.show()
