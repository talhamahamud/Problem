def matchWord(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    sentences = ["Talha is a bad boy", "Python is not a snake",
                 "I love you", "This is me", "Python is a good language", "Proggramar can do anything"]
    input1 = input("pls enter your word: ")
    sentenceScore = [matchWord(input1, senten) for senten in sentences]
    sortedSenten = [sentscore for sentscore in sorted(
        zip(sentenceScore, sentences), reverse=True) if sentscore[0] != 0]
    print(len(sortedSenten))
    for num, sentence in sortedSenten:
        print(f"\"{sentence}\" is the output and score is {num}")
