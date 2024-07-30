def count_words(text):
    """
    Counts the number of words in the given text.
    """
    words = text.split()
    return len(words)

def count_character_frequency(text):
    """
    Counts the frequency of each character in the given text.
    Converts all characters to lowercase to avoid duplicates.
    """
    text = text.lower()  # Convert all characters to lowercase
    frequency = {}
    
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

def main():
    # Open the file and read its contents
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
    
    # Print the contents to the console
    print(file_contents)
    
    # Count the number of words and print it
    word_count = count_words(file_contents)
    print(f"\nThe Frankenstein book contains {word_count} words.")
    
    # Count the frequency of each character and print it
    char_frequency = count_character_frequency(file_contents)
    print("\nCharacter frequencies:")
    for char, freq in char_frequency.items():
        print(f"'{char}': {freq}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()