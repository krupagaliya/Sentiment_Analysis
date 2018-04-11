# from vaderSentiment import SentimentIntensityAnalyzer

# sentences = input("Enter sentence = ")
# #print(sentences)

# # senten = input("Hii ")
# # sentences = list(map(str, senten.split()))


# analyzer = SentimentIntensityAnalyzer()


# vs = analyzer.polarity_scores(sentences)
# print("{:-<100} {}".format(sentences, str(vs)))


from vaderSentiment import SentimentIntensityAnalyzer
import textblob as tb

sentences = input("Enter sentence = ")

#print(sentences)

# senten = input("Hii ")
# sentences = list(map(str, senten.split()))


analyzer = SentimentIntensityAnalyzer()


vs = analyzer.polarity_scores(sentences)
print("{:-<50} {}".format(sentences, str(vs)))


