# PulseAI 🤖

A personal AI agent that monitors the internet for AI news and delivers a sharp daily briefing to your inbox every morning.

Built for people who want to stay on top of AI without drowning in noise.

## What it does

- Scrapes top AI stories from HackerNews and Reddit (r/MachineLearning, r/LocalLLaMA, r/artificial, r/singularity)
- Uses LLaMA 3.3 via Groq to filter and summarize the most important stories
- Delivers a clean 5-point briefing to your email every day

## Example Output

1. Hyundai Demanding Tens of Thousands of Boston Dynamics Robots
   What: Hyundai is scaling up Boston Dynamics robot procurement for manufacturing.
   Why it matters: Mass deployment of humanoid robots is accelerating — this is the data flywheel moment for robotics AI.

2. Mozilla Used Anthropic's Mythos to Find and Fix 271 Bugs in Firefox
   What: AI agents autonomously identified and patched hundreds of real bugs in production code.
   Why it matters: Agentic coding is moving from demos to real-world deployment at scale.

## Tech Stack

- Python
- Groq API (LLaMA 3.3 70B)
- HackerNews Firebase API
- Reddit JSON API
- Gmail SMTP

## Setup

1. Clone the repo
   git clone https://github.com/yourusername/pulseai.git

2. Install dependencies
   pip install requests groq python-dotenv

3. Create a .env file
   GROQ_API_KEY=your_groq_api_key_here

4. Add your Gmail credentials to send_email.py

5. Run it
   python main.py

## Why I built this

I kept falling behind on AI developments while scrolling Instagram instead of learning. 
PulseAI fixes that — one email, every morning, only what matters.