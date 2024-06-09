import speech_recognition as sr
import googletrans
from googletrans import Translator

def speech_to_text_translator():
    """
    Translates speech to text and then translates the text to another language.
    """

    # Initialize speech recognizer
    r = sr.Recognizer()

    # Get audio from microphone
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    try:
        # Recognize speech
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Initialize translator
        translator = Translator()

        # Get target language from user
        target_language = input("Enter target language code (e.g., 'es' for Spanish): ")

        # Translate text
        translation = translator.translate(text, dest=target_language)

        # Print translation
        print("Translation: " + translation.text)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    speech_to_text_translator()