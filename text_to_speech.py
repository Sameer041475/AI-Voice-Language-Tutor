from gtts import gTTS
import os


LANGUAGE_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de"
}


def text_to_speech(text, language="English"):

    language_code = LANGUAGE_CODES.get(
        language,
        "en"
    )

    output_file = "audio/corrected_sentence.mp3"

    # Create audio folder if it doesn't exist
    os.makedirs("audio", exist_ok=True)

    tts = gTTS(
        text=text,
        lang=language_code,
        slow=False
    )

    tts.save(output_file)

    return output_file