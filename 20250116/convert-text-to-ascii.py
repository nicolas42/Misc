# Define the text
text = "Actually this is not the text above haha!"

# Convert each character in the text to its ASCII value
ascii_values = [ord(char) for char in text]

# Join the ASCII values into a space-separated string (optional)
ascii_string = " ".join(map(str, ascii_values))

# Print the ASCII representation
print(ascii_string)
