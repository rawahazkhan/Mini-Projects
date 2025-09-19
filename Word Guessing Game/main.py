import random
word_bank =[
    "mystify", "oxygen", "awkward", "rhythm", "sapphire", "cryptic", "jigsaw", "phobia", "quartz", "voyage",
    "python", "galaxy", "whisper", "puzzle", "cipher", "jungle", "hazard", "sphinx", "unique", "voyager",
    "plasma", "nebula", "matrix", "gadget", "wizard", "random", "glitch", "fusion", "rocket", "shadow",
    "ember", "velvet", "cosmic", "energy", "hollow", "mirror", "spirit", "signal", "secret", "throne",
    "legacy", "orbit", "vortex", "phantom", "savage", "hunter", "silent", "stormy", "twilight", "zodiac"]

word = random.choice(word_bank)
guess_word = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print("\nCurrent word: " + " ".join(guess_word))
    guess = input("Guess the letter: ").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess_word[i] = guess
                print("Wow! You guessed right!")
    else:
        attempts -= 1
        print("Oop! Wrong Guess, Attempts left: " + str(attempts))

    if "_" not in guess_word:
        print("\nHurray! You guess the word: " + word)
        break

if attempts == 0 and "_" in guess_word:
    print("\nOop! You\'ve run out of attempts. The word was: " + word)
     



