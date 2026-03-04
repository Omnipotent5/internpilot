import subprocess
import sys

task = " ".join(sys.argv[1:])

cmd = [
    "aider",
    "--model",
    "ollama/deepseek-coder:6.7b",
    "--message",
    task,
]

subprocess.run(cmd)