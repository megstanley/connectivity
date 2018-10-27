import numpy as np
from scipy.io import loadmat
import os

class ConnectivityCohort():

    def __init__(self, filename, here_dir = None):
        self.filename = filename
        self.here_dir = here_dir

    def find_data_path(self):
        '''
        Returns path of the data
        '''
        self.here_dir    = os.path.dirname(os.path.realpath('__file__'))
        self.dataset_dir = os.path.join(self.here_dir, 'data')
        self.filepath = (self.dataset_dir + '/' + self.filename)

    def load_matrices(self):

        tmp = loadmat(self.filepath)
        self.data = tmp['S']
        data_shape = self.data.shape
        self.cohort_size = data_shape[2]
        self.connectome_size = data_shape[0]
