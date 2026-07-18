# GitHub Copilot / AI Agent Guide for gabotkom

## What this repository is

`gabotkom` is a Spanish-language intelligent training platform for corporate safety courses. It combines a Streamlit frontend with a small AI prompt layer and course content for a learning experience focused on fire prevention and other safety topics.

## Key files and structure

- `gabotkom.py`
  - Primary Streamlit UI and session flow for participant onboarding, diagnosis, and lesson progression.
- `ia.py`
  - OpenAI/GROQ client wrapper and prompt loader.
  - Uses `GROQ_API_KEY` environment variable.
- `prompts/prompt_sistema.txt`
  - System prompt that defines the AI persona and hard rules.
  - This file is critical: do not break its constraints when changing AI behavior.
- `curso.py`
  - Course metadata for the current lesson, keyword-based answer validation, and lesson text.
- `validador.py`
  - Simple keyword matcher used to validate participant responses.
- `reglas.py`
  - Rule configuration for permitted conversation topics.
- `cursos/`
  - Course content and stimuli files, currently including `cursos/incendios/leccion1.md` and `preguntas.json`.

## How to run

Typical local execution is via Streamlit:

```bash
streamlit run gabotkom.py
```

If the AI integration is used, ensure:

- `GROQ_API_KEY` is set in the environment
- `ia.py` remains pointing to `https://api.groq.com/openai/v1`

## Agent guidance

When editing or extending this repository, keep these points in mind:

- The product is a training instructor, not a general chatbot.
- The AI prompt is intentionally strict: it must stay on course topics and avoid sports, politics, religion, entertainment, and unrelated conversation.
- Spanish is the default language of the UI, prompts, and course content.
- The core app is stateful; `st.session_state` is used to track the participant journey.
- The current validation is keyword-based, so new learning modules should also define clear `palabras_clave` or similar expected responses.

## Good first enhancements

- Add support for additional courses in `cursos/` and update the UI selection in `gabotkom.py`.
- Improve the AI prompt and validation flow in `ia.py`, `curso.py`, and `validador.py`.
- Add a dedicated `README` section or `docs/` page with setup and deployment details.
- Preserve the existing course safety rules when introducing new features.

## Notes for Copilot-style agents

- Prefer changes that keep the current project’s Spanish training focus.
- Use `AGENTS.md` as the authoritative agent instruction file for this repo.
- Do not create conflicting `.github/copilot-instructions.md` unless the repo later needs a second agent guidance layer.

## Changed files

- `AGENTS.md`: Added repository-specific AI agent guidance and run context.
