# Encryption:

You’ve taken a plain text message (let’s call it “hello, world”) and transformed it into a secret code using a shuffled key.

The key is essentially a scrambled version of the character set (including punctuation, digits, and letters).

For each letter in your original message, you find its index in the original character set and use the corresponding letter from the shuffled key.

So, “hello, world” might become something like “qjssv, zjzsk.”

# Decryption:

Now, you want to reverse the process. You have the encrypted message (“qjssv, zjzsk”) and the shuffled key.

For each letter in the encrypted message, you find its index in the shuffled key and use the corresponding letter from the original character set.

Voilà! You get back your original message: “hello, world.”

# Random Shuffling:
The magic lies in the random shuffling of the key. It ensures that the relationship between characters in the original message and the encrypted message is unpredictable.

Without the correct key, decrypting the message becomes quite challenging.