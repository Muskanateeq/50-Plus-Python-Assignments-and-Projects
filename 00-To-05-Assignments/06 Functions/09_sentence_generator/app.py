def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # Template for a noun.
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        # Template for a verb.
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        # Template for an adjective.
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech selection.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()
