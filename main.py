from email.mime import text
import os
from time import time
from dotenv import load_dotenv

from slack_bolt import App, SayStream, BoltContext, SetStatus

from slack_sdk import WebClient
from slack_bolt.adapter.socket_mode import SocketModeHandler

import re
import llm_functions

load_dotenv()


print("Loaded environment variables:")
print(f"SLACK_DM_SOCKET_TOKEN: {os.getenv('SLACK_DM_SOCKET_TOKEN')}")
print(f"SLACK_BOT_TOKEN: {os.getenv('SLACK_BOT_TOKEN')}")

app = App(token=os.getenv("SLACK_BOT_TOKEN"))


@app.message("hello")
def message_hello(message, say):
    print(f"Received a message: {message}")
    say(f"Hello there <@{message['user']}>!")


@app.command("/cal")
def command_hello(ack, respond, command):
    print(f"Received command: {command}")
    ack()
    try:
        pattern = re.compile(
            r'(?P<date>\b(?:\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4})\b)?.*?'
            r'(?P<time>\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\b)?.*?'
            r'(?:in\s+)?(?P<location>[A-Z][a-zA-Z\s,.-]+)?'
        )        
        match = pattern.search(command['text'])
        if match:
            date = match.group('date') or 'unspecified date'
            time = match.group('time') or 'unspecified time'
            location = match.group('location') or 'unspecified location'
            response = f"Got it - {match.groupdict()}"
        else:
            response = "Sorry, I couldn't parse the date, time, and location from your command."
    except Exception as e:
        response = f"An error occurred while processing your command: {str(e)}"
    respond(response)

@app.event('message')
def handle_message_event(body, say):
    print(f"Received a message event: {body}")
    say(f"Received a message: {body['event']['text']}")

@app.event("app_mention")
def handle_app_mention_event(
    client: WebClient, 
    event: dict, 
    context: BoltContext, 
    say_stream: SayStream, 
    set_status: SetStatus
):
    try:
        # Clean the input text
        text = event.get("text", "")
        cleaned_text = re.sub(r"<@[A-Z0-9]+>", "", text).strip()
        thread_ts = event.get("thread_ts") or event["ts"]

        if not cleaned_text:
            return

        set_status('is thinking...')

        # Initialize the Slack stream
        stream = say_stream()

        # Call your local Ollama stream function
        # It yields strings directly based on your logic: yield data.get("message", {}).get("content", "")
        resp_stream = llm_functions.stream_local_response(
            "llama3.1",
            [{"role": "user", "content": cleaned_text}]
        )

        for content_chunk in resp_stream:
            # Append the string chunk directly to Slack
            stream.append(markdown_text=content_chunk)

        # Finalize the stream
        stream.stop()


    except Exception as e:
        print(f"Error: {e}")
        client.chat_postMessage(
            channel=context.channel_id, 
            text=f":warning: Local LLM Error: {e}", 
            thread_ts=event.get("ts")
        )


SocketModeHandler(app, os.getenv("SLACK_DM_SOCKET_TOKEN")).start()