
import scipy.io.wavfile as wavfile
from estimate_bpm import BPM_Analyzer
import os
import librosa

audio_path = './audio'

input_file = os.listdir(audio_path)

bpms = BPM_Analyzer()
print('{0:<23} {1:<14} {2:<24}'.format('File name','BPM wdt','BPM librosa') )

for i in range(len(input_file)):
    rate, signal = wavfile.read(audio_path + '/' + input_file[i])
    signal = signal.flatten()
    bpm = bpms.computeWindowBPM(signal,rate)
    samples, sample_rate = librosa.load(audio_path + '/' + input_file[i])
    onset_env = librosa.onset.onset_strength(samples, sr=sample_rate)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sample_rate)

    print('{0:<23} {1:<14} {2:<24}'.format(input_file[i],str(bpm),str(tempo)))