#!/usr/bin/env python

import os
import requests


def download_image(image_url, target_directory):
    """
    Downloads an image from a given URL and saves it to a target directory.

    Args:
        image_url (str): The URL of the image to download.
        target_directory (str): The directory where the image will be saved.

    Returns:
        None
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(image_url, stream=True, headers=headers)

    if response.status_code == 200:
        filename = os.path.basename(image_url)
        save_path = os.path.join(target_directory, filename)

        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with open(save_path, "wb") as image_file:
            image_file.write(response.content)

        print(f"Image successfully downloaded to {save_path}")
    else:
        print(
            f"Failed to download image. HTTP GET request returned status code {response.status_code}"
        )


def main():
    """
    The main function that triggers the image download.
    """
    image_url = input("Please enter the URL of the image you want to download: ")
    target_directory = os.path.join("src", "images")

    download_image(image_url, target_directory)


if __name__ == "__main__":
    main()
