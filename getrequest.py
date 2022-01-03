import os, subprocess, time, json

def get_request(url):
    output = subprocess.Popen(["curl", url], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    content = output.stdout.read().decode("utf-8").strip()
    if not content:
        raise Exception(
            f"Invalid URL: '{url}'"
        )
    if content.startswith("{") and content.endswith("}"):
        return json.loads(content)
    return content

print(get_request("http://localhost:5000/"))