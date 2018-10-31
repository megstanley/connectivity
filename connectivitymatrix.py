import numpy as np
from scipy.io import loadmat
import os


class ConnectivityMatrix():

    def __init__(self, Cmat):
        self.connectome_size = Cmat.shape[0]
        self.connectome = Cmat

    def get_adjacency(self):
        '''calculate the adjacency matrix from the connectivity,
        returns 1 if a connection is present'''
        self.adjacency = (self.connectome > 0).astype(int)
        rowdiag = np.diag(np.sum(self.adjacency, axis = 0))
        coldiag = np.diag(np.sum(self.adjacency, axis = 1))
        self.degree = np.sqrt(rowdiag*coldiag) #matrix with degrees of nodes on the diagonal

    def get_laplacian(self):
        '''calculate a normalised Laplacian matrix from the connectivity'''
        self.rowsum = np.sum(self.connectome, axis = 0)
        self.colsum = np.sum(self.connectome, axis = 1)
        self.norm = np.sqrt(self.rowsum*self.colsum).reshape(self.connectome_size) #making normalization vector
        self.laplacian = np.identity(self.connectome_size) - np.divide(self.connectome, self.norm)
