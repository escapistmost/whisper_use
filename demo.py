import whisper_use

print(whisper_use.detect_text('audio1.m4a'))
print(whisper_use.detect_language('audio1.m4a'))
print(whisper_use.detect_text_from_mel('audio1.m4a'))