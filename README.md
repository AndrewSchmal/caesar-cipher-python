## Introduction
Welcome to the Caesar Cipher Python tool! This simple yet powerful tool allows you to encode and decode messages using the Caesar cipher, a classic substitution cipher that has been used for centuries. Whether you're testing cipher solutions or just exploring the world of encryption, this tool is perfect for you. :D


## Caesar Cipher - Python
This Python tool lets you encode or decode messages using the Caesar cipher, a simple yet effective substitution cipher that shifts letters in the alphabet by a set number. Perfect for checking cipher solutions or just for fun (I made this to double check a Cryptography assignment for my ITIS-3200 Intro to Information Security and Privacy class).

## What's a Substitution Cipher?
A substitution cipher replaces plaintext letters with ciphertext letters based on a fixed system. The Caesar cipher is a classic, shifting letters by a certain number of positions. 


# What is the Caesar Cipher?

The Caesar cipher is a type of substitution cipher named after Julius Caesar, who is believed to have used it to communicate confidential information. In the Caesar cipher, each letter in the plaintext is shifted a fixed number of positions down or up the alphabet.

For example, with a shift of 3 (which is a common choice in Caesar ciphers), 'A' would become 'D', 'B' would become 'E', and so on. If we reach the end of the alphabet, we wrap around to the beginning.

There is a table representing the changes of this logic at the bottom of this readme if you want a visual of it.



# Features
This app has two functions, encoding text and decoding text. For my app, encoding text is "scrambling text", and decoding text is "unscrambling text". This allows you to check your Caesar ciphers both ways to make sure you've got it right.


Encode Text: Shift letters in a given text forward by a specified number of spaces.

Decode Text: Shift letters in a given text backward by a specified number of spaces to decode it.

## Usage

1. Clone the repo to your local machine.

2. Run the app.
   
3. Follow the prompts to enter the number of spaces to shift and the text to encode or decode.

# Example Output
Do you want to encode (scramble) or decode (unscramble)? Enter 'encode' or 'decode': encode

Enter how many times the letters should be shifted: 3

Enter the text to encode or decode: Squid Games!

Encoded text (shifted 3 characters): Vtxlg Jdphv!

## Logic Table

| The regular ol' alphabet  | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Shift 1 | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A |
| Shift 2 | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B |
| Shift 3 | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |
| Shift 4 | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D |
| Shift 5 | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E |
| Shift 6 | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F |
| Shift 7 | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G |
| Shift 8 | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H |
| Shift 9 | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I |
| Shift 10 | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J |
| Shift 11 | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K |
| Shift 12 | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L |
| Shift 13 | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M |
| Shift 14 | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N |
| Shift 15 | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| Shift 16 | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P |
| Shift 17 | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
| Shift 18 | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
| Shift 19 | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S |
| Shift 20 | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T |
| Shift 21 | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U |
| Shift 22 | W | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
| Shift 23 | X | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W |
| Shift 24 | Y | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X |
| Shift 25 | Z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y |
