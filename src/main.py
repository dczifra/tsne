import os
import sklearn
import argparse
import matplotlib.pyplot as plt

# load mnist dataset
from torchvision import datasets, transforms


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MNIST Dataset and t-SNE Visualization')
    parser.add_argument('--N', type=int, default=10000, help='Number of samples to use for t-SNE')
    parser.add_argument('--cuda', action='store_true', help='Use CUDA for computations')
    parser.add_argument('--mode', type=str, default='sklearn', help='Choose from t-SNE implementations', choices=['sklearn', 'cannylab'])
    args = parser.parse_args()

    mnist_train = datasets.MNIST(root='./data', train=True, download=True, transform=transforms.ToTensor())
    mnist_test = datasets.MNIST(root='./data', train=False, download=True, transform=transforms.ToTensor())
    mnist_train_data = mnist_train.data.float() / 255.0
    mnist_train_labels = mnist_train.targets
    mnist_test_data = mnist_test.data.float() / 255.0
    mnist_test_labels = mnist_test.targets

    # Example usage
    print("MNIST train data shape:", mnist_train_data.shape)
    print("MNIST train labels shape:", mnist_train_labels.shape)
    print("MNIST test data shape:", mnist_test_data.shape)
    print("MNIST test labels shape:", mnist_test_labels.shape)

    # Example of using TSNE
    X = mnist_train_data.view(mnist_train_data.size(0), -1)  # Flatten the images
    X = X[:args.N]
    Y = mnist_train_labels.numpy()[:args.N]

    if args.mode == 'sklearn':
        from sklearn.manifold._t_sne import TSNE
        tsne = TSNE(n_components=2, perplexity=15, learning_rate=10)
        X_embedded = tsne.fit_transform(X.numpy())
    elif args.mode == 'cannylab':
        from tsnecuda import TSNE
        X_embedded = TSNE(n_components=2, perplexity=15, learning_rate=10).fit_transform(X.numpy())
    else:
        raise ValueError("Invalid mode selected. Choose 'sklearn' or 'cannylab'.")

    # === Scatter plot of t-SNE results ===
    os.makedirs('data/plots', exist_ok=True)
    print("TSNE embedded shape:", X_embedded.shape)
    plt.scatter(X_embedded[:, 0], X_embedded[:, 1], c=Y, cmap='jet', s=1)
    plt.colorbar()
    plt.title('t-SNE visualization of MNIST')
    plt.savefig(f'data/plots/mnist_tsne-{args.mode}.png')