import json
import requests


def stream_local_response(model, messages):
    print(f"Sending request to local LLM with model: {model} and messages: {messages}")
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": messages,
            "stream": True
        },
        stream=True
    )
    print(f"Response status code: {response.status_code}")


    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "message" in data:
                yield data.get("message", {}).get("content", "")
