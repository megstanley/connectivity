import numpy as np
from scipy.io import loadmat
import os

def path_from_dialog():
    '''find the path to the data'''
    '''this doesn't work yet'''
    tk.Tk().withdraw() # Close the root window
    in_path = tkFileDialog.askopenfilename()
    print(in_path)

def find_data_path():
    '''
    Returns path of the data
    '''
    here_dir    = os.path.dirname(os.path.realpath('__file__'))
    dataset_dir = os.path.join(here_dir, 'data')
    return dataset_dir

def load_matrices():
    '''load the matrices in to numpy arrays'''

    dataset_dir = find_data_path()
    datapath = (dataset_dir + '/connectivity_matrices.mat')
    data = loadmat(datapath)
    #print(data.keys())
    #print(data['S'].shape)
    return data

def element_variance():
    '''find the variance of an element (check whether numpy can do this)'''

def element_mean():
    '''mean of an element of the matrix'''

def to_distances():
    '''convert the connectivity matrix to an inverse that represents distances'''


if __name__ == "__main__":
    #path_from_dialog()
    #find_data_path()
    load_matrices()

data = load_matrices()
data
