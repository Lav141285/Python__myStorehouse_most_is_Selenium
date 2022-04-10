from instapy import InstaPy 

#headless_browser = True if you want to hide your browser
session = InstaPy(username = "gunther.super", password = "gunther1234", headless_browser = True)
session.login()

#You can set max and min followers here
session.set_relationship_bounds(enabled = True, max_followers = 200)

#Percentage from 0 to 100. 100 if you want to follow everyone who get your likes
session.set_do_follow(True, percentage=100)

#You will like posts with "bmw" and "steam" tags. If you set "amount = 3" 
#then you'll give 12 likes to "bmw" tag and 12 likes to "steam" tag
session.like_by_tags(["bmw", "steam"], amount = 3)
session.set_dont_like(["nsfw"])

#session.unfollow_users(amount=6, allFollowing=True, sleep_delay=60)

session.end()