import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

#x = np.array([0.1, 0.3])
#y = 0.2
#
#weights = np.array([-0.8, 0.5])
#learnrate = 0.5
#
#h = x[0] * weights[0] + x[1] * weights[1]
#nn_output = sigmoid(h)
#error = y - nn_output
#
#output_grad = sigmoid_prime(h)
#error_term = error * output_grad
#
#del_w = [learnrate * error_term * x[0],
#         learnrate * error_term * x[1]]
#
#print(del_w)

learnrate = 0.5

x = np.array([1, 2, 3, 4])
y = np.array(0.5)

w = np.array([0.5, -0.5, 0.3, 0.1])

h = np.dot(x, w)

nn_output = sigmoid(h)
error = y - nn_output

output_grad = sigmoid_prime(h)
error_term = error * output_grad

del_w = learnrate * error_term * x

print(del_w)
