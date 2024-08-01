import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
# models = TTS().list_models().list_models()
# for model in models:
#     print(model)

# Running a multi-speaker and multi-lingual model
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
# text = "Thanks for reading this article. I hope you learned something."
# text = "感謝您閱讀本文。我希望你學到了一些東西。"
# speaker_wav = "./audio-sample/zh-sample.wav"
# print("start tts")
# wav = tts.tts(text="Hello world!", speaker_wav=speaker_wav, language="en")  # amplitude values
# tts.tts_to_file(text=text, speaker_wav=speaker_wav, language="zh", file_path="output.wav")  # to a file

# Example voice conversion
tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24").to(device)
tts.voice_conversion_to_file(source_wav="./audio-sample/zh-sample.wav", target_wav="./audio-sample/en-sample.wav",
                             file_path="output.wav")
