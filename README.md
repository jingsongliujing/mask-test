# mask-test
基于飞桨的口罩检测能力

“控制传染源、切断传播途径和排查易感人群”是打赢抗疫的三种手段。
其中切断传播途径中，佩戴口罩已经几乎成为了最重要的举措之一。 
但是在实际场景中，仍然有不重视、不注意、侥幸心理的人员不戴口罩，尤其在公众场合，给个人和公众造成极大的风险隐患。
目前，仅有少数厂商能够提供口罩佩戴人脸检测AI模型的相关商业化方案，且在密集人流下的识别效果参差不齐。
而由于缺乏数据集和模型开发经验，更多中小开放商在面临园区、关口等细分场景时，更是无从下手。
我运用百度免费开源自研的“口罩人脸识别”预训练模型，基于此预训练模型，我仅需使用少量自有数据，便可快速完成自有场景模型开发。
飞桨预训练模型管理与迁移学习工具PadddleHub已提供PyramidBox预训练模型(pyramidbox_lite_mobile_mask/pyramidbox_lite_server_mask)用于一键检测人们是否佩戴口罩。
同时PaddleHub还提供了飞桨生态下的高质量预训练模型，涵盖了图像分类、目标检测、词法分析、语义模型、情感分析、视频分类、图像生成、图像分割、文本审核、关键点检测等主流模型。


注：如果您在本地运行该项目示例，需要首先安装PaddleHub。部署的时候记得换成清华源，否则下载速度十分慢
我以linux环境作为教程来讲解。

pip install --upgrade paddlehub -i https://pypi.tuna.tsinghua.edu.cn/simple

一、定义待预测数据
新建一个文件夹test_mask_detection.png为待预测图片文件夹
若是待预测图片存放在一个文件中，当然也要创建一个文本文件test.txt。

cat test.txt



二、加载预训练模型
PaddleHub口罩检测提供了两种预训练模型，pyramidbox_lite_mobile_mask和pyramidbox_lite_server_mask。
不同点在于，pyramidbox_lite_mobile_mask是针对于移动端优化过的模型，适合部署于移动端或者边缘检测等算力受限的设备上。


三、预测
PaddleHub对于支持一键预测的module，可以调用module的相应预测API，完成预测功能。




如果想要实现通过视频轴帧实时预测，建议先用cv2读入图片帧，之后调用预测接口。本地软件集成可以用这种方式。这样方式也可以加快预测。同时这种方式会直接返回预测结果在图片中的位置，不会将预测结果写入图片。

代码如下：

import cv2

# 读入图片
test_img_datas = [cv2.imread(img) for img in test_img_path]
# 预测
results = module.face_detection(data={"data":test_img_datas})
for result in results:
    print(result)
    
    
    
    
    
 四、部署服务器
借助 PaddleHub，服务器端的部署也非常简单，直接用一条命令行在服务器启动口罩人脸检测与分类模型就行了：

$ hub serving start -m pyramidbox_lite_server_mask -p 8866



只要在服务器端完成部署，剩下在客户端调用就不会有多大问题了。当然我也没有试过移动端啦，就不细说了。




五、移动端部署

在移动端部署口罩人脸检测及分类模型，也只需要三步：①下载预测库，Paddle Lite 会提供编译好的预测库；②优化模型，使用 model_optimize_tool 工具实现模型优化；③通过预测 API 实现调用。


























