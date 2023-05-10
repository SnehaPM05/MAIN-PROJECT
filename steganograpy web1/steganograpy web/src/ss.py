
def hide_text(secret_text, cover_text):
    # Convert the secret text to binary
    binary_secret = ''.join(format(ord(char), '08b') for char in secret_text)

    # Embed the secret text in the cover text
    stego_text = ''
    cover_index = 0
    for bit in binary_secret:
        cover_char = cover_text[cover_index]
        stego_char = cover_char[:-1] + bit  # Replace the least significant bit of the cover character
        stego_text += stego_char
        cover_index += 1
        if cover_index >= len(cover_text):
            break

    # Append the remaining cover text
    stego_text += cover_text[cover_index:]

    return stego_text


def reveal_text(stego_text):
    # Extract the embedded secret text from the stego text
    binary_secret = ''
    for char in stego_text:
        binary_secret += char[-1]  # Extract the least significant bit

    # Convert binary back to text
    secret_text = ''
    for i in range(0, len(binary_secret), 8):
        char = binary_secret[i:i+8]
        secret_text += chr(int(char, 2))

    return secret_text


# Example usage
cover_text = "This is a cover text. This is a cover text.This is a cover text.This is a cover text.This is a cover text.This is a cover text."
secret_text = "This"

# Hide the secret text in the cover text
stego_text = hide_text(secret_text, cover_text)
print("Stego text:", stego_text)

# Reveal the secret text from the stego text
revealed_text = reveal_text(stego_text)
print("Revealed text:", revealed_text)