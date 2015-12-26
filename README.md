# twitter-marketing-bot
Python scripts to market news to twitter followers.
Note: A delay of 1 min after every tweet has been added to prevent Twitter from blocking the app immediately.

## Prerequisites
* [Install tweepy](https://github.com/tweepy/tweepy#installation)
* Create an app at [apps.twitter.com](apps.twitter.com) with read, write permissions

## Usage
1. Modify the [get_oauth_token.py](https://github.com/antrromet/twitter-marketing-bot/blob/master/get_oauth_token.py) to add your consumer key and secret from the app you created in prerequisites.
2. Run the get_oauth_token.py script and follow the instructions on the terminal.
3. Modify the [get_followers.py](https://github.com/antrromet/twitter-marketing-bot/blob/master/get_followers.py) to add your access token and secret. It is printed on the terminal after completing the previous step.
4. Run the get_followers.py to let the bot do its work.

## Troubleshooting
* Twitter might block the app for several reasons, and those reasons will be printed on the terminal.
* The best way to avoid twitter write timeouts, would be separate the tasks in 2 different scripts. One script can handle just fetching the followers part, and other script can handle the tweeting part. Also the code can be modified such that the name from the file is deleted after the tweet has been posted to that person.
* If you find any other doubts or problems feel free to create issues.
