from PIL import Image

# Load the image
img = Image.open("image.jpg")

# Convert the image to grayscale
gray_img = img.convert('L')

# Create a mask
mask = gray_img.point(lambda x: 0 if x<100 else 255, '1')

# Apply the mask
img.putalpha(mask)

# Save the image
img.save("image-no-bg.png", "PNG")