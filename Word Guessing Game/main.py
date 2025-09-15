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



