from twitterscraper import query_tweets
import datetime as dt

if __name__ == '__main__':
    list_of_tweets = query_tweets("리버풀", 10)

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("리버풀", 10,
                              begindate=dt.date(2018,3,1),
                              enddate=dt.date(2018,4,5)):
        print(tweet.timestamp) # 작성시각
        print(tweet.text) # 트윗내용

    #Or save the retrieved tweets to file:
    file = open("output.txt", "wb")
    for tweet in query_tweets("리버풀", 10):
        file.write(str(tweet.timestamp).encode())
        file.write(tweet.text.encode('utf-8'))
    file.close()