# Removing-outliers-from-image-with-Kmeans-
this code performs K-means clustering on the colors of the image, dividing it into a specified number of clusters, and visualizes the original image alongside the clustered version, where pixels belonging to different clusters are represented using distinct colors.
n_clusters = 3  # Number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(image_2d)
# # Requirements
Make sure you have Python installed along with the libraries like NumPy, scikit-learn, Matplotlib, and scikit-image (skimage).
Copy the provided code snippet into a Python script or a Jupyter Notebook.
Ensure that the required libraries are installed and import them as mentioned in the code.
# # # Run the code.
It will load the specified image, perform K-means clustering on its colors, and display the original image alongside the clustered image.
After executing the code, you'll see a Matplotlib window displaying two images:
![myplot](https://github.com/sadiakazmi/Removing-outliers-from-image-with-Kmeans-/assets/142217150/12337860-e710-4962-87ae-251abfc1993e)
Original Image: The first image displayed is the original image.
Clustered Image: The second image is the clustered version of the original image, where different colors represent different clusters obtained by the K-means algorithm.
Remember to replace 'path_to_your_image.jpg' with the path to the image file you want to use for clustering. Additionally, adjust the n_clusters variable if you want a different number of clusters for segmenting the image.
