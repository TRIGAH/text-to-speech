from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")  # This command plays the generated audio using mpg123
    os.remove("output.mp3")  # Remove the temporary audio file after playing

if __name__ == "__main__":
    text = input("Enter the text to convert to speech: ")
    text_to_speech(text)
