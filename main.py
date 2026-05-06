from fetch import fetch_hackernews
from fetch_reddit import fetch_reddit
from summarize import summarize_stories
from send_email import send_briefing

def run_pulseai():
    print("=" * 40)
    print("       PULSEAI - Your Daily AI Briefing")
    print("=" * 40)
    
    # fetch from both sources
    hn_stories = fetch_hackernews()
    reddit_stories = fetch_reddit()
    
    # combine and deduplicate
    all_stories = hn_stories + reddit_stories
    
    seen_titles = set()
    unique_stories = []
    for story in all_stories:
        if story["title"] not in seen_titles:
            seen_titles.add(story["title"])
            unique_stories.append(story)
    
    print(f"\nTotal unique stories found: {len(unique_stories)}")
    
    if not unique_stories:
        print("No stories found today. Try again later.")
        return
    
    # summarize
    briefing = summarize_stories(unique_stories)
    
    print("\n📰 TODAY'S BRIEFING\n")
    print(briefing)
    print("\n" + "=" * 40)
    
    # send to email
    send_briefing(briefing)

if __name__ == "__main__":
    run_pulseai()