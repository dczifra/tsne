import argparse
import numpy as np
import tsnecuda
from tsnecuda import TSNE



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Random Data t-SNE with tsnecuda')
    parser.add_argument('--N', type=int, default=1000000, help='Number of random samples to generate')
    parser.add_argument('--M', type=int, default=10, help='Dimensionality of each sample')
    args = parser.parse_args()


    data = np.random.rand(args.N, args.M).astype(np.float32)
    r = TSNE(verbose=1).fit_transform(data)
    print('tsne cuda result', r)