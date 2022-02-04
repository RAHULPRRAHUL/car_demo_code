<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""

@author: rahul
"""

import cv2
folder_path = 'D:\\segmentation\\car_segmentation\\output\\'
filepath = 'two-cars-in-driveway-gettyimages-1200x630.jpg'
fullpath = folder_path + filepath 
image = cv2.imread(fullpath,0)
# Window name in which image is displayed
window_name = 'image'
cv2.imshow(window_name, image)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

 
         
ret,thresh1 = cv2.threshold(image,50,255,cv2.THRESH_BINARY)


window_name = 'image'
cv2.imshow(window_name, thresh1)
cv2.waitKey(0) 
=======
# -*- coding: utf-8 -*-
"""

@author: rahul
"""

import cv2
folder_path = 'D:\\segmentation\\car_segmentation\\output\\'
filepath = 'two-cars-in-driveway-gettyimages-1200x630.jpg'
fullpath = folder_path + filepath 
image = cv2.imread(fullpath,0)
# Window name in which image is displayed
window_name = 'image'
cv2.imshow(window_name, image)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

 
         
ret,thresh1 = cv2.threshold(image,50,255,cv2.THRESH_BINARY)


window_name = 'image'
cv2.imshow(window_name, thresh1)
cv2.waitKey(0) 
>>>>>>> 5eb14467b305d63c7ae7aed1d69a21484fd8bd76
cv2.destroyAllWindows() 