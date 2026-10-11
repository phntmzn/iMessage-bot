import subprocess


def send_message(phone_number, message):
    """
    Send a message through the macOS Messages app using AppleScript.

    Args:
        phone_number (str): Recipient's phone number or reachable address.
        message (str): Text of the message to send.
    """

    # Define an AppleScript command to interact with Messages.
    # The phone number and message are inserted into the script.
    applescript = f'''
    tell application "Messages"
        -- Select the first iMessage account.
        set targetService to 1st account whose service type = iMessage

        -- Identify the recipient using their phone number.
        set targetBuddy to participant "{phone_number}" of targetService

        -- Send the message to the recipient.
        send "{message}" to targetBuddy
    end tell
    '''

    # Execute AppleScript through macOS's osascript utility.
    result = subprocess.run(
        ["osascript", "-e", applescript],
        capture_output=True,  # Capture standard output and errors.
        text=True             # Return output as strings.
    )

    # Check whether AppleScript executed successfully.
    if result.returncode == 0:
        print("Message sent successfully.")
    else:
        # Display the error if the command failed.
        print("Error:", result.stderr)


if __name__ == "__main__":
    # Specify the recipient's phone number.
    recipient = "+15551234567"

    # Define the message to send.
    message = "Hello from Python and AppleScript!"

    # Send the message.
    send_message(recipient, message)
