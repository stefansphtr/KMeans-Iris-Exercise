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

def plot_data_and_centroids(x: np.ndarray, y: np.ndarray, centroids: np.ndarray) -> None:
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
    plt.scatter(x, y, label='Data Points')
    
    # Plot centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], label='Centroids')
    
    # Remove the top and right spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    
    # Add legend to the plot
    ax.legend()
    
    # Add title
    plt.title("Data Points and Centroids")
    
    # Add x and y axis labels
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    
    # Display the plot
    plt.show()
