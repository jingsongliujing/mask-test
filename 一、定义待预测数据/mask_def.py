# 待预测图片
test_img_path = ["./kze.jpg"]


import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 

img = mpimg.imread(test_img_path[0]) 

# 展示待预测图片
plt.figure(figsize=(10,10))
plt.imshow(img) 
plt.axis('off') 
plt.show()
