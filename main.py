import os
# One-liner entry (71 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "To fix any bug, just delete the code. No code, no bug. You are welcome."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
