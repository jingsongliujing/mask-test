input_dict = {"image": test_img_path}

# 口罩检测预测
results = module.face_detection(data=input_dict, use_multi_scale=True, shrink=0.6,)
for result in results:
    print(result)

# 预测结果展示
img = mpimg.imread("detection_result/kze.jpg")
plt.figure(figsize=(10,10))
plt.imshow(img) 
plt.axis('off') 
plt.show()
