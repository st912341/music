import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Text to speech
text = text = """Table of Content
How Much Should a Small Business Spend on Marketing?
Small Business Marketing Budget Planning: Key Considerations
How to Create a Marketing Budget for a Small Business
Best Way to Allocate a Marketing Budget Effectively
Small Business Advertising Costs 2025: What to Expect
Using a Marketing Budget Template for Small Businesses
Conclusion"""

engine.say(text)

# Wait for completion
engine.runAndWait()
