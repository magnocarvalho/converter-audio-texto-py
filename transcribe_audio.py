from pydub import AudioSegment
from google.cloud import speech
import io

# Função para converter mp3 para wav
def convert_mp3_to_wav(mp3_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    wav_path = mp3_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path
# Defina o caminho para sua API key JSON do Google Cloud
google_api_key_path = "google-api.json"

# Caminho para o arquivo de áudio
audio_path = "audio1.mp3"
# Caminho para o arquivo de saída de texto
output_text_path = "transcricao1.txt"

wav_path = convert_mp3_to_wav(audio_path)

# Inicializar o cliente do Google Cloud Speech
client = speech.SpeechClient.from_service_account_json(google_api_key_path)

# Carregar o arquivo de áudio
audio = AudioSegment.from_wav(wav_path)

# Dividir o áudio em partes menores (10 MB cada, aproximadamente 1 minuto de áudio)
segment_length_ms = 60000  # 60 segundos
segments = [audio[i:i + segment_length_ms] for i in range(0, len(audio), segment_length_ms)]

# Função para transcrever um segmento de áudio
def transcribe_segment(segment):
    audio_bytes = segment.raw_data
    audio = speech.RecognitionAudio(content=audio_bytes)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=segment.frame_rate,
        language_code="pt-BR",
    )

    response = client.recognize(config=config, audio=audio)

    if response.results:
        return response.results[0].alternatives[0].transcript
    return ""

# Transcrever todos os segmentos
transcriptions = []
for i, segment in enumerate(segments):
    print(f"Transcrevendo segmento {i + 1}/{len(segments)}...")
    transcription = transcribe_segment(segment)
    transcriptions.append(transcription)

# Salvar a transcrição em um arquivo de texto
full_transcription = "\n".join(transcriptions)
with open(output_text_path, "w") as file:
    file.write(full_transcription)

print(f"Transcrição salva em: {output_text_path}")