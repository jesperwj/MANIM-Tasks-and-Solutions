import numpy as np
import cv2
import os
import sys

# Parameters
transformation_matrix = np.array([[1, 0.5],   # Example generic 2x2 matrix
                                  [0.5, 1]])  # You can replace this with any 2x2 matrix

# Define a horizontal shear matrix
shear_amount = -0.25  # Adjust this to control the amount of shear
picture_transform_matrix = np.array([[1, shear_amount], [0, 1]])

transformation_matrix = picture_transform_matrix

translation = 20
read_file_name = "standard_Mona_Lisa.jpg"
write_file_name = "transformed_Mona_Lisa.png"

current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

original_image = cv2.imread(os.path.join(current_directory, read_file_name), cv2.IMREAD_UNCHANGED)

# Ensure the image has an alpha channel for transparency
if original_image.shape[2] == 3:
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2BGRA)

rows, cols, ch = original_image.shape

# Convert the 2x2 matrix into a 2x3 affine matrix for OpenCV
M_affine = np.hstack([transformation_matrix, [[0], [0]]])

# Calculate new dimensions to prevent cropping
cos_part = np.abs(M_affine[0, 0])
sin_part = np.abs(M_affine[0, 1])
new_cols = int(rows * sin_part + cols * cos_part)
new_rows = int(rows * cos_part + cols * sin_part)

# Calculate necessary padding for the new image size
up_down = (new_rows - rows) // 2
left_right = (new_cols - cols) // 2

# Add transparent padding to prevent cropping
final_image = cv2.copyMakeBorder(original_image, up_down, up_down, left_right, left_right,
                                 borderType=cv2.BORDER_CONSTANT, value=[0, 0, 0, 0])

# Adjust translation in the matrix for padding
M_affine[0, 2] += left_right
M_affine[1, 2] += up_down

# Apply the generic 2x2 transformation with padding and transparency
final_image = cv2.warpAffine(final_image, M_affine, (new_cols, new_rows),
                             borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))

# Save the output image with a transparent background
cv2.imwrite(os.path.join(current_directory, write_file_name), final_image)
