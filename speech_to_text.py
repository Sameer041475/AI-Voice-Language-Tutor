from faster_whisper import WhisperModel


# Load Whisper model once
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path, language="en"):

    segments, info = model.transcribe(
        audio_path,

        # Tell Whisper exactly which language
        language=language,

        # Transcription, not translation
        task="transcribe",

        # Better decoding
        beam_size=5,

        # Detect speech and remove silence
        vad_filter=True,

        vad_parameters={
            "min_silence_duration_ms": 500
        },

        # Important for preventing hallucinations
        condition_on_previous_text=False,

        # Don't accept extremely unlikely text
        compression_ratio_threshold=2.4,
        log_prob_threshold=-1.0,
        no_speech_threshold=0.6,

        # Don't randomly generate different results
        temperature=0
    )

    text = " ".join(
        segment.text.strip()
        for segment in segments
    )

    return text.strip()