# Twitter Sentiment Analysis
# Program that proccess tweets and determines the region of tweet as well as corresponding Happiness Value

keyWordsDict = dict()                        # Empty dictionary to stored key words in

keyInput = int(input("Would you like to manually add key words (Type 1) or use a text file containing the words(Type 2):"))
if keyInput == 2:
    keyWordsName = str(input("Enter the name of the file containing the keywords:"))

    keyWordsfile = open(keyWordsName, "r")     # Opens and reads Keywords Text
    line = keyWordsfile.readline()
    while line != "":                            # While loop to add the key word and its value to the empty dictionary
        line = line.replace(","," ")
        line = line.strip()
        line = line.split(" ")                   # Splits the line
        keyWordsDict.update({line[0]: line[1]})  # Adds the key word and its value to keyWordsDict
        line = keyWordsfile.readline()
    keyWordsfile.close()
elif keyInput == 1:
    entry = "Y"
    while entry == "Y":
        keyWord = str(input("Enter a key word to add:"))
        keyValue = int(input("Enter its value:"))
        keyWordsDict.update({keyWord: keyValue})
        entry = str(input("Would you like to add another key word? (Y/N) ")).upper()






def coordinates(text):                 # Function that determines what region the tweet belongs to
    text = text.split("]")
    coordinates = text[0]
    coordinates = coordinates.strip("[")
    coordinates = coordinates.replace(",","")
    coordinates = coordinates.split()
    latCord = float(coordinates[0])
    longCord = float(coordinates[1])
    if 24.660845 <= latCord <= 49.189787 and -87.518395 <= longCord <= -67.444574:  # Checks for Eastern Region
        region = "Eastern"
    elif 24.660845 <= latCord <= 49.189787 and -101.998892 <= longCord <= -87.518395:  # Check for Central Region
        region = "Central"
    elif 24.660845 <= latCord <= 49.189787 and -115.236428 <= longCord <= -101.998892:  # Check for Mountain Region
        region = "Mountain"
    elif 24.660845 <= latCord <= 49.189787 and -125.242264 <= longCord <= -115.236428:  # Check for Pacific Region
        region = "Pacific"
    else:
        region = "outofrange"

    return region


def tweetSentiment(text):             # Function that determines the Sentiment value of the tweet
    sentiment = 0
    text = text.split()              # Splits the line into a list
    del text[0:5]                    # Deletes all elements  until where the tweet starts
    tweet = ""                       # Empty string to add the elements of the list to make the tweet
    for i in text:
        tweet = tweet + " " + i
        tweet = tweet.rstrip(",./?!@#$%^&*():; ")  # Strips tweet from right side for certain characters
        tweet = tweet.lstrip(",./?!@#$%^&*():; ")  # Strips tweet from left side for certain characters
    tweet = tweet.lower()                     # Makes all words in the tweet lower case
    tweetlist = tweet.split()                 # Splits the tweet into a list
    for i in tweetlist:
        if i in keyWordsDict:            # Checks to see if words from the tweet are in the dictionary for keywords
            sentiment = sentiment + int(keyWordsDict[i])

    return sentiment


easternCount = 0   # Total number of tweets in eastern region
easternScore = 0   # Total sentiment value in eastern region
centralCount = 0   # Total number of tweets in central region
centralScore = 0   # Total sentiment value in central region
mountainCount = 0   # Total number of tweets in mountain region
mountainScore = 0   # Total sentiment value in mountain region
pacificCount = 0   # Total number of tweets in pacific region
pacificScore = 0   # Total sentiment value in pacific region

tweetsName = str(input("Enter the name of the file containing the tweets:"))
inputfile = open(tweetsName, "r")   # Opens and reads tweets Text
line = inputfile.readline()
while line != "":             # While loop to check if each tweet has sentiment value and what region it belongs to
    area = (coordinates(line))     # Calling coordinates function to determine region of tweet
    score = (tweetSentiment(line))  # calling tweetSentiment function to determine sentiment of tweet
    if area == "Eastern" and score != 0:
        easternCount = easternCount + 1
        easternScore = easternScore + score
    elif area == "Central" and score != 0:
        centralCount = centralCount + 1
        centralScore = centralScore + score
    elif area == "Mountain" and score != 0:
        mountainCount = mountainCount + 1
        mountainScore = mountainScore + score
    elif area == "Pacific" and score != 0:
        pacificCount = pacificCount + 1
        pacificScore = pacificScore + score
    line = inputfile.readline()
inputfile.close()

if easternCount != 0:
    eastHapValu = easternScore/easternCount  # Calculated Eastern Region Happiness Value
else:
    eastHapValu = 0
if centralCount!= 0:
    centHapValu = centralScore/centralCount  # Calculates Central Region Happiness Value
else:
    centHapValu = 0
if mountainCount != 0:
    mounHapValu = mountainScore/mountainCount  # Calculates Mountain Region Happiness Value
else:
    mounHapValu = 0
if pacificCount!= 0:
    pacificHapValue = pacificScore/pacificCount
else:
    pacificHapValue = 0

print('The Happiness Score for The Eastern Region is', round(eastHapValu, 2), 'With a Total of', easternCount, 'Tweets')
print('The Happiness Score for The Central Region is', round(centHapValu, 2), 'With a Total of', centralCount, 'Tweets')
print('The Happiness Score for The Mountain Region is', round(mounHapValu, 2), 'With a Total of', mountainCount, 'Tweets')
print('The Happiness Score for The Pacific Region is', round(pacificHapValue, 2), 'With a Total of', pacificCount, 'Tweets')
