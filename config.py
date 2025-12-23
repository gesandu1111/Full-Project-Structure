# ===============================
# SYSTEM CONFIGURATION FILE
# ===============================

# ---- AI SETTINGS ----
OPENAI_API_KEY = "sk-your-openai-api-key-here"  # Replace with your actual key
AI_MODEL = "gpt-4o-mini"
AI_TEMPERATURE = 0.7
AI_MAX_TOKENS = 500

# ---- SYSTEM SETTINGS ----
SYSTEM_NAME = "Local AI System"
SYSTEM_VERSION = "1.0.0"
DEFAULT_USER = "local_user"

# ---- MEMORY SETTINGS ----
DB_NAME = "memory.db"
MEMORY_CONTEXT_LIMIT = 5      # How many past messages AI sees
MEMORY_MAX_MESSAGES = 1000

# ---- SECURITY / LIMITS ----
ENABLE_COMMANDS = True
ENABLE_MEMORY = True

# ---- DEBUG ----
DEBUG = True
