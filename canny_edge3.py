import cv2

image_path = r'C:\Users\user\Desktop\pr\pic.jpg'  

img = cv2.imread(image_path)
resize=cv2.resize(img,(650,500))
cv2.imshow('orginal_image', resize)

gray=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,50,100)
cv2.imshow('canny_edge_detection',canny)
cv2.waitKey(0)