from vaderSentiment import SentimentIntensityAnalyzer

#sentences = ["now i am not feeling good"]
senten = input("Enter the text = ");
sentences = senten.split()

#sentences = [str(a) for a in sentences] 

#sentences = eval(sentences)
#print(sentences)
#senten = raw_input("Hii ")
#sentences = list(map(str, senten.split()))

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
