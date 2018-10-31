import numpy as np
from scipy.io import loadmat
import os

class ConnectivityCohort():

    def __init__(self, filename, here_dir = None):
        self.filename = filename
        self.here_dir = os.path.dirname(os.path.realpath('__file__'))

    def find_data_path(self):
        '''
        Returns path of the data
        '''
        self.par_dir = os.path.abspath(os.path.join(self.here_dir, os.pardir))
        self.dataset_dir = os.path.join(self.par_dir, 'spectral_decomposition-master/data')
        self.filepath = (self.dataset_dir + '/' + self.filename)

    def load_matrices(self):

        tmp = loadmat(self.filepath)
        self.data = tmp['S']
        data_shape = self.data.shape
        self.cohort_size = data_shape[2]
        self.connectome_size = data_shape[0]

    def cohort_statistics(self, p):
        self.mean = np.mean(self.data, axis = 2)
        self.var = np.var(self.data, axis = 2)
        self.zeromean = np.subtract(self.data, self.mean)



    # def add_brains(self, matrix):
    #     '''add additional brain matrices to cohort, from file or matrix'''
    #     #check matrix has the right size
    #     if matrix.size == False:
    #         print('Need input matrix')
    #         return
    #     data_shape = matrix.shape
    #
    #     if data_shape[0:2] == self.data.shape[0:2]:
    #         self.data = np.append(self.data, matrix, axis = 2)
    #     else:
    #         print('Matrix has incorrect dimensions')
    #         return
    #     data_shape = self.data.shape
    #     self.cohort_size = data_shape[2]
