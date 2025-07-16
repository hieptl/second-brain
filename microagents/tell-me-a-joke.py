#!/usr/bin/env python3
"""
OpenHands Microagent: Tell Me a Joke

This microagent tells a random joke when triggered.

Triggers: tell-me-a-joke
"""

import random
import json
import sys

# Collection of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "What do you call a fake noodle? An impasta!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why was the math book sad? Because it had too many problems.",
    "What do you call a parade of rabbits hopping backwards? A receding hare-line.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "How do you organize a space party? You planet!",
    "What's orange and sounds like a parrot? A carrot.",
    "Why can't you give Elsa a balloon? Because she will let it go.",
    "I used to be a baker, but I couldn't make enough dough.",
    "What's brown and sticky? A stick.",
    "Why did the chicken go to the séance? To get to the other side.",
    "What do you call a fish with no eyes? Fsh.",
    "How do you make a tissue dance? Put a little boogie in it!",
    "What did one ocean say to the other ocean? Nothing, they just waved."
]

def main():
    # Select a random joke
    joke = random.choice(jokes)
    
    # Return the joke in the expected format
    response = {
        "response": joke
    }
    
    # Print the response as JSON
    print(json.dumps(response))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())