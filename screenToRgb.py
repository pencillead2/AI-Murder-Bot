import mss
import time
import numpy as np
from PIL import Image

# Define the target downscaled resolution
TARGET_WIDTH = 320   # Change this to the desired width
TARGET_HEIGHT = 180  # Change this to the desired height
OUTPUT_FILENAME = "downscaled_screen.jpg"  # Name of the output file

def capture_screen():
    """Captures the entire screen and returns it as a PIL image."""
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])  # Capture primary monitor
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        return img

def downscale_image(image, width, height):
    """Resizes the image to the target width and height."""
    return image.resize((width, height), Image.Resampling.LANCZOS)

def get_rgb_values(image):
    """Returns the RGB values of each pixel in the downscaled image."""
    return np.array(image)

def save_image(image, filename):
    """Saves the downscaled image as a JPEG file."""
    image.save(filename, "JPEG", quality=95)
    print(f"Saved downscaled image as {filename}")

def screen_to_rgb():
    # Capture and process the screen

    screen_image = capture_screen()
    downscaled_image = downscale_image(screen_image, TARGET_WIDTH, TARGET_HEIGHT)
    
    # Get RGB values
    rgb_values = get_rgb_values(downscaled_image)
    return rgb_values

if __name__ == "__main__":
    main()