from website.models import UserDetails, Auction, Bid
from django.utils import timezone
from datetime import datetime, timedelta

def increase_bid(user, auction, price):
    """
    Creates a Bid record
    Increases the auction's number of bids

    Parameters
    ----------
    auction : class 'website.models.Auction
    """
    
    bid = Bid()
    bid.user_id = user
    bid.auction_id = auction
    bid.bid_time = timezone.now()
    bid.bid_price = price
    bid.save()
    auction.number_of_bids += 1
    auction.base_price = price
    # auction.time_ending = timezone.now() + timedelta(minutes=5)
    auction.save()

def cut_balance(user, auction, price):
    """
    Removes money from user.
    """

    userDetails = UserDetails.objects.get(user_id=user.id)
    userDetails.balance = userDetails.balance - price
    userDetails.save()

def remaining_time(auction):
    """
    Calculates the auction's remaining time
    in minutes and seconds and converts them 
    into a string.
    
    Parameters
    ----------
    auction : class 'website.models.Auction
    
    Returns
    -------
    
    time_left : str
        string representation of remaining time in
        minutes and seconds.
    expired : int
        if the value is less than zero then the auction ended.
    
    """
    time_left = auction.time_ending - timezone.now()
    days, seconds = time_left.days, time_left.seconds
    # hours = days * 24 + seconds // 3600
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    time_left = str(days) + "d " + str(hours) + "h " + str(minutes) + "m"
    expired = days + hours + minutes
    
    return time_left, expired