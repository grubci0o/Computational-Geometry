import numpy as np


def uniform_mesh(d1, d2, p, m, element_type=''):
    dim = 2

    q = np.array([[0, 0], [d1, 0], [0, d2], [d1, d2]])

    number_of_nodes = (p + 1) * (m + 1)
    number_of_elements = p * m
    nodes_per_element = 4

    node_list = np.zeros([number_of_nodes, dim])

    a = (q[1, 0] - q[0, 0]) / p  # horyzontalnie inkrementuje
    b = (q[2, 1] - q[0, 1]) / m  # wertykalnie inkrementuje

    n = 0

    for i in range(1, m + 2):
        for j in range(1, p + 2):
            node_list[n, 0] = q[0, 0] + (j + 1) * a
            node_list[n, 1] = q[0, 1] + (i - 1) * b
            n += 1

    element_list = np.zeros([number_of_elements, nodes_per_element])
    for i in range(1, m + 1):
        for j in range(1, p + 1):
            if j == 1:
                element_list[(i - 1) * p + j - 1, 0] = (i - 1) * (p + 1) + j
                element_list[(i - 1) * p + j - 1, 1] = element_list[(i - 1) * p + j - 1, 0] + 1
                element_list[(i - 1) * p + j - 1, 3] = element_list[(i - 1) * p + j - 1, 0] + p + 1
                element_list[(i - 1) * p + j - 1, 2] = element_list[(i - 1) * p + j - 1, 3] + 1
            else:
                element_list[(i - 1) * p + j - 1, 0] = element_list[(i - 1) * p + j - 2, 1]
                element_list[(i - 1) * p + j - 1, 3] = element_list[(i - 1) * p + j - 2, 2]
                element_list[(i - 1) * p + j - 1, 1] = element_list[(i - 1) * p + j - 1, 0] + 1
                element_list[(i - 1) * p + j - 1, 2] = element_list[(i - 1) * p + j - 1, 3] + 1

    if element_type == "triangular":
        nodes_per_element_triangular = 3
        number_of_elements_triangular = 2 * number_of_elements
        element_list_triangular = np.zeros([number_of_elements_triangular, nodes_per_element_triangular])

        for i in range(1, number_of_elements + 1):
            element_list_triangular[2 * (i - 1), 0] = element_list[i - 1, 0]
            element_list_triangular[2 * (i - 1), 1] = element_list[i - 1, 1]
            element_list_triangular[2 * (i - 1), 2] = element_list[i - 1, 2]

            element_list_triangular[2 * (i - 1) + 1, 0] = element_list[i - 1, 0]
            element_list_triangular[2 * (i - 1) + 1, 1] = element_list[i - 1, 2]
            element_list_triangular[2 * (i - 1) + 1, 2] = element_list[i - 1, 3]
        element_list = element_list_triangular
    element_list = element_list.astype(int)
    return node_list, element_list
