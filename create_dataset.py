from data_processing.mozilla_common_voice import MozillaCommonVoiceDataset
from data_processing.urban_sound_8K import UrbanSound8K
from data_processing.dataset import Dataset
import warnings

warnings.filterwarnings(action='ignore')

# mozilla_basepath = '/home/thallessilva/Documents/datasets/en'
mozilla_basepath = './home/en'
urbansound_basepath = './home/UrbanSound8K'
# urbansound_basepath = '/home/thallessilva/Documents/datasets/UrbanSound8K'

#纯净语音数据集 ，大小1000
mcv = MozillaCommonVoiceDataset(mozilla_basepath, val_dataset_size=1000)
# mcv = MozillaCommonVoiceDataset(mozilla_basepath, val_dataset_size=1000)
clean_train_filenames, clean_val_filenames = mcv.get_train_val_filenames()

us8K = UrbanSound8K(urbansound_basepath, val_dataset_size=200)
noise_train_filenames, noise_val_filenames = us8K.get_train_val_filenames()

windowLength = 256
config = {'windowLength': windowLength, # 窗口长度
          'overlap': round(0.25 * windowLength),#步长 = 0.25 * 窗口长度
          'fs': 16000, #采样率，16kHz,每秒采样16000个点
          'audio_max_duration': 0.8} #最大持续时间0.8s = 800ms
# val_dataset = Dataset(clean_val_filenames, noise_val_filenames, **config)
# # val_dataset.create_tf_record(prefix='val', subset_size=1000)
# val_dataset.create_tf_record(prefix='val', subset_size=2000)

#
train_dataset = Dataset(clean_train_filenames, noise_train_filenames, **config)
# train_dataset.create_tf_record(prefix='train', subset_size=2000)
train_dataset.create_tf_record(prefix='train', subset_size=1000)

# Create Test Set
# clean_test_filenames = mcv.get_test_filenames()
#
# noise_test_filenames = us8K.get_test_filenames()
#
# test_dataset = Dataset(clean_test_filenames, noise_test_filenames, **config)
# # test_dataset.create_tf_record(prefix='test', subset_size=500, parallel=False)
# test_dataset.create_tf_record(prefix='test', subset_size=1000, parallel=False)

