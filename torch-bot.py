import subprocess
import torch
import torch.nn as nn


# Define a simple neural network using PyTorch.
class MessageModel(nn.Module):
    def __init__(self, input_size=10, hidden_size=16, output_size=2):
        super().__init__()

        # Fully connected layers.
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size)
        )

    def forward(self, x):
        # Pass the input through the neural network.
        return self.network(x)


def send_message(phone_number, message):
    """
    Send a message through the macOS Messages app using AppleScript.

    Args:
        phone_number (str): Recipient's phone number or reachable address.
        message (str): Text of the message to send.
    """

    # Define an AppleScript command to interact with Messages.
    applescript = f'''
    tell application "Messages"
        -- Select the first iMessage account.
        set targetService to 1st account whose service type = iMessage

        -- Identify the recipient.
        set targetBuddy to participant "{phone_number}" of targetService

        -- Send the message.
        send "{message}" to targetBuddy
    end tell
    '''

    # Execute AppleScript through macOS's osascript utility.
    result = subprocess.run(
        ["osascript", "-e", applescript],
        capture_output=True,
        text=True
    )

    # Check whether the command succeeded.
    if result.returncode == 0:
        print("Message sent successfully.")
    else:
        print("Error:", result.stderr)


if __name__ == "__main__":
    # Initialize the PyTorch model.
    model = MessageModel()

    # Create a sample input tensor.
    sample_input = torch.randn(1, 10)

    # Run inference without calculating gradients.
    with torch.no_grad():
        prediction = model(sample_input)

    # Display the neural network's output.
    print("PyTorch model output:", prediction)

    # Specify the recipient.
    recipient = "+15551234567"

    # Define the message.
    message = "Hello from Python, PyTorch, and AppleScript!"

    # Send the message through macOS Messages.
    send_message(recipient, message)
