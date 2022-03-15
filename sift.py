#%%

import cv2 
import matplotlib.pyplot as plt


# read images
img1 = cv2.imread('img1.jpg')  
img2 = cv2.imread('img2.jpg') 

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#sift
sift = cv2.SIFT_create()

keypoints_1, descriptors_1 = sift.detectAndCompute(img1_gray,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2_gray,None)

#feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)

img1_sift = cv2.drawKeypoints(img1_gray,keypoints_1,img1)
img2_sift = cv2.drawKeypoints(img2_gray,keypoints_2,img2)
cv2.imwrite('sift_keypoints1.jpg',img1_sift)
cv2.imwrite('sift_keypoints2.jpg',img2_sift)

img3 = cv2.drawMatches(img1_gray, keypoints_1, img2_gray, keypoints_2, matches[:50], img2_gray, flags=2)
plt.imshow(img3),plt.show()

