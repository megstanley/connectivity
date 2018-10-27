import numpy as np



class ConnectivityMatrix():
    

    def __init__(self, data):
        self.connectome_number = data.shape[2]
        self.connectome_size = data.shape[0]

    def load_matrices(data):
