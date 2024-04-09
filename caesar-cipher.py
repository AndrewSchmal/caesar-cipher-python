def shift_letters(text, shift):
    """
    Shifts the letters in the given text by the specified number of spaces.
    
    Parameters:
    - text (str): The text to be encoded.
    - shift (int): The number of spaces to shift the letters.
    
    Returns:
    - str: The encoded text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    return result

def unshift_letters(text, shift):
    """
    Unshifts the letters in the given text by the specified number of spaces.
    
    Parameters:
    - text (str): The text to be decoded.
    - shift (int): The number of spaces to unshift the letters.
    
    Returns:
    - str: The decoded text.
    """
    return shift_letters(text, -shift)

def main():
    # Ask the user if they want to encode or decode
    action = input("Do you want to encode (scramble) or decode (unscramble)? Enter 'encode' or 'decode': ")
    
    # Ask the user for the number of spaces to shift
    shift = int(input("Enter how many times the letters should be shifted: "))
    
    # Ask the user for the text to be encoded or decoded
    text_to_process = input("Enter the text to encode or decode: ")
    
    # Process the text based on the user's choice
    if action.lower() == 'encode':
        processed_text = shift_letters(text_to_process, shift)
        print(f"Encoded text (shifted {shift} characters): {processed_text}")
    elif action.lower() == 'decode':
        processed_text = unshift_letters(text_to_process, shift)
        print(f"Decoded text (shifted {shift} characters): {processed_text}")
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
