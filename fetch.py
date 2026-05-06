import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_hackernews():
    print("Fetching top AI stories from HackerNews...")
    
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    story_ids = response.json()[:30]
    
    stories = []
    
    for story_id in story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()
        
        title = story.get("title", "")
        url = story.get("url", "")
        score = story.get("score", 0)
        
        ai_keywords = ["AI", "LLM", "GPT", "machine learning", "neural", "model", 
                       "agent", "Claude", "Gemini", "OpenAI", "Anthropic", "robot"]
        
        if any(keyword.lower() in title.lower() for keyword in ai_keywords):
            stories.append({
                "title": title,
                "url": url,
                "score": score
            })
    
    print(f"Found {len(stories)} AI-related stories")
    return stories