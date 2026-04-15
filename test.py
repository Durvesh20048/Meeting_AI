from STT import transcribe_audio
from analyzer import analyze_text

text = transcribe_audio("meeting.wav")

print("\n--- TRANSCRIPT ---")
print(text)

result = analyze_text(text)

print("\n--- ANALYSIS ---")
print(result)