import time
import numpy as np
import matplotlib.pyplot as plt
from src.classifiers.fc_net import *
from src.data_utils import get_CIFAR10_data
from src.gradient_check import eval_numerical_gradient, eval_numerical_gradient_array
from src.solver import Solver
from src.canonicalize import *

plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

########################################################################################
def rel_error(x, y):
    """ returns relative error """
    return np.max(np.abs(x - y) / (np.maximum(1e-8, np.abs(x) + np.abs(y))))
########################################################################################

########################################################################################
def plot_train_loss(solver1, plot_name):
    plt.subplot(2, 1, 1)
    plt.title('Training loss')
    plt.plot(solver1.loss_history, 'o')
    plt.xlabel('Iteration')
    
    plt.subplot(2, 1, 2)
    plt.title('Accuracy')
    plt.plot(solver1.train_acc_history, '-o', label='train')
    plt.plot(solver1.val_acc_history, '-o', label='val')
    plt.plot([0.5] * len(solver1.val_acc_history), 'k--')
    plt.xlabel('Epoch')
    plt.legend(loc='lower right')
    plt.gcf().set_size_inches(15, 12)
    plt.savefig('outputs/'+plot_name+'.png')
########################################################################################

########################################################################################
# Load the (preprocessed) CIFAR10 data.

data = get_CIFAR10_data()
for k, v in data.iteritems():
    print '%s: ' % k, v.shape
########################################################################################

########################################################################################
X_train = data['X_train']
y_train = data['y_train']

'''
total_train_size = X_train.shape[0]
full_indices = np.random.permutation(total_train_size)

mask1 = range(total_train_size)
X_train1 = X_train[full_indices[mask1]]
y_train1 = y_train[full_indices[mask1]]
'''
data1 = {
        'X_train': X_train, 'y_train' : y_train,
        'X_val': data['X_val'], 'y_val' : data['y_val'],
        'X_test': data['X_test'], 'y_test' : data['y_test'],
        }
########################################################################################

########################################################################################
best_model1 = None
################################################################################
# TODO: Train the best FullyConnectedNet that you can on CIFAR-10. You might   #
# batch normalization and dropout useful. Store your best model in the         #
# best_model variable.                                                         #
################################################################################
# here I use the same parameters I got before, seems like they perform moderately fine
model1 = FullyConnectedNet([100, 100], weight_scale=0.003, use_batchnorm = False, reg=0.6)
solver1 = Solver(model1, data1,
                        print_every=data1['X_train'].shape[0], num_epochs=100, batch_size=100,
                        update_rule='sgd',
                        optim_config={
                          'learning_rate': 0.03,
                        },verbose=True, lr_decay = 0.9,
                 )
solver1.train()
best_model1 = model1
pass
########################################################################################

########################################################################################
# plot stuff
plot_train_loss(solver1, 'train_accuracy_plot')
########################################################################################
