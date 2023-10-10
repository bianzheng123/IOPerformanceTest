import os
import numpy as np


# generate the data, then split the data into several buckets
def generate_data(n_chunk: int, vec_dim: int):
    default_item_size_chunk = 25000
    n_item = n_chunk * default_item_size_chunk
    doclens = np.random.normal(100, 10, size=n_item)



    vector_set_l = np.random.normal(1, 10, size=())
    pass


if __name__ == '__main__':
    pass
