import numpy as np
import networkx as nx

class ConnectivityMatrix():
    """A class to contain a connectivity matrix representing a single brain.

    Parameters
    ----------
    Cmat : numpy array
        Input the connectivity matrix.

    Attributes
    ----------
    connectome_size : int
        Dimension of the connectivity matrix; the number of brain regions included/number of graph nodes.
    connectome : numpy array
        The connectivity matrix itself.

    """

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

    def normalise_connectome(self):
        rowsum = np.sum(self.connectome, axis = 0)
        colsum = np.sum(self.connectome, axis = 1)
        norm = np.sqrt(rowsum*colsum) #making normalization vector
        self.norm_connectome = np.divide(self.connectome, norm)

    def get_laplacian(self):
        '''calculate a normalised Laplacian matrix from the connectivity'''
        self.laplacian = np.identity(self.connectome_size) - self.norm_connectome

    def get_eigenvectors(self):
        '''return eigenvalues and eigenvectors of the Laplacian, sorted
        from smallest eigenvalue to largest'''
        eigvals,eigvecs = np.linalg.eig(self.laplacian)
        valsort = np.argsort(eigvals)
        self.eigvals = np.array(eigvals)[valsort]
        self.eigvecs = np.array(eigvecs)[:,valsort]

    def centrality(self):
        '''find principle eigenvector of weighted adjacency matrix (normalised
        connectome) -- measures centrality of each node'''
        eigvals,eigvecs = np.linalg.eig(self.norm_connectome)
        valsort = np.argsort(eigvals)
        eigvecs = np.array(eigvecs)[:,valsort]
        centrality = eigvecs[:,self.connectome_size]
        return centrality
