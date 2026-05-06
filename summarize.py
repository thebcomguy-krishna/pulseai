import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def summarize_stories(stories):
    print("Summarizing stories with AI...")
    
    stories_text = ""
    for i, story in enumerate(stories, 1):
        stories_text += f"{i}. {story['title']}\n   {story['url']}\n\n"
    
    prompt = f"""You are a tech news analyst for a 19-year-old who wants to stay updated on AI.

Here are today's top AI stories:

{stories_text}

Give me a briefing with the 5 most important stories. For each one:
- Write the title
- One sentence on what it is
- One sentence on why it matters for someone interested in AI agents, automation, and building things

Keep it sharp, no fluff. Format it like this:

1. [Title]
   What: ...
   Why it matters: ...
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content