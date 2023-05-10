def hide_text(secret_text):
    cover_text = '''A poor Brahmin lived in a village all alone. He had no friends or relatives. He was known for being stingy and he used to beg for a living. The food he got as alms were kept in an earthen pot which was hung beside his bed. This allowed him to easily access the food when he got hungry.'''

    # Split the cover text into individual words
    words = cover_text.split()

    # Ensure the secret text can fit within the cover text
    if len(words) < len(secret_text):
        raise ValueError("Cover text is too short to hide the secret text.")

    # Replace the first letter of each word with the corresponding character from the secret text
    stego_words = []
    for i, word in enumerate(words):
        if i < len(secret_text):
            first_letter = secret_text[i]
            modified_word = first_letter + word[1:]
            stego_words.append(modified_word)
        else:
            pass

    # Join the stego words to form the stego text
    stego_text = ' '.join(stego_words)

    return stego_text


def reveal_text(stego_text):
    # Split the stego text into individual words
    words = stego_text.split()

    # Extract the first letters from each word to reveal the secret text
    secret_text = ''
    for word in words:
        secret_text += word[0]

    return secret_text


# # Example usage
# cover_text = "The quick brown fox jumps over the lazy dog."
# secret_text = "HELLO"
#
# # Hide the secret text in the cover text
# stego_text = hide_text(secret_text)
# print("Stego text:", stego_text)
#
# # Reveal the secret text from the stego text
# revealed_text = reveal_text(stego_text)
# print("Revealed text:", revealed_text)
