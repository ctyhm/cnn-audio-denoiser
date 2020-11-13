import pandas as pd
import numpy as np
import os

np.random.seed(999)

class MozillaCommonVoiceDataset:

    #初始化，入参[路径，数据集大小]
    def __init__(self, basepath, *, val_dataset_size):
        self.basepath = basepath
        self.val_dataset_size = val_dataset_size

    #获取文件，根据train.tsv文件中的文件名获取语音训练数据
    def _get_common_voice_filenames(self, dataframe_name='train.tsv'):
        mozilla_metadata = pd.read_csv(os.path.join(self.basepath, dataframe_name), sep='\t')
        clean_files = mozilla_metadata['path'].values
        np.random.shuffle(clean_files)
        print("Total number of training examples:", len(clean_files))
        return clean_files

    #获取训练和验证文件，根据上面的函数分别取出训练样本和验证样本
    def get_train_val_filenames(self):
        clean_files = self._get_common_voice_filenames(dataframe_name='train.tsv')

        # resolve full path
        clean_files = [os.path.join(self.basepath+'/', 'clips/', filename) for filename in clean_files]

        clean_files = clean_files[:-self.val_dataset_size]
        clean_val_files = clean_files[-self.val_dataset_size:]
        print("# of Training clean files:", len(clean_files))
        print("# of  Validation clean files:", len(clean_val_files))
        return clean_files, clean_val_files

    #获取测试样本
    def get_test_filenames(self):
        clean_files = self._get_common_voice_filenames(dataframe_name='test.tsv')

        # resolve full path
        clean_files = [os.path.join(self.basepath+'/', 'clips/', filename) for filename in clean_files]

        print("# of Testing clean files:", len(clean_files))
        return clean_files