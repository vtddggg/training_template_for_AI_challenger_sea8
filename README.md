

# 中文版 | [English](https://github.com/vtddggg/training_template_for_AI_challenger_sea8/blob/main/README_EN.md)

为了更好的研究以数据为中心的鲁棒机器学习，我们公开了初赛/复赛的测试集合，供大家使用：

初赛测试集：https://drive.google.com/file/d/1CtK2tkYncn5uX4OJH4QQAFO_NN6ocEzy/view?usp=sharing

复赛测试集：https://drive.google.com/file/d/1ZofA9X2cMtGC7fXA7_Qrr-1KhL3fo3u-/view?usp=sharing

## 使用方法

该代码是[AAAI2022 安全AI挑战者计划第八期：Data-Centric Robust Learning on ML Models](https://tianchi.aliyun.com/competition/entrance/531939/introduction)复赛阶段的训练示例。选手可简单的使用以下两条命令训练`wideresnet`以及`preactresnet18`模型：

```
git clone https://github.com/vtddggg/training_template_for_AI_challenger_sea8.git && cd training_template_for_AI_challenger_sea8
sh train.sh
```
运行完成后，会在当前路径下产生`Dataset.zip`文件，选手可直接上传该文件作为官方提供的baseline成绩

## 创建自己的提交
选手必须提交一个压缩包（包含`data.npy`, `label.npy`, `config.py`, `wideresnet.pth.tar`以及`preactresnet18.pth.tar`），这5个文件分别通过以下步骤生成：

1. `data.npy`, `label.npy`, `config.py`三个文件可由选手自己创建和修改，作为自定义的训练数据和config，但需要满足[赛题](https://tianchi.aliyun.com/competition/entrance/531939/information)中给出的限制。除了训练数据和config，另外在`training_template_for_AI_challenger_sea8`目录下的训练代码`.py`文件均固定，不可擅自改动。

2. 将以上三个文件替换到training_template_for_AI_challenger_sea8中，执行`sh train.sh`训练

3. 训练完毕后，将生成的`Dataset.zip`提交至比赛页面

需要注意的是，在测试提交结束后，我们会验证选手的训练结果，因此，请时刻注意压缩包中的`wideresnet.pth.tar`和`preactresnet18.pth.tar`确实是由对应的`data.npy`, `label.npy`, `config.py`训练生成的


**感谢大家的参与，最后预祝各位参赛选手取得好成绩！**
