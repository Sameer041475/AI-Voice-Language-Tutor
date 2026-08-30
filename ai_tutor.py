import requests
import json


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:latest"


def analyze_sentence(sentence, language="English"):

    prompt = f"""
You are an expert {language} language tutor.

The learner said:

"{sentence}"

Analyze the sentence and help the learner improve.

Return ONLY valid JSON using exactly this structure:

{{
    "corrected_sentence": "corrected sentence here",

    "grammar_mistakes": [
        {{
            "mistake": "incorrect part",
            "correction": "correct part",
            "explanation": "simple explanation"
        }}
    ],

    "vocabulary_feedback": "feedback about vocabulary",

    "overall_feedback": "overall feedback",

    "grammar_score": 0,
    "vocabulary_score": 0,
    "overall_score": 0,

    "difficulty": "Beginner"
}}

Rules:

1. Do not unnecessarily change the meaning.
2. If the sentence is already correct, keep it unchanged.
3. Give simple explanations.
4. Scores must be between 0 and 10.
5. Difficulty must be Beginner, Intermediate, or Advanced.
6. Return ONLY JSON.
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "format": "json",
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return json.loads(result["response"])

    except requests.exceptions.ConnectionError:

        return {
            "error": (
                "Could not connect to Ollama. "
                "Make sure Ollama is running."
            )
        }

    except Exception as e:

        return {
            "error": str(e)
        }