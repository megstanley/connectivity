filename = 'connectivity_matrices.mat'

from connectivitycohort import ConnectivityCohort

cohort1 = ConnectivityCohort(filename)
cohort1.filename
cohort1.here_dir
cohort1.find_data_path()
cohort1.filepath
cohort1.load_matrices()
cohort1.cohort_size
cohort1.connectome_size
