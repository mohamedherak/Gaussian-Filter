import cv2
from skimage import io, img_as_float
from skimage.filters import gaussian


img_salt_pepper_noise = img_as_float(io.imread('shoreline.jpg',as_gray=True))

img = img_salt_pepper_noise

gaussian_using_cv2 = cv2.GaussianBlur(img, (5,5), 0, borderType=cv2.BORDER_CONSTANT)

gaussian_using_skimage = gaussian(img, sigma=1, mode='constant', cval=0.0)

#sigma defines the std dev of the gaussian kernel. Slightly different than how we define in cv2


cv2.imshow("Original", img)
cv2.imshow("Using cv2 gaussian", gaussian_using_cv2)
cv2.imshow("Using skimage", gaussian_using_skimage)

cv2.waitKey(0)          
cv2.destroyAllWindows() 
