def word_frequency(sentence):
    # Split the sentence into words by whitespace and remove punctuation
    words = sentence.split()
    
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}
    
    for word in words:
        # Remove punctuation and convert to lowercase for consistent counting
        cleaned_word = word.strip('.,!?()[]{}"\'').lower()
        
        # Check if the word is already in the dictionary, and if not, add it with a frequency of 1
        if cleaned_word not in word_freq:
            word_freq[cleaned_word] = 1
        else:
            # If the word is already in the dictionary, increment its frequency
            word_freq[cleaned_word] += 1
    
    return word_freq

# Test case
sentence = "This is a test. This test is a simple test."
result = word_frequency(sentence)
print(result)