import numpy as np
# train_specturm = np.random.rand(129,201)
# val_specturm = np.random.rand(129,201)
# clean_phase = np.angle(train_specturm)
# noise_phase = np.angle(val_specturm)
# clean_magnitude = np.abs(train_specturm)
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