import os,  sys
from pydub import AudioSegment
import os.path
from collections import OrderedDict


if len(sys.argv) < 2:
    print ('Error: Wrong usage\nUsage: python3 OGG_to_WAV.py {ogg_folder_name}}')  
    sys.exit()
    
    
ogg_folder_name = str(sys.argv[1]) 

ogg_path = os.path.join(os.getcwd(), ogg_folder_name)

# print(ogg_path)

def create_wav_folder(path):
    isExist = os.path.exists(path)
    if not isExist:
       # Create a new directory because it does not exist
       os.makedirs(path)
    return path


def convert_to_wav(ogg_path):
    file_name = ogg_path.split(chr(92))[-1]
    # print(file_name)
    try:
        aud = AudioSegment.from_ogg(ogg_path)
        wav  = f'{wav_path}\\{file_name}.wav'
        #print(wav_path)
        aud.export(wav, format="wav")
    except:
        pass


wav_path = create_wav_folder(f'{ogg_path.split("OGG_Files")[0]}WAV_Files')
# print(wav_path)

for i in os.listdir(ogg_path):
    convert_to_wav(f"{ogg_path}\{i}")
    print("File successfully converted")