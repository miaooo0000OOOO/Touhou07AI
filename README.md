# Touhou07AI

## 使用yolo5和DQN玩东方妖妖梦

+ 通过python脚本提取游戏中的图像，使用opencv进行图像切割，取游戏的主画面。

+ 通过labelimg数据标注平台，标注游戏画面的检测框。检测框的类别只包含三种，即玩家、弹幕和分数点。

+ 将已标注的数据交给yolov5进行训练。Yolov5训练完毕后，将其输出的提取框作为强化学习模型（DQN）的输入。

+ 其包含目前帧以及上几帧的候选框以便强化学习模型判断弹幕运动轨迹。

+ 通过获取游戏内得分作为强化学习模型的分数，进行训练。
