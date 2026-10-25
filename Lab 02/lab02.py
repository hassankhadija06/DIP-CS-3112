# %%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Step 2: Load the Image
# ==========================================
image_path = 'my_image.png.jfif' 

image = cv.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Error: Could not load image at {image_path}. Check the filename.")

print("--- Step 2: Image Loading ---")
print(f"Image Shape: {image.shape}")
print(f"Image Data Type: {image.dtype}")


# ==========================================
# Step 3: Inspect the Image
# ==========================================
height, width, channels = image.shape

# Coordinates for top-left and center
y_center, x_center = height // 2, width // 2

print("\n--- Step 3: Image Inspection ---")
print(f"Height: {height} pixels")
print(f"Width: {width} pixels")
print(f"Number of Channels: {channels}")
print(f"Top-Left Pixel (BGR) at [0, 0]: {image[0, 0]}")
print(f"Center Pixel (BGR) at [{y_center}, {x_center}]: {image[y_center, x_center]}")

print(f"\nGlobal Minimum Pixel Value: {np.min(image)}")
print(f"Global Maximum Pixel Value: {np.max(image)}")

# Per-channel min/max (0=Blue, 1=Green, 2=Red)
print(f"Blue Channel Min/Max: {np.min(image[:, :, 0])} / {np.max(image[:, :, 0])}")
print(f"Green Channel Min/Max: {np.min(image[:, :, 1])} / {np.max(image[:, :, 1])}")
print(f"Red Channel Min/Max: {np.min(image[:, :, 2])} / {np.max(image[:, :, 2])}")


# ==========================================
# Step 4: Convert Colors and Separate Channels
# ==========================================
# Convert BGR to RGB for Matplotlib
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Create Grayscale version
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Separate channels (OpenCV loads as B, G, R)
b, g, r = cv.split(image)

# Create a 2x3 figure
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Display RGB
axes[0, 0].imshow(image_rgb)
axes[0, 0].set_title('RGB Image')

# Display Red Channel
axes[0, 1].imshow(r, cmap='gray')
axes[0, 1].set_title('Red Channel')

# Display Green Channel
axes[0, 2].imshow(g, cmap='gray')
axes[0, 2].set_title('Green Channel')

# Display Blue Channel
axes[1, 0].imshow(b, cmap='gray')
axes[1, 0].set_title('Blue Channel')

# Display Grayscale
axes[1, 1].imshow(image_gray, cmap='gray')
axes[1, 1].set_title('Grayscale Image')

# Display Unconverted BGR (will look weird with swapped colors)
axes[1, 2].imshow(image)
axes[1, 2].set_title('Unconverted BGR Display')

# Hide axes for all subplots
for ax in axes.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()

# Convert Center Pixel's RGB to HEX
center_rgb_pixel = image_rgb[y_center, x_center]
# Format as #RRGGBB
hex_value = '#{:02x}{:02x}{:02x}'.format(center_rgb_pixel[0], center_rgb_pixel[1], center_rgb_pixel[2])

print("\n--- Step 4: Color Analysis ---")
print(f"Center Pixel (RGB): {center_rgb_pixel}")
print(f"Center Pixel HEX Code: {hex_value}")


# ==========================================
# Step 5: Crop, Resize, and Save
# ==========================================
# Define coordinates for crop (starting at y=50, x=50)
y_start, x_start = 50, 50
y_end, x_end = y_start + 100, x_start + 100

# Crop the region
cropped_image = image[y_start:y_end, x_start:x_end]
print("\n--- Step 5: Crop and Resize ---")
print(f"Cropped Image Shape: {cropped_image.shape}")

# Resize to 200x200
resized_image = cv.resize(cropped_image, (200, 200))

# Display Original, Crop, and Resized side by side
fig2, axes2 = plt.subplots(1, 3, figsize=(15, 5))

axes2[0].imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
axes2[0].set_title('Original Image')

axes2[1].imshow(cv.cvtColor(cropped_image, cv.COLOR_BGR2RGB))
axes2[1].set_title('100x100 Crop')

axes2[2].imshow(cv.cvtColor(resized_image, cv.COLOR_BGR2RGB))
axes2[2].set_title('200x200 Resized')

for ax in axes2:
    ax.axis('off')

plt.tight_layout()
plt.show()

# Convert the resized image back to BGR and save it
# (Since OpenCV works in BGR natively, resized_image is already in BGR, 
# but we follow the manual's instruction strictly)
resized_rgb = cv.cvtColor(resized_image, cv.COLOR_BGR2RGB)
resized_bgr_to_save = cv.cvtColor(resized_rgb, cv.COLOR_RGB2BGR)

save_success = cv.imwrite('resized_crop.png', resized_bgr_to_save)
print(f"Did cv.imwrite save the file successfully? {save_success}")


# ==========================================
# Step 6: Create a Histogram
# ==========================================
# Flatten the grayscale image
flattened_gray = image_gray.ravel()

plt.figure(figsize=(10, 5))
# Plot 256-bin histogram
plt.hist(flattened_gray, bins=256, range=(0, 256), color='black', alpha=0.8)
plt.title('Grayscale Image Histogram')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency (Number of Pixels)')

# Save the plot
plt.savefig('grayscale_histogram.png')
plt.show()

print("\n--- Step 6: Histogram ---")
print("Histogram saved as 'grayscale_histogram.png'.")
print("Explanation: The histogram indicates that the image is predominantly bright, which is evidenced by the massive spike in pixel frequency on the far right side (around intensity levels 220-230). There is also a noticeable presence of darker pixels (a smaller peak around level 30-40), but the mid-tones are relatively sparse. Overall, the image exhibits high contrast with a strong leaning towards bright highlights rather than being mainly dark or perfectly balanced.")


# ==========================================
# Step 7: Demonstrate Bit Depth
# ==========================================
# Create an 8-bit horizontal gradient from 0 to 255
gradient_8bit = np.linspace(0, 255, 256, dtype=np.uint8)
# Make it a 2D image (100 rows tall) so we can display it
gradient_8bit_2d = np.tile(gradient_8bit, (100, 1)) 

# Function to quantize an image
def quantize(image, bits):
    levels = 2**bits
    step_size = 256 // levels
    return (image // step_size) * step_size

# Apply quantization
quant_1bit = quantize(gradient_8bit_2d, 1)
quant_2bit = quantize(gradient_8bit_2d, 2)
quant_4bit = quantize(gradient_8bit_2d, 4)

# Display all four
fig3, axes3 = plt.subplots(4, 1, figsize=(10, 8))

axes3[0].imshow(gradient_8bit_2d, cmap='gray', aspect='auto')
axes3[0].set_title('Original 8-bit (256 levels)')

axes3[1].imshow(quant_1bit, cmap='gray', aspect='auto')
axes3[1].set_title('1-bit (2 levels)')

axes3[2].imshow(quant_2bit, cmap='gray', aspect='auto')
axes3[2].set_title('2-bit (4 levels)')

axes3[3].imshow(quant_4bit, cmap='gray', aspect='auto')
axes3[3].set_title('4-bit (16 levels)')

for ax in axes3:
    ax.axis('off')

plt.tight_layout()
plt.show()

# Print unique counts
print("\n--- Step 7: Bit Depth ---")
print(f"Unique values in 8-bit: {len(np.unique(gradient_8bit_2d))}")
print(f"Unique values in 1-bit: {len(np.unique(quant_1bit))}")
print(f"Unique values in 2-bit: {len(np.unique(quant_2bit))}")
print(f"Unique values in 4-bit: {len(np.unique(quant_4bit))}")