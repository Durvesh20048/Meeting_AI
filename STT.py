import os
import uuid
import whisper

model = whisper.load_model("base")

def convert_to_wav(input_file):
    os.makedirs("audio_files", exist_ok=True)

    unique_name = f"{uuid.uuid4()}.wav"
    output_path = os.path.join("audio_files", unique_name)

    os.system(f'ffmpeg -i "{input_file}" "{output_path}" -y')

    return output_path


def transcribe_audio(file_path):
    if not file_path.endswith(".wav"):
        file_path = convert_to_wav(file_path)

    result = model.transcribe(file_path)
    return result["text"]