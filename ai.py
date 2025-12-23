import openai
from config import OPENAI_API_KEY, AI_MODEL, AI_TEMPERATURE, AI_MAX_TOKENS, MEMORY_CONTEXT_LIMIT, ENABLE_MEMORY
from memory import add_message, get_recent_messages

openai.api_key = OPENAI_API_KEY

def ask_ai(user_input):
    messages = []

    # Include memory context
    if ENABLE_MEMORY:
        memory_messages = get_recent_messages(MEMORY_CONTEXT_LIMIT)
        messages.extend(memory_messages)

    # Add current user input
    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.chat.completions.create(
            model=AI_MODEL,
            messages=messages,
            temperature=AI_TEMPERATURE,
            max_tokens=AI_MAX_TOKENS
        )
        ai_text = response.choices[0].message["content"].strip()

        # Save both user and AI messages to memory
        if ENABLE_MEMORY:
            add_message("user", user_input)
            add_message("assistant", ai_text)

        return ai_text

    except Exception as e:
        return f"AI ERROR: {str(e)}"
