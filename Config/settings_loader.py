from dotenv import load_dotenv
import os

load_dotenv()

# SQL Server settings (Windows Auth)
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")

# Embedding model
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")  # Default fallback

# OpenAI key (if used later)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)