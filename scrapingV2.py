import praw
import warnings
from datetime import datetime


# Config
reddit = praw.Reddit(
    client_id='CLIENTID',
    client_secret='CLIENTSECRET',
    user_agent='Scraper:v1.0 (by u/penguinshaveknees20)'
)

# warnings disabled 
warnings.filterwarnings("ignore", category=UserWarning, module="praw")


# URL LIST
post_urls = [
   "https://old.reddit.com/r/autism/comments/qxqjhr/what_does_sensory_overload_feel_like/?sort=top",
"https://old.reddit.com/r/autism/comments/wtxihq/how_to_describe_sensory_or_auditory_overload_to/",
"https://old.reddit.com/r/AuDHDWomen/comments/1d299c2/what_are_steps_you_take_to_help_yourself_when/",
"https://old.reddit.com/r/ADHD/comments/14lp4rk/do_people_with_adhd_suffer_from_sensory_overload/",
"https://old.reddit.com/r/neurodiversity/comments/1epz0ac/how_do_you_handle_sensory_overload_looking_for/",
"https://old.reddit.com/r/AutisticAdults/comments/17tkhgr/the_science_behind_sensory_overload/",
"https://old.reddit.com/r/autism/comments/163jiv8/what_does_sensory_overload_feel_like_to_you/",
"https://old.reddit.com/r/ADHD/comments/18gvvpx/what_does_sensory_overload_feel_like/",
"https://www.reddit.com/r/AutismInWomen/comments/1efae2p/how_do_you_handle_sensory_overload_in_public/",
"https://old.reddit.com/r/neurodiversity/comments/1c5cdy8/tips_on_dealing_with_sensory_overload/",
"https://old.reddit.com/r/autism/comments/18ssymx/can_nonautistic_people_experience_sensory_overload/",
"https://old.reddit.com/r/autism/comments/ppou65/my_tips_on_how_to_avoid_a_sensory_overload/"

]


def format_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def print_comments(comment_list, level=0):
    for comment in comment_list:
        if isinstance(comment, praw.models.Comment):
 
            print("    " * level + f"User: {comment.author}")
            print("    " * level + f"- {comment.body}")
            print("    " * level + f"Date: {format_date(comment.created_utc)}")
            print("")

            if len(comment.replies) > 0:
                print_comments(comment.replies, level + 1)


for post_url in post_urls:
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)

    print(f"# POST TITLE: {submission.title}")
    print("")
    print(f"# SUBREDDIT: {submission.subreddit}")
    print("")
    print(f"Date: {format_date(submission.created_utc)}")
    print("")
    print("# COMMENTS:")
    print("")
    print_comments(submission.comments)
    print("=" * 80)
