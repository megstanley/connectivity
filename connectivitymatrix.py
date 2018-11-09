import numpy as np
import networkx as nx

class ConnectivityMatrix():
    """Short summary.

    Args:
        Cmat (type): connectivity matrix.

    Attributes:
        connectome_size (type): size of square matrix size -- number of connectome nodes.
        connectome (type):representation of connectome as the matrix.

    """
    #TO DO: Implement 'property' instead of directly accessing variables.

    def __init__(self, Cmat):
        self.connectome_size = Cmat.shape[0]
        self.connectome = Cmat

    def adjacency(self):
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
        norm_connectome = np.divide(self.connectome, norm)
        return norm_connectome

    def laplacian(self):
        '''calculate a normalised Laplacian matrix from the connectivity'''
        laplacian = np.identity(self.connectome_size) - self.norm_connectome
        return laplacian

    def eigenvectors(self):
        '''return eigenvalues and eigenvectors of the Laplacian, sorted
        from smallest eigenvalue to largest'''
        eigvals,eigvecs = np.linalg.eig(self.laplacian)
        valsort = np.argsort(eigvals)
        self.eigvals = np.array(eigvals)[valsort]
        self.eigvecs = np.array(eigvecs)[:,valsort]
        return eigvals, eigvecs

    def centrality(self):
        '''find principle eigenvector of weighted adjacency matrix (normalised
        connectome) -- measures centrality of each node'''
        eigvals,eigvecs = np.linalg.eig(self.norm_connectome)
        valsort = np.argsort(eigvals)
        eigvecs = np.array(eigvecs)[:,valsort]
        centrality = eigvecs[:,self.connectome_size]
        return centrality
