# Write your solution here
def anagrams(word1, word2):
    
    if sorted(list(word1)) == sorted(list(word2)):
        return True
    else:
        return False


if __name__ == "__main__":
    print(anagrams("tame", "meta"))