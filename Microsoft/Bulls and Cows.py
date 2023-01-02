class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        secret = list(secret)
        guess = list(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                secret[i] = " "
            elif guess[i] in secret and guess[i] != secret[i]:
                secret[secret.index(guess[i])] = " "
                cow += 1
            else:
                continue
        return str(bull)+"A"+str(cow)+"B"
