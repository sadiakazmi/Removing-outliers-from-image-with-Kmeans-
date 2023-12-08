import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from skimage import io

# Load the image
image_path = r'C:\Users\user\Downloads\IMG_0610.jpg'
image = io.imread(image_path)

# Flatten the image into a 2D array (rows x columns, channels)
rows, cols, channels = image.shape
image_2d = image.reshape(rows * cols, channels)

# Apply K-means clustering
n_clusters = 3  # Number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(image_2d)

# Predict cluster labels
cluster_labels = kmeans.predict(image_2d)

# Reshape the cluster labels to the original image shape
cluster_labels = cluster_labels.reshape(rows, cols)

# Display the original image and clustered image
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image)
axes[0].set_title('Original Image')

# Show the clustered image using different colors for each cluster
axes[1].imshow(cluster_labels, cmap='viridis')
axes[1].set_title('Clustered Image')

plt.tight_layout()
plt.show()
