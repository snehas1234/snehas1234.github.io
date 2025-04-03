import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


image = mpl.image.imread(r"c:\Users\user\Downloads\kmeans(pic).jpg")

x = image.reshape(-1, 3)

k_means = KMeans(n_clusters=4)
k_means.fit(x)

segmented_image = k_means.cluster_centers_[k_means.labels_]
segmented_image = segmented_image.reshape(image.shape)  

plt.imshow(image)
plt.title("Original Image")
plt.axis("off")
plt.show()

plt.imshow(segmented_image / 255)
plt.title("Segmented Image")
plt.axis('off')  
plt.show()
