# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List


def create_centroids(x: np.ndarray, y: np.ndarray, k: int) -> np.ndarray:
    """
    Create k centroids from given x and y coordinates.

    Parameters:
        x (np.ndarray): The x coordinates of the data points.
        y (np.ndarray): The y coordinates of the data points.
        k (int): The number of centroids to create.

    Returns:
        np.ndarray: The x and y coordinates of the created centroids.
    """
    # Create x and y coordinates of k random centroids
    centroids_x = np.random.uniform(np.min(x), np.max(x), k)
    centroids_y = np.random.uniform(np.min(y), np.max(y), k)

    # Combine x and y coordinates to create centroids
    centroids = np.array(list(zip(centroids_x, centroids_y)))

    return centroids


def plot_data_and_centroids(
    x: np.ndarray, y: np.ndarray, centroids: np.ndarray
) -> None:
    """
    Plot data points and centroids.

    Parameters}:
        x (np.ndarray): The x coordinates of the data points.
        y (np.ndarray): The y coordinates of the data points.
        centroids (np.ndarray): The x and y coordinates of the centroids.

    Returns:
    None
    """
    # Create a new figure and axes
    fig, ax = plt.subplots()

    # Plot the data points
    plt.scatter(x, y, label="Data Points")

    # Plot centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], label="Centroids")

    # Remove the top and right spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position("left")
    ax.xaxis.set_ticks_position("bottom")

    # Add legend to the plot
    ax.legend()

    # Add title
    plt.title("Data Points and Centroids")

    # Add x and y axis labels
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")

    # Display the plot
    plt.show()


def calculate_euclidean_distance(
    point1: Tuple[float, float], point2: Tuple[float, float]
) -> float:
    """
    Calculate the Euclidean distance between two points in a 2D space.
    Parameters:
    point1 (Tuple[float, float]): The coordinates of the first point.
    point2 (Tuple[float, float]): The coordinates of the second point.
    Returns:
    float: The Euclidean distance between the two points.
    """
    # Calculate the square of the difference in x coordinates
    x_difference_squared = (point1[0] - point2[0]) ** 2
    # Calculate the square of the difference in y coordinates
    y_difference_squared = (point1[1] - point2[1]) ** 2
    # Calculate the Euclidean distance using the Pythagorean theorem
    euclidean_distance = (x_difference_squared + y_difference_squared) ** 0.5
    return euclidean_distance


def assign_to_nearest_centroid(
    data_point: np.ndarray, centroids: List[np.ndarray]
) -> int:
    """
    Assign the nearest centroid to a data point.
    Parameters:
    data_point (np.ndarray): The data point to assign a centroid to.
    centroids (List[np.ndarray]): The list of centroids.
    Returns:
    int: The index of the nearest centroid.
    """
    # Calculate the distance from the data point to each centroid
    distances_to_centroids = np.array(
        [calculate_euclidean_distance(data_point, centroid) for centroid in centroids]
    )
    # Find the index of the nearest centroid
    nearest_centroid_index = np.argmin(distances_to_centroids)
    return nearest_centroid_index


def plot_clusters(
    sepal_dimensions: np.ndarray,
    centroids: np.ndarray,
    cluster_labels: np.ndarray,
    k: int,
) -> None:
    """Plot the clusters and centroids.
    Args:
    sepal_dimensions (np.array): The sepal dimensions of the samples.
    centroids (np.array): The centroids of the clusters.
    cluster_labels (np.array): The labels of the clusters for each sample.
    k (int): The number of clusters.
    """
    # Define colors for each cluster
    cluster_colors = ["red", "green", "blue"]
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()
    # Plot each cluster
    for centroid_index in range(k):
        # Gather points assigned to the current centroid
        points_in_cluster = np.array(
            [
                sepal_dimensions[j]
                for j in range(len(sepal_dimensions))
                if cluster_labels[j] == centroid_index
            ]
        )

        # Plot points in the current cluster
        ax.scatter(
            points_in_cluster[:, 0],
            points_in_cluster[:, 1],
            c=cluster_colors[centroid_index],
            alpha=0.5,
            label=f"Cluster {centroid_index+1}",
        )
    # Plot centroids
    ax.scatter(
        centroids[:, 0],
        centroids[:, 1],
        marker="D",
        s=150,
        color="#1f77b4",
        label="Centroids",
    )
    # Remove the top and right spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position("left")
    ax.xaxis.set_ticks_position("bottom")
    # Label axes
    ax.set_xlabel("Sepal length (cm)")
    ax.set_ylabel("Sepal width (cm)")
    # Add a title
    ax.set_title("K-Means Clustering of Iris Dataset (Sepal Dimensions)")
    # Add a legend
    ax.legend()
    # Display plot
    plt.show()
