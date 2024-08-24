import cv2
import numpy as np

# Create a black background image
height, width = 500, 500
black_image = np.zeros((height, width, 3), dtype=np.uint8)

# Define the animation parameters
num_frames = 100
animation_duration = 5  # in seconds

# Main animation loop
for i in range(num_frames):
    # Clear the image with black color
    black_image.fill(0)

    # Draw a moving circle
    radius = 20
    x = int(i / num_frames * width)
    y = height // 2
    cv2.circle(black_image, (x, y), radius, (0, 255, 0), -1)

    # Display the current frame
    cv2.imshow("Animation", black_image)
    
    # Wait for a short duration to control the animation speed
    key = cv2.waitKey(int(animation_duration / num_frames * 1000))
    
    # Break the loop if the 'q' key is pressed
    if key == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
