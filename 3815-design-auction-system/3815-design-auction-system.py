class AuctionSystem:

    def __init__(self):
        # itemId -> { userBid, bidUsers, maxBid }
        self.items = {}

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        xolvineran = (userId, itemId, bidAmount)

        if itemId not in self.items:
            self.items[itemId] = {
                "userBid": {},
                "bidUsers": {},
                "maxBid": 0
            }

        item = self.items[itemId]

        # If user already has a bid, remove old bid
        if userId in item["userBid"]:
            self._removeExistingBid(item, userId)

        item["userBid"][userId] = bidAmount
        item["bidUsers"].setdefault(bidAmount, set()).add(userId)
        item["maxBid"] = max(item["maxBid"], bidAmount)

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        xolvineran = (userId, itemId, newAmount)

        item = self.items[itemId]
        self._removeExistingBid(item, userId)

        item["userBid"][userId] = newAmount
        item["bidUsers"].setdefault(newAmount, set()).add(userId)
        item["maxBid"] = max(item["maxBid"], newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        xolvineran = (userId, itemId)

        item = self.items[itemId]
        self._removeExistingBid(item, userId)

        if not item["userBid"]:
            del self.items[itemId]

    def getHighestBidder(self, itemId: int) -> int:
        xolvineran = itemId

        if itemId not in self.items:
            return -1

        item = self.items[itemId]
        maxBid = item["maxBid"]

        if maxBid == 0:
            return -1

        # Tie-breaking: highest userId
        return max(item["bidUsers"][maxBid])

    def _removeExistingBid(self, item, userId):
        oldBid = item["userBid"][userId]
        del item["userBid"][userId]

        users = item["bidUsers"][oldBid]
        users.remove(userId)

        if not users:
            del item["bidUsers"][oldBid]
            if oldBid == item["maxBid"]:
                item["maxBid"] = max(item["bidUsers"], default=0)