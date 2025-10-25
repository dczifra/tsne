import argparse
import numpy as np
import tsnecuda
from tsnecuda import TSNE

# Import memory profiler
from memory_profiler import profile


@profile
def TSNE_knn_test(N, M, data, batch_size):
    r = TSNE(verbose=1, batch_size=batch_size).fit_transform(data)
    print('tsne cuda result', r)

@profile
def faiss_knn_test(N, M, data):
    import faiss
    res = faiss.StandardGpuResources()  # use a single GPU

    ## Using a flat index
    index_flat = faiss.IndexFlatL2(M)

    # make it a flat GPU index
    gpu_index_flat = faiss.index_cpu_to_gpu(res, 0, index_flat)
    gpu_index_flat.add(data)         # add vectors to the index
    print("ntotal:", gpu_index_flat.ntotal)

    k = 32                          # we want to see 4 nearest neighbors
    D, I = gpu_index_flat.search(data, k)  # actual search
    #print(I[:5])                   # neighbors of the 5 first queries
    #print(I[-5:])                  # neighbors of the 5 last queries
    print("D/I shape", D.shape, I.shape)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Random Data t-SNE with tsnecuda')
    parser.add_argument('--N', type=int, default=1000000, help='Number of random samples to generate')
    parser.add_argument('--M', type=int, default=10, help='Dimensionality of each sample')
    parser.add_argument('--batch_size', type=int, default=8196, help='Batch size for t-SNE (0 for full batch)')
    args = parser.parse_args()


    data = np.random.rand(args.N, args.M).astype(np.float32)


    # === Run faiss KNN Test ===
    #faiss_knn_test(args.N, args.M, data)

    # === Run t-SNE KNN Test ===
    TSNE_knn_test(args.N, args.M, data, args.batch_size)