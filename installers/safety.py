"""Obvious secret/state checks shared by installation and repository validation."""

import re

FORBIDDEN_PARTS = {
    ".git", ".ssh", ".aws", "cache", "cookies", "logs", "sessions", "session",
    "replay", "state", "node_modules", "venv", ".venv", "__pycache__", "browser_profiles",
}
FORBIDDEN_NAMES = {
    ".netrc", ".npmrc", "auth.json", "credentials.json", "secrets.json", "tokens.json",
    "state.db", "cases.jsonl", "id_rsa", "id_ed25519",
}
FORBIDDEN_SUFFIXES = (
    ".db", ".db-wal", ".db-shm", ".db-journal", ".sqlite", ".sqlite3", ".sqlite-wal",
    ".sqlite-shm", ".sqlite-journal", ".sqlite3-wal", ".sqlite3-shm", ".sqlite3-journal",
    ".jsonl", ".log", ".pem", ".key", ".p12", ".pfx", ".pyc",
)
TOKEN_PATTERNS = {
    "openrouter key": re.compile(rb"\bsk-or-v1-[A-Za-z0-9_-]{20,}\b"),
    "openai key": re.compile(rb"\bsk-(?!or-v1-)[A-Za-z0-9_-]{20,}\b"),
    "telegram bot token": re.compile(rb"\b[0-9]{7,12}:[A-Za-z0-9_-]{30,}\b"),
    "private key": re.compile(rb"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    "private machine path": re.compile(rb"(?i)(?:/home/" + rb"hermes/|C:[\\/]Users[\\/]typakon4[\\/])"),
}


def forbidden_filename(relative):
    parts = [part.lower() for part in relative.parts]
    name = parts[-1]
    return (any(part in FORBIDDEN_PARTS for part in parts)
            or name in FORBIDDEN_NAMES or name.startswith((".env", "id_rsa", "id_ed25519"))
            or re.search(r"(^|[._-])cookies?([._-]|$)", name)
            or name.endswith(FORBIDDEN_SUFFIXES))


def suspicious_content(content):
    return [label for label, pattern in TOKEN_PATTERNS.items() if pattern.search(content)]
