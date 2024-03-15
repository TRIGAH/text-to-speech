from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")  # Save the speech as an MP3 file

    # Play the speech using the default media player
    if os.name == 'nt':  # For Windows
        os.system("start output.mp3")
    elif os.name == 'posix':  # For Linux/Mac OS
        os.system("xdg-open output.mp3")
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)
