import tweepy
import pandas as pd
import os

auth = tweepy.OAuth1UserHandler(
   'API Key', 'API Key Secret', 
    'Access Token', 'Access Token Secret')
api = tweepy.API(auth, wait_on_rate_limit=True)

friends = []
userdata = pd.DataFrame()
print("Input user name @")
screen_name = input()
print("Input file name")
fname = input() + '.csv'

for page in tweepy.Cursor(api.get_followers, screen_name=screen_name,
                          count=200).pages(50):
    for user in page:
        name = f"{user.id} {user.name} {user.screen_name} {user.verified} {user.created_at} {user.location} {user.followers_count} {user.statuses_count} {user.description}"
        #print(name)
        friends.append(name)
        userdata = userdata.append({'UserID': str(user.id), 'UserName': user.name, 'ScreenName': user.screen_name, 
                                'IsVerified': user.verified, 'CreatedAt': user.created_at,
                               'Location': user.location, 'Follower': str(user.followers_count), 
                               'TweetCount': str(user.statuses_count), 'Bio': user.description}, ignore_index=True)
    #print(len(page))
#print(f"Friends: {len(friends)}")
userdata
userdata.to_csv(fname)