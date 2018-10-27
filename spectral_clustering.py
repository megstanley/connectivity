import numpy as np
from scipy.io import loadmat
import os

def load_matrices():
    '''load the matrices in to numpy arrays'''

    dataset_dir = find_data_path()
    datapath = (dataset_dir + '/connectivity_matrices.mat')
    data = loadmat(datapath)
    #print(data.keys())
    #print(data['S'].shape)
    return data

def element_variance(data):
    '''find the variance of an element (check whether numpy can do this)'''
    var_mat = np.var(dat)
    return var_mat

def element_mean():
    '''mean of an element of the matrix'''

def to_distances():
    '''convert the connectivity matrix to an inverse that represents distances'''


if __name__ == "__main__":
    #path_from_dialog()
    #find_data_path()
    load_matrices()


data = load_matrices()
keys = data.keys()
keys
