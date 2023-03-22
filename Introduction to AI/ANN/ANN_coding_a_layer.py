# inputs = [1.2,5.1,2.1] 
# weights = [3.1, 2.1, 8.7] # the connections between neurons
# bias = 3 #each neuron has a unique bias

# output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2]\
# + bias # sum(weights*neuron) + bias

# print('%.1f' %output)


import numpy as np
np.random.seed(0)

X = np.array([[1.0, 2.0, 3.0, 2.5],
              [2.0, 5.0, -1.0, 2.0],
               [-1.5, 2.7,3.3,-0.8]])

class Layer_Dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.1*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
layer2.forward(layer1.output)
# print(layer1.output)
print(layer2.output)



"""inputs = np.array([[1.0, 2.0, 3.0, 2.5],
                   [2.0, 5.0, -1.0, 2.0],
                   [-1.5, 2.7,3.3, -0.8]])

weights = np.array([[0.2,0.8,-0.5,1.0],
           [0.5,-0.91,0.26,-0.5], 
           [-0.26,-0.27,0.17,0.87]])

biases = np.array([2,3,0.5])

weights2 = np.array([[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]])
biases2 = np.array([-1, 2, -0.5])
layer1_output = np.dot(inputs, weights.T) + biases
layer2_output = np.dot(layer1_output, weights2.T) + biases2

print(layer2_output)"""




# layer_output = []
# for neuron_weights, neuron_bias in zip(weights, biases):
#     neuron_output = 0
#     for n_input, weight in zip(inputs,neuron_weights):
#         neuron_output += n_input * weight
#     neuron_output += neuron_bias
#     layer_output.append(neuron_output)

# print(layer_output)

 
