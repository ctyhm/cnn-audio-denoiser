import numpy as np
# train_specturm = np.random.rand(129,201)
# val_specturm = np.random.rand(129,201)
# clean_phase = np.angle(train_specturm)
# noise_phase = np.angle(val_specturm)
# clean_magnitude = np.abs(train_specturm)
'''
noise_stft_mag_features = np.array([1]*201*129*8*1)
clean_stft_magnitude = np.array([2]*201*129*1)
noise_stft_phase = np.array([3]*201*129)
noise_stft_mag_features = noise_stft_mag_features.reshape((201,129,8,1))
clean_stft_magnitude = clean_stft_magnitude.reshape((201,129,1))
noise_stft_phase = noise_stft_phase.reshape((201,129))
print(noise_stft_mag_features.shape)
print(clean_stft_magnitude.shape)
print(noise_stft_phase.shape)

for x_, y_, p_ in zip(noise_stft_mag_features, clean_stft_magnitude, noise_stft_phase):
    print(x_.shape)
    print(y_.shape)
    print(p_.shape)
    print(x_)
    print(y_)
    print(p_)
'''


# print(clean_magnitude.shape)
# print(np.mean(clean_magnitude))
# print(np.std(clean_magnitude))
# sum = 0
# for i in range(clean_magnitude.shape[0]):
#     for j in range(clean_magnitude.shape[1]):
#         sum = sum + clean_magnitude[i][j]
# print(sum/clean_magnitude.shape[0]/clean_magnitude.shape[1])

'''
aaa = clean_magnitude[:,0:7]
print(aaa.shape)
print(aaa[0:2])
print(clean_magnitude[0:2,7:9])
bbb=np.concatenate([aaa[0:2, 0:8 - 1], clean_magnitude[0:2,7:9]], axis=1)
print(bbb)
print(bbb.shape)

    print('=================start=================')
    print('=================clean_phase=================')
    print(clean_phase.min())
    print('=================noise_phase=================')
    print(noise_phase.min())
    result = clean_magnitude * np.cos(clean_phase - noise_phase)
    print('=================clean_magnitude=================')
    print(clean_magnitude)
    print('=================result=================')
    print(result)
    print('=================end=================')

'''

# import os
# import librosa
# def read_audio(filepath, sample_rate, normalize=True):
#     """Read an audio file and return it as a numpy array"""
#     audio, sr = librosa.load(filepath, sr=sample_rate)
#     if normalize:
#       div_fac = 1 / np.max(np.abs(audio)) / 3.0
#       audio = audio * div_fac
#     return audio, sr
#
# cleanAudio, sr = read_audio(os.path.join('./dataset/en', 'test', 'common_voice_zh-CN_18531539.mp3'), sample_rate=16000)
# # cleanAudio, sr = read_audio(os.path.join(mozilla_basepath, 'test', 'common_voice_en_16526.mp3'), sample_rate=fs)
# print("Min:", np.min(cleanAudio),"Max:",np.max(cleanAudio))
# print(cleanAudio.shape)

from keras.models import load_model
import wave
import struct
from scipy import *
import pyworld as pw
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import os
import soundfile as sf

# 读取wav文件E:\python_demo\cnn-audio-denoiser\dataset\UrbanSound8K\test\50-1_3_Point1.wav
root_wavs = 'E:/python_demo/cnn-audio-denoiser/dataset/UrbanSound8K/test/'
names = os.listdir(root_wavs)

len(names)

cnt = 0
plt.figure(figsize=(20, 20))
for name in names:
    wav_name = root_wavs + name
    x, fs = sf.read(wav_name)
    f0, sp, ap = pw.wav2world(x, fs)
    cnt += 1

    plt.subplot(3, 4, cnt)
    plt.plot(f0)
    plt.imshow(np.log(sp), cmap='hot')
plt.show()



