class Twitter:

    def __init__(self):
        self.followers = {} #List of followers as values to followed id as key
        self.tweets = {} #User id as key and there tweet id's and posted sequence as values
        self.seq = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId,[]).append([tweetId,self.seq])
        self.seq += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId]
        for f in self.followers.get(userId, []):
            users.append(f)
        
        all_tweets = []
        
        for uid in users:
            if uid in self.tweets:
                all_tweets.extend(self.tweets[uid])
                
        all_tweets.sort(key=lambda x: x[1], reverse=True)
        
        return [t[0] for t in all_tweets][:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers.get(followerId, []):
            self.followers.setdefault(followerId, []).append(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

