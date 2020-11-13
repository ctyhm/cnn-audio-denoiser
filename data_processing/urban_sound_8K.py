import pandas as pd
import numpy as np
import os

np.random.seed(999)


class UrbanSound8K:
    #初始化，入参[路径，数据集大小，噪声类别（0-9）]
    def __init__(self, basepath, *, val_dataset_size, class_ids=None):
        self.basepath = basepath
        self.val_dataset_size = val_dataset_size
        self.class_ids = class_ids

    #获取噪声数据集，
    def _get_urban_sound_8K_filenames(self):
        urbansound_metadata = pd.read_csv(os.path.join(self.basepath, 'metadata', 'UrbanSound8K_0_5.csv'))

        # shuffle the dataframe #打乱数据，先随机生成索引，再按照索引重新排序
        urbansound_metadata.reindex(np.random.permutation(urbansound_metadata.index))

        return urbansound_metadata

    #通过类别获取噪声数据
    def _get_filenames_by_class_id(self, metadata):

        if self.class_ids is None:
            self.class_ids = np.unique(metadata['classID'].values) #unique去重
            print("Number of classes:", self.class_ids)

        all_files = []
        file_counter = 0
        for c in self.class_ids:
            per_class_files = metadata[metadata['classID'] == c][['slice_file_name', 'fold']].values
            per_class_files = [os.path.join(self.basepath, 'audio', 'fold' + str(file[1]), file[0]) for file in
                               per_class_files]
            print("Class c:", str(c), 'has:', len(per_class_files), 'files')
            file_counter += len(per_class_files)
            all_files.extend(per_class_files)

        assert len(all_files) == file_counter
        return all_files

    #获取训练数据集和验证数据集
    def get_train_val_filenames(self):
        urbansound_metadata = self._get_urban_sound_8K_filenames()

        # folds from 0 to 9 are used for training
        urbansound_train = urbansound_metadata[urbansound_metadata.fold != 10]

        urbansound_train_filenames = self._get_filenames_by_class_id(urbansound_train)
        np.random.shuffle(urbansound_train_filenames)

        # separate noise files for train/validation
        urbansound_val = urbansound_train_filenames[-self.val_dataset_size:]
        urbansound_train = urbansound_train_filenames[:-self.val_dataset_size]
        print("Noise training:", len(urbansound_train))
        print("Noise validation:", len(urbansound_val))

        return urbansound_train, urbansound_val

    #获取测试数据集
    def get_test_filenames(self):
        urbansound_metadata = self._get_urban_sound_8K_filenames()

        # fold 10 is used for testing only
        urbansound_train = urbansound_metadata[urbansound_metadata.fold == 10]

        urbansound_test_filenames = self._get_filenames_by_class_id(urbansound_train)
        np.random.shuffle(urbansound_test_filenames)

        print("# of Noise testing files:", len(urbansound_test_filenames))
        return urbansound_test_filenames
