# A Fully Convolutional Neural Network for Speech Enhancement

Tensorflow 2.0 implementation of the paper [A Fully Convolutional Neural Network for Speech Enhancement](https://pdfs.semanticscholar.org/9ed8/e2f6c338f4e0d1ab0d8e6ab8b836ea66ae95.pdf)

Blog post: [Practical Deep Learning Audio Denoising](https://medium.com/better-programming/practical-deep-learning-audio-denoising-79c1c1aea299)

## Dataset

Part of the dataset used to train the original system is now [available to download](cdn.daitan.com/dataset.zip).
The zip file contains 1 training file (that is 10% of the data used to train the system), a validation file, and two 
audio files (not included in the training files) used to evaluate the model. 

You can create the dataset for yourself. 

- Download the [Mozilla Common Voice](https://voice.mozilla.org/) and [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html) datasets.
- Use the ```create_dataset.py``` script to create the TFRecord files.

## 流程说明

### 1.造数据

- create_dataset.py是入口，先设置滑窗、步长、最大时长和数据集大小等参数，然后分别造训练train、验证val、测试test的tfrecords数据集。并获取纯净语音和噪声的语音文件列表
- 获取语音文件列表从data_processing/mozilla_common_voice.py中获取纯净语音数据文件，具体获取哪些文件从配置文件train.tsv和test.tsv中读取每一行的文件名和存放路径
- 从urban_sound_8K.py中读取噪声数据，同样在配置文件UrbanSound8K_0_5.csv中获取语音文件名和路径
- 类比上述获取文件的方式，自己写了一个lntu.py的类，从lntu文件夹中获取姜老师录的噪声数据

#### 获取到语音数据的列表后开始创建tfrecords文件

- 拿创建训练集来说，调用data_processing/dataset.py 的create_tf_record方法，先按照设置的subset_size一次使用多少个语音文件创建tfrecords数据集。查看是否已经创建，如未创建第【i,i+subset_size】个文件的数据集就新建文件处理这一批次的文件
- 先按顺序将纯净语音文件取出来，核心处理方法是data_processing/dataset.py的parallel_audio_processing()方法。通过删除空白帧，加噪（随机加噪和顺序加噪两种）等一系列操作返回（None,129）的数据格式，一个语音按照最大时长进行限制切分的帧数，如果是0.8s就切分成201帧
- 将所获取的加噪语音帧存入tfrecords里

## 训练数据

- SpeechDenoiserCNN.ipynb 是训练的部分，打开jupyter notebook 直接执行训练即可
- 详细注解请看SpeechDenoiserCNN.ipynb文件内部

