class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetList = defaultdict(list)
        self.followList = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetList[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followList[userId].add(userId)
        for followeeId in self.followList[userId]:
            if self.tweetList[followeeId]:
                index = len(self.tweetList[followeeId]) - 1
                count, tweetId = self.tweetList[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index - 1])
        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetList[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index - 1])
                index -= 1
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)
