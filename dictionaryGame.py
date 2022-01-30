import random, time, sys


engWordsDict = {"Deranged" : "Dengesiz", "Cat" : "Kedi"}
sortedDict = dict( sorted(engWordsDict.items(), key=lambda x: x[0].lower()))
engWords = list(sortedDict.keys())
turkWords = list(sortedDict.values())
print("Translate english words to turkish!")
def main():

    while True:
        time.sleep(0.2)

        if len(engWords) == 0:
            print("Congrats!!! You answered all questions!")
        else:
            randomIndex = random.randint(0,len(engWords)-1)

            while True:
                time.sleep(0.2)
                answer = input(engWords[randomIndex] + ": ")
                if answer.lower() == turkWords[randomIndex].lower():
                    print("Correct answer")
                    engWords.pop(randomIndex)
                    turkWords.pop(randomIndex)
                    main()
                else:
                    print("False! Try Again")
                    continue


main()
