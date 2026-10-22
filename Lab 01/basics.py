# Digital Image Processing Lab - Lab Task 01
# Name: Syeda Khadija Hassan | Roll No: 2024-SE-09
# File: basics.py - Basic Python exercises

# ---------------------------------------------------------
# Exercise 1: Variables and Data Types
# ---------------------------------------------------------
print("=== Exercise 1: Variables and Data Types ===")
width = 640
height = 480
image_name = "sample.png"
is_color = True

print("width =", width, "| type:", type(width))
print("height =", height, "| type:", type(height))
print("image_name =", image_name, "| type:", type(image_name))
print("is_color =", is_color, "| type:", type(is_color))

total_pixels = width * height
print("Total number of pixels:", total_pixels)  # Expected: 307200

# ---------------------------------------------------------
# Exercise 2: if, elif, and else
# ---------------------------------------------------------
print("\n=== Exercise 2: if, elif, and else ===")
test_values = [-1, 0, 127, 128, 255, 256]

for intensity in test_values:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"
    print(intensity, "->", label)

# ---------------------------------------------------------
# Exercise 3: for and while Loops
# ---------------------------------------------------------
print("\n=== Exercise 3: for and while Loops ===")

# for loop: visit each pixel value and label it (threshold = 128)
for pixel in [20, 130, 255]:
    if pixel >= 128:
        print(pixel, "->", "Bright pixel")
    else:
        print(pixel, "->", "Dark pixel")

# while loop: print 0, 1, 2 and stop before 3
counter = 0
while counter < 3:
    print("counter =", counter)
    counter = counter + 1  # update the loop counter

# ---------------------------------------------------------
# Exercise 4: Functions
# ---------------------------------------------------------
print("\n=== Exercise 4: Functions ===")


def is_bright(pixel, threshold=128):
    if pixel >= threshold:
        return True
    return False


print("is_bright(127) =", is_bright(127))        # Expected: False
print("is_bright(128) =", is_bright(128))        # Expected: True
print("is_bright(200, 210) =", is_bright(200, 210))  # Expected: False

# ---------------------------------------------------------
# Exercise 5: Lists and Tuples
# ---------------------------------------------------------
print("\n=== Exercise 5: Lists and Tuples ===")
pixels = [0, 128, 255]
print("First item:", pixels[0])

pixels[1] = 150      # replace the middle item
pixels.append(64)    # add a new item at the end
print("List:", pixels)           # Expected: [0, 150, 255, 64]
print("Length:", len(pixels))    # Expected: 4

size = (640, 480)
width, height = size  # tuple unpacking
print("width =", width)
print("height =", height)

# Why can a list item be changed but a tuple item cannot?
# A list is mutable: it is stored so its elements can be modified, added or
# removed in place (e.g. pixels[1] = 150). A tuple is immutable: once created,
# its elements cannot be reassigned, so size[0] = 100 would raise a TypeError.
# Tuples are therefore safe for fixed values such as an image's (width, height).

# ---------------------------------------------------------
# Exercise 6: Dictionaries and Sets
# ---------------------------------------------------------
print("\n=== Exercise 6: Dictionaries and Sets ===")
image = {"width": 640, "height": 480}
image["mode"] = "RGB"  # add a new key
print("Width:", image["width"])
print("Mode:", image["mode"])

labels = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels)  # a set removes duplicates
print("Unique labels:", unique_labels)
print("Number of unique labels:", len(unique_labels))  # Expected: 3

