from google.cloud import texttospeech
from google.cloud import vision
from playsound import playsound
import io
import os

def detect_text(path):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print(texts)

    final_text = texts[0].description
    #for text in texts:
     #   print('\n"Hello{}"'.format(text.description))
      #  final_text+=" "+text.description

    print(final_text)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.types.SynthesisInput(text=final_text)
    print(synthesis_input)
    voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    	out.write(response.audio_content)
    	print('Audio content written to file "output.mp3"')

    playsound('output.mp3')
    os.remove('output.mp3')
