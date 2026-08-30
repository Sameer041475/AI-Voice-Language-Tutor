import streamlit as st
from audio_recorder_streamlit import audio_recorder
import tempfile
import os

from speech_to_text import transcribe_audio
from ai_tutor import analyze_sentence
from text_to_speech import text_to_speech

from database import (
    create_database,
    save_session,
    get_sessions,
    get_average_scores
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Voice Language Tutor",
    page_icon="🎙️",
    layout="wide"
)


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

create_database()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("🎙️ AI Language Tutor")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Practice",
        "📊 Progress",
        "📚 History"
    ]
)


# ==================================================
# PRACTICE PAGE
# ==================================================

if page == "🏠 Practice":

    st.title("🎙️ AI Voice Language Tutor")

    st.write(
        "Speak in your target language and "
        "get instant AI-powered feedback."
    )

    st.divider()

    # --------------------------------------------------
    # LANGUAGE
    # --------------------------------------------------

    language = st.selectbox(
        "🌍 Select Language",
        [
            "English",
            "Hindi",
            "Spanish",
            "French",
            "German"
        ]
    )

    # --------------------------------------------------
    # DIFFICULTY
    # --------------------------------------------------

    difficulty = st.selectbox(
        "🎯 Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    st.divider()

    # --------------------------------------------------
    # RECORD AUDIO
    # --------------------------------------------------

    st.subheader("🎤 Speak Your Sentence")

    st.write(
        "Click the microphone button and speak."
    )

    audio_bytes = audio_recorder(
        text="Click to Record",
        recording_color="#e74c3c",
        neutral_color="#3498db",
        icon_name="microphone",
        icon_size="2x"
    )

    # --------------------------------------------------
    # AUDIO PROCESSING
    # --------------------------------------------------

    if audio_bytes:

        st.audio(
            audio_bytes,
            format="audio/wav"
        )

        # Save recorded audio temporarily

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp_audio:

            temp_audio.write(audio_bytes)

            audio_path = temp_audio.name

        # --------------------------------------------------
        # LANGUAGE CODES
        # --------------------------------------------------

        language_codes = {
            "English": "en",
            "Hindi": "hi",
            "Spanish": "es",
            "French": "fr",
            "German": "de"
        }

        whisper_language = language_codes[language]

        # --------------------------------------------------
        # SPEECH TO TEXT
        # --------------------------------------------------

        with st.spinner(
            "🎧 Converting speech to text..."
        ):

            transcript = transcribe_audio(
                audio_path,
                whisper_language
            )

        # Delete temporary audio

        os.remove(audio_path)

        # --------------------------------------------------
        # DISPLAY TRANSCRIPTION
        # --------------------------------------------------

        st.subheader("📝 You Said")

        st.info(transcript)

        # --------------------------------------------------
        # AI ANALYSIS
        # --------------------------------------------------

        with st.spinner(
            "🤖 AI is analyzing your sentence..."
        ):

            feedback = analyze_sentence(
                transcript,
                language
            )

        # --------------------------------------------------
        # ERROR HANDLING
        # --------------------------------------------------

        if "error" in feedback:

            st.error(
                feedback["error"]
            )

        else:

            # --------------------------------------------------
            # CORRECTED SENTENCE
            # --------------------------------------------------

            st.subheader(
                "✍️ Corrected Sentence"
            )

            corrected_sentence = feedback[
                "corrected_sentence"
            ]

            st.success(
                corrected_sentence
            )

            # --------------------------------------------------
            # SCORES
            # --------------------------------------------------

            st.subheader("📊 Your Score")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Grammar",
                f"{feedback['grammar_score']}/10"
            )

            col2.metric(
                "Vocabulary",
                f"{feedback['vocabulary_score']}/10"
            )

            col3.metric(
                "Overall",
                f"{feedback['overall_score']}/10"
            )

            # --------------------------------------------------
            # GRAMMAR
            # --------------------------------------------------

            st.subheader(
                "📚 Grammar Mistakes"
            )

            mistakes = feedback[
                "grammar_mistakes"
            ]

            if mistakes:

                for mistake in mistakes:

                    st.error(
                        f"❌ {mistake['mistake']}"
                    )

                    st.success(
                        f"✅ {mistake['correction']}"
                    )

                    st.write(
                        f"💡 {mistake['explanation']}"
                    )

            else:

                st.success(
                    "🎉 No grammar mistakes!"
                )

            # --------------------------------------------------
            # VOCABULARY
            # --------------------------------------------------

            st.subheader(
                "📖 Vocabulary Feedback"
            )

            st.write(
                feedback[
                    "vocabulary_feedback"
                ]
            )

            # --------------------------------------------------
            # OVERALL FEEDBACK
            # --------------------------------------------------

            st.subheader(
                "💬 Overall Feedback"
            )

            st.write(
                feedback[
                    "overall_feedback"
                ]
            )

            # --------------------------------------------------
            # TEXT TO SPEECH
            # --------------------------------------------------

            st.subheader(
                "🔊 Correct Pronunciation"
            )

            try:

                audio_file = text_to_speech(
                    corrected_sentence,
                    language
                )

                st.audio(
                    audio_file,
                    format="audio/mp3"
                )

            except Exception as e:

                st.warning(
                    f"TTS error: {e}"
                )

            # --------------------------------------------------
            # SAVE PROGRESS
            # --------------------------------------------------

            save_session(
                language,
                transcript,
                corrected_sentence,
                feedback["grammar_score"],
                feedback["vocabulary_score"],
                feedback["overall_score"],
                feedback["difficulty"]
            )

            st.success(
                "✅ Your session has been saved!"
            )


# ==================================================
# PROGRESS PAGE
# ==================================================

elif page == "📊 Progress":

    st.title("📊 Learning Progress")

    average_scores = get_average_scores()

    grammar_avg = average_scores[0]
    vocabulary_avg = average_scores[1]
    overall_avg = average_scores[2]

    if overall_avg is None:

        st.info(
            "No learning sessions yet. "
            "Complete your first practice session!"
        )

    else:

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Grammar",
            f"{grammar_avg:.1f}/10"
        )

        col2.metric(
            "Vocabulary",
            f"{vocabulary_avg:.1f}/10"
        )

        col3.metric(
            "Overall",
            f"{overall_avg:.1f}/10"
        )

        st.divider()

        st.subheader(
            "🎯 Current Level"
        )

        if overall_avg < 5:

            st.warning(
                "Beginner"
            )

        elif overall_avg < 7.5:

            st.info(
                "Intermediate"
            )

        else:

            st.success(
                "Advanced"
            )


# ==================================================
# HISTORY PAGE
# ==================================================

elif page == "📚 History":

    st.title("📚 Practice History")

    sessions = get_sessions()

    if not sessions:

        st.info(
            "No practice sessions yet."
        )

    else:

        for session in sessions:

            (
                session_id,
                language,
                sentence,
                corrected,
                grammar,
                vocabulary,
                overall,
                difficulty,
                created_at
            ) = session

            with st.expander(
                f"{language} | "
                f"Score: {overall}/10 | "
                f"{created_at}"
            ):

                st.write(
                    "**You said:**"
                )

                st.info(sentence)

                st.write(
                    "**Corrected:**"
                )

                st.success(corrected)

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Grammar",
                    f"{grammar}/10"
                )

                col2.metric(
                    "Vocabulary",
                    f"{vocabulary}/10"
                )

                col3.metric(
                    "Overall",
                    f"{overall}/10"
                )

                st.write(
                    f"**Difficulty:** {difficulty}"
                )