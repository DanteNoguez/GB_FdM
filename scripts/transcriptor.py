
import whisper
from whisper.utils import write_vtt, write_txt

def transcript(modelo, audio, language, vtt_file, txt_file):
  model = whisper.load_model(modelo)
  audio = audio
  results = model.transcribe(audio, language=language)
  with open(vtt_file, "w") as txt:
    write_vtt(results["segments"], file=txt)
  with open(txt_file, "w") as txt:
    write_txt(results["segments"], file=txt)

def demo(file_name):
  with open(file_name, "r") as txt:
    print('\n'.join(txt.readlines()))

def typos(file_name, prev, new):
  with open(file_name, 'r') as file:
    filedata = file.read()
  filedata = filedata.replace(prev, new)
  with open(file_name, 'w') as file:
    file.write(filedata)
