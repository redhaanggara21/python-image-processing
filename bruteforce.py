import cv2
from matplotlib import pyplot as plt

# Load two images
image1 = cv2.imread('./archive/home/1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('./archive/home/2.jpg', cv2.IMREAD_GRAYSCALE)

# Create ORB detector
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors for both images
keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

# Create a Brute-Force Matcher
bf = cv2.BFMatcher()

# Match descriptors
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Apply ratio test to filter matches
good_matches = []
for m, n in matches:
    if m.distance < 0.5 * n.distance:
        good_matches.append(m)

# Draw matches
matched_image = cv2.drawMatches(image1, keypoints1, 
                        image2, keypoints2, good_matches, None)

# Display the original image with keypoints marked
plt.figure(figsize = (14, 10))
plt.imshow(matched_image) 
plt.title('Image mathching with Brute-Force method')
plt.show()