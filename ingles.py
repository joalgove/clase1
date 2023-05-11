import urllib.request
import random

def get_word(n):
    if n > 0 and n < 7:
        url = f"https://www.mit.edu/~ecprice/wordlist.10000"
        response = urllib.request.urlopen(url)
        long_words = [word.decode().strip() for word in response if len(word.decode().strip()) == n]
        return random.choice(long_words)
    else:
        return "El número no está entre 0 y 10"

numero = int(input("Introduce un número:!!! "))
palabra = get_word(numero)
print(palabra)
