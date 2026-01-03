import sys
import requests
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # points to ai-automation/
data_dir = BASE_DIR / "basics"
data_dir.mkdir(exist_ok=True)

# 1. Print Python version
print("Python version:", sys.version)

# 2. Write a text file
input_file = data_dir / "input.txt"
input_file.write_text("This is a test input file.\n", encoding="utf-8")

# 3. Read the text file
content = input_file.read_text(encoding="utf-8")
print("File content:", content.strip())

# 4. HTTP GET request to a public API
response = requests.get("https://api.github.com")
response.raise_for_status()

# 5. Parse JSON
data = response.json()
api_status = {
    "current_user_url": data.get("current_user_url"),
    "rate_limit_url": data.get("rate_limit_url")
}

# 6. Save output to a file
output_file = data_dir / "api_output.json"
output_file.write_text(json.dumps(api_status, indent=2), encoding="utf-8")
print(f"Saved API output to: {output_file}")
