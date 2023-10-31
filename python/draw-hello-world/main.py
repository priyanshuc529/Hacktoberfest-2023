import cv2
import numpy as np

# Generate blank white background image
width, height = 400, 200
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Add "Hello, World!" text to image
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)  # black RGB
thickness = 2
text = "Hello, World!"
text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
x = (width - text_size[0]) // 2
y = (height + text_size[1]) // 2
cv2.putText(image, text, (x, y), font, font_scale, font_color, thickness, lineType=cv2.LINE_AA)

# Show image
cv2.imshow('Hello, World!', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save image to file
cv2.imwrite('hello_world.png', image)
