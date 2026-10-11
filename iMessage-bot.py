import subprocess

def send_message(phone_number, message):
    applescript = f'''
    tell application "Messages"
        set targetService to 1st account whose service type = iMessage
        set targetBuddy to participant "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''

    result = subprocess.run(
        ["osascript", "-e", applescript],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("Message sent successfully.")
    else:
        print("Error:", result.stderr)


if __name__ == "__main__":
    recipient = "+15551234567"
    message = "Hello from Python and AppleScript!"

    send_message(recipient, message)
