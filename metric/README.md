
## 使用
（前提是根据说明安装依赖的第三方库）

1. 拷贝生成的文件和参考的文件到output文件夹，修改metric_main.py文件中hypothesis_path和references_path

2. 在根目录执行python metric_main.py命令

## 安装第三方库
### 安装
安装在pip公共库中的三方包

pip install -r requirements.txt

安装nlg-eval

pip install git+git://github.com/Maluuba/nlg-eval.git@master

或者参考这篇文章，先从GitHub clone，然后执行安装命令https://blog.csdn.net/tandelin/article/details/103664721
## 用到的评测库介绍
#### nlg-eval

用来评测meteor、rough

https://github.com/Maluuba/nlg-eval

#### sacrebleu

用来评测bleu

https://github.com/mjpost/sacrebleu

#### py-rouge

用来评测rouge指标

https://github.com/Diego999/py-rouge

