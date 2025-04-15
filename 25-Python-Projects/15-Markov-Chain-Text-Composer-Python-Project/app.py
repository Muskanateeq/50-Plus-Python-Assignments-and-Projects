import random
import re
import nltk
from collections import defaultdict

# Download NLTK tokenizer
nltk.download('punkt')
nltk.download('punkt_tab')
# Uncomment below if you get an error about 'punkt_tab'
# nltk.download("punkt_tab")

class MarkovChainTextComposer:
    def __init__(self):
        self.model = defaultdict(list)

    def train(self, text, order=2):
        """ Train the Markov chain model with the given text. """
        words = nltk.word_tokenize(text)
        for i in range(len(words) - order):
            key = tuple(words[i : i + order])
            next_word = words[i + order]
            self.model[key].append(next_word)

    def generate(self, length=50, seed=None):
        """ Generate text based on the trained Markov model. """
        if not self.model:
            raise ValueError("The model is empty. Train it with some text first!")
        start = random.choice(list(self.model.keys())) if not seed else tuple(seed.split()[:2])
        output = list(start)
        for _ in range(length):
            last_words = tuple(output[-2:])
            next_word = random.choice(self.model.get(last_words, ["."]))  # Fallback to '.'
            output.append(next_word)
        return " ".join(output)

# Example usage
if __name__ == "__main__":
    text = """Markov Chains are a mathematical system that undergoes transitions from one state to another 
    according to certain probabilistic rules. They are used in text generation, speech recognition, 
    and even AI-based music composition."""
    
    composer = MarkovChainTextComposer()
    composer.train(text, order=2)
    
    generated_text = composer.generate(length=30)
    print("Generated Text:\n", generated_text)
