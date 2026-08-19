import subprocess, webbrowser, time, os
subprocess.Popen(["python", "-m", "uvicorn", "main:app", "--port", "8000"], cwd="backend")
time.sleep(1)
webbrowser.open("file://" + os.path.abspath("frontend/index.html"))
