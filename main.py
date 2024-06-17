import cv2
from PIL import Image
from utils import get_color_limit

# Define the color to track (BGR format)
color = [0, 255, 0]  # Green in BGR ColorSpace

# Initialize webcam input
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the frame from BGR to HSV color space
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the lower and upper HSV limits for the specified color
    lower_limit, upper_limit = get_color_limit(color)

    # Create a mask for the color
    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

    # Convert mask to PIL Image to use getbbox() method
    mask_ = Image.fromarray(mask)

    # Get the bounding box around the object of the specified color
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Display the original frame and the mask
    cv2.imshow('Frame', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
