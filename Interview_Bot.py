import openai
import speech_recognition as sr
import googletrans
from googletrans import Translator
from gtts import gTTS
import os
import tempfile
import numpy as np
import io
from pydub import AudioSegment
from IPython.display import Audio
import tempfile
import pygame
import requests
import time
# Set up OpenAI API key
openai.api_key = "Your API Key here"

# Set up the recognizer and the microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Set up the translator
translator = Translator()

def choose_languages():
    user_language = input("Enter user language code (e.g. 'en' for English, 'es' for Spanish): ")
    bot_language = input("Enter bot language code (e.g. 'en' for English, 'es' for Spanish): ")
    slow_bot = input("Enter 'Yes' if you would like the patient to speak slowly. Otherwise, enter 'No'")
    return user_language, bot_language, slow_bot

def listen_and_recognize(language):
    while True:
        print("Listening...")

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=10)

        try:
            text = recognizer.recognize_google(audio, language=language)
            print("You said: ", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio. Retrying...")
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout. Retrying...")


def translate_text(text, language, max_retries=3, delay_between_retries=5):
    translator = Translator()
    translated_text = ""
    retries = 0

    while retries <= max_retries:
        try:
            translated_text = translator.translate(text, dest=language).text
            return translated_text
        except Exception as e:
            retries += 1
            print(f"Translation attempt {retries} failed. Error: {str(e)}. Retrying in {delay_between_retries} seconds...")
            time.sleep(delay_between_retries)

    print("translation failed after all retries")
    return text  # Return the original text if translation fails after all retries




def generate_response(messages, user_role, bot_role):
    while True:
        try:
            system_message = {
                "role": "system",
                "content": f"You are playing the role of a {bot_role}. You should assume the part of your role, including any assumptions about age, educational level, and general demeanor. You should respond accordingly to the user's questions and statements based on their role, including assumptions about age, educational level, and demeanor."
            }
            
            messages.insert(0, system_message)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response_text = response['choices'][0]['message']['content'].strip()
            return response_text
        except Exception as e:
            print(f"Error occurred while generating response: {e}. Retrying...")



def text_to_speech(text, language, slow_bot, tld='com'):
    if slow_bot == "Yes":                 
        tts = gTTS(text=text, lang=language, slow=True, tld=tld)
    else:
        tts = gTTS(text=text, lang=language, slow=False, tld=tld)
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio_file.name)
    temp_audio_file.close()  # Close the temporary file before loading with pygame

    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_file.name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()  # Unload the music before deleting the file
    os.unlink(temp_audio_file.name)


def main():
    # Initialize the list of messages
    messages = []

    # Choose user and bot languages
    user_language, bot_language, slow_bot = choose_languages()

    while True:
        # Listen to user input in the specified language
        user_input = listen_and_recognize(user_language)

        if user_input:

            # Specify the illness
            bot_role = "The Patient"
            user_role = "The Doctor"

            # Translate user input to bot language
            translated_input = translate_text(user_input, language = "en")
            # Add user input to the list of messages
            messages.append({"role": f"user", "content": translated_input})
            print("Translated text: ", translator.translate(translated_input, dest="en").text)

            # Generate GPT-3.5 Turbo response
            gpt_response = generate_response(messages, user_role, bot_role)

            # Add AI response to the list of messages
            messages.append({"role": "assistant", "content": gpt_response})

            # Translate GPT-3.5 Turbo response back to the user language
            translated_response = translate_text(gpt_response, language = bot_language)
            print("Bot Response: ", translated_response)
            print("Translated text: ", gpt_response)

            # Convert the translated response to speech
            text_to_speech(text = translated_response, language=bot_language, slow_bot=slow_bot)
        else:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()