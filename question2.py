# CSI428 Assignment 1 Question 2 Solution
# Trudy-Lynn O. K. Dube 202102225
# Naomi S. Tumaeletse 202005404
# Keletso Joy Ditlhotlhole 202002023
# DUE: 24/02/2025

import re

#function to read contents of file
def read_file(filename):
    """Load words"""
    with open(filename, 'r', encoding='utf-8') as f:
        return set(f.read().strip().split('\n'))

#function to read contents of file and create dictionary
def read_file_to_dict(filename):
    """Load words into a dictionary"""
    word_dict = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            label, word = line.strip().split()
            word_dict[word] = label
    return word_dict

cc = read_file_to_dict('cc.txt')  # Conjunctions
l = read_file_to_dict('l.txt')   # verb
pro = read_file('pronouns.txt')  # Pronouns
vng = read_file('verbs.txt')  # Verbs
vnge = read_file('verbstense.txt')  # Vnge vng
nouns = read_file('nouns.txt')  # Nouns

# Merge cc and l dictionary
word_to_label = {**cc, **l}
word_to_label.update({'o': 'CC2'})

# Reversal of dictionary for outputting Leamanyi struture as words
label_to_word = {v: k for k, v in word_to_label.items()}

def convert_sentence_to_labels(sentence):
    """Convert an actual Setswana sentence to its corresponding CC labels."""
    words = sentence.split()
    converted = [word_to_label.get(word, word) for word in words]
    return " ".join(converted)

# Leamanyi structures
leamanyi_structures = [

    rf"(CC1)\s+(CC2)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})",  # CC1 CC2 [L02 CC12|L02] Vng
    rf"(CC3)\s+(CC3)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})",  # CC3 CC3 [L02 CC12|L02] Vng
    rf"(CC4)\s+(CC4)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})",  # CC4 CC4 [L02 CC12|L02] Vng
    rf"(CC5)\s+(CC5)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})",  # CC5 CC5 [L02 CC12|L02] Vng
    rf"(CC6)\s+(CC6)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})",  # CC6 CC6 [L02 CC12|L02] Vng
    rf"(CC7)\s+(CC7)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})",  # CC7 CC7 [L02 CC12|L02] Vng
    rf"(CC8)\s+(CC9)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})",  # CC8 CC9 [L02 CC12|L02] Vng
    rf"(CC10)\s+(CC11)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})", # CC10 CC11 [L02 CC12|L02] Vng
    rf"(CC11)\s+(CC12)\s+(L02\s+CC12|L02)?\s+({'|'.join(vng)})", # CC11 CC12 [L02 CC12|L02] Vng
    
    rf"(CC1)\s+(CC2)\s+(L01)\s+({'|'.join(vnge)})",  # CC1 CC2 L01 Vnge
    rf"(CC3)\s+(CC3)\s+(L01)\s+({'|'.join(vnge)})",  # CC3 CC3 L01 Vnge
    rf"(CC4)\s+(CC4)\s+(L01)\s+({'|'.join(vnge)})",  # CC4 CC4 L01 Vnge
    rf"(CC5)\s+(CC5)\s+(L01)\s+({'|'.join(vnge)})",  # CC5 CC5 L01 Vnge
    rf"(CC6)\s+(CC6)\s+(L01)\s+({'|'.join(vnge)})",  # CC6 CC6 L01 Vnge
    rf"(CC7)\s+(CC7)\s+(L01)\s+({'|'.join(vnge)})",  # CC7 CC7 L01 Vnge
    rf"(CC8)\s+(CC9)\s+(L01)\s+({'|'.join(vnge)})",  # CC8 CC9 L01 Vnge
    rf"(CC10)\s+(CC11)\s+(L01)\s+({'|'.join(vnge)})", # CC10 CC11 L01 Vnge
    rf"(CC11)\s+(CC12)\s+(L01)\s+({'|'.join(vnge)})", # CC11 CC12 L01 Vnge
    
    rf"(CC1)\s+(CC2)\s+(L03)\s+(CC5)\s+({'|'.join(nouns)}|{'|'.join(pro)})",  # CC1 CC2 L03 CC5 Noun|PRO
    rf"(CC3)\s+(CC3)\s+(L03)\s+(CC5)\s+({'|'.join(nouns)}|{'|'.join(pro)})",  # CC3 CC3 L03 CC5 Noun|PRO
    rf"(CC4)\s+(CC4)\s+(L03)\s+(CC5)\s+({'|'.join(nouns)}|{'|'.join(pro)})",  # CC4 CC4 L03 CC5 Noun|PRO
    rf"(CC5)\s+(CC5)\s+(L03)\s+(CC5)\s+({'|'.join(nouns)}|{'|'.join(pro)})",  # CC5 CC5 L03 CC5 Noun|PRO
]

def convert_labels_to_words(converted_sentence):
    words = converted_sentence.split()
    return " ".join([label_to_word.get(word, word) for word in words])

def identify_leamanyi(sentence):
    """Check if a sentence contains a Leamanyi structure."""
    converted_sentence = convert_sentence_to_labels(sentence)
    for pattern in leamanyi_structures:
        match = re.search(pattern, converted_sentence)
        if match:
            matched_sentence = match.group(0)
            return f"Leamanyi found! Structure: {convert_labels_to_words(matched_sentence)}" 
    return "Leamanyi not found!"

# Example usage
if __name__ == "__main__":
    test_sentence = "yo o sa tsamaeng thata eish eish"
    test_sentence = test_sentence.lower()
    result = identify_leamanyi(test_sentence)
    print(result)
