import requests

def fetch_reddit():
    print("Fetching stories from Reddit...")
    
    subreddits = ["MachineLearning", "artificial", "LocalLLaMA", "singularity"]
    stories = []
    
    headers = {"User-Agent": "PulseAI/1.0"}
    
    for subreddit in subreddits:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            posts = data["data"]["children"]
            
            for post in posts:
                post_data = post["data"]
                title = post_data.get("title", "")
                link = post_data.get("url", "")
                score = post_data.get("score", 0)
                
                # filter out low quality posts
                if score > 50:
                    stories.append({
                        "title": title,
                        "url": link,
                        "score": score,
                        "source": f"r/{subreddit}"
                    })
        
        except Exception as e:
            print(f"Error fetching r/{subreddit}: {e}")
    
    # sort by score
    stories = sorted(stories, key=lambda x: x["score"], reverse=True)[:10]
    
    print(f"Found {len(stories)} stories from Reddit")
    return stories

if __name__ == "__main__":
    stories = fetch_reddit()
    for s in stories:
        print(f"\n- [{s['source']}] {s['title']} (score: {s['score']})")

