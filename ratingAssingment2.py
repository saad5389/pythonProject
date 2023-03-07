class Rating:
    def __init__(self, rating):
        if self.validateRating(rating):
            self.starRating = rating
        else:
            print('Invalid rating')

    def validateRating(self, rating):
        return 0 <= rating <= 5

    def getRating(self):
        rate = ["empty", "empty", "empty", "empty", "empty"]
        i = 0
        while i < round(self.starRating):
            rate[i] = "full"
            i += 1
        return rate
