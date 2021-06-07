from re import sub
from threading import active_count
import praw
from datetime import datetime
import os
from tqdm import tqdm
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
reddit = praw.Reddit('bot1')

printAll = False
postsToCheck = 50
delay = 900
subreddit = reddit.subreddit("smg4")
print("[Hornyjail Bot] Authenticated to Reddit and waiting for commands.")
while True:
    print(f"""----------------------------------------
    Checking 50 posts from r/{subreddit.display_name}...
    Grabbing newest submissions...
    Downloading and checking submissions...""")
    PostCount = 0
    NSFWPosts = []
    ToCheck = []
    Actions = ""
    #for submission in tqdm(subreddit.new(limit=postsToCheck),total=postsToCheck): This only works if you are not using a host that has a shitty console
    for submission in subreddit.new(limit=postsToCheck):
        PostCount = PostCount + 1
        print(f"Checking post {PostCount} out of {postsToCheck}.\n{round(100/postsToCheck*PostCount)}% completed.")
        if printAll:
            print(f"""---Debug printout---
            Title: {submission.title}
            Author: {submission.author.name}
            Score: {submission.score}
            URL: {submission.url}
            Created at: {datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')}
            ---------------------""")
        if submission.over_18:
            print(f"""---NSFW post found---
            Title: {submission.title}
            Author: {submission.author.name}
            Score: {submission.score}
            URL: {submission.url}
            Created at: {datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')}
            ---------------------""")
            try:
                submission.mod.remove()
            except:
                Actions = "Post removal(Failed)"
                print("Submission deletion failed")
            else:
                Actions = "Post removal"
                print("Deleted submission")
            time.sleep(0.5)
            try:
                message = "One of your posts on r/SMG4 has been removed because it contains innapropriate content. Please keep it appropriate.\n\nThis action was performed automatically."
                submission.mod.send_removal_message(message, title='ignored', type='private')
            except:
                Actions = Actions + "\nSet removal reason(Failed)"
                print("Set removal reason failed")
            else:
                Actions = Actions + "\nSet removal reason"
                print("Set removal reason")
            embed = DiscordEmbed(title='NSFW post', description='', color='03b2f8')
            timeStr = datetime.utcfromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')
            embed.add_embed_field(name='Post info', value=f'Title: {submission.title}\nAuthor: {submission.author.name}\nScore: {submission.score}\nURL: {submission.url}\nCreated at: {timeStr}')
            embed.add_embed_field(name='Action(s) taken', value=Actions)
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/850750748953149470/X_Fl-PwMD9vnGgsZTYVtqPS84_pfl1m9ntxRiDYXPJCvPxyyN4X0D5AwdtfT5PDVF4Fk')
            webhook.add_embed(embed)
            response = webhook.execute()
    print("----Results----")
    if not NSFWPosts:
        print("No NSFW posts found!")
    else:
        print("NSFW posts found: ",len(NSFWPosts))
    print("Checked posts: ", PostCount)
    print("----------------------------------------\n")
    time.sleep(delay)