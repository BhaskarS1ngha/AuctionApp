from django.db import models
from django.utils import timezone

class Auction(models.Model):
    auctionId = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=100)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(blank=False)
    startPrice = models.FloatField(blank=False)
    highestBid = models.FloatField(blank=True,null=True)
    highestBidder = models.UUIDField(blank=True,null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.itemName

    def check_status(self):
        currentTime = timezone.now()
        time_diff = self.endTime-currentTime
        if time_diff.total_seconds() <=0:
            self.isActive = False
        self.save()

    def getBidderName(self):
        if self.highestBidder is not None:
            users = user.objects.all()
            hb = users.get(pk=self.highestBidder)
            return hb




class user(models.Model):
    userID = models.UUIDField(primary_key=True)
    userName = models.CharField(max_length=100,null=False)


    def __str__(self):
        return self.userName


class bid(models.Model):
    bidID = models.AutoField(primary_key=True)
    auctionID = models.IntegerField(null=False)
    bidAmount = models.FloatField(null=False)
