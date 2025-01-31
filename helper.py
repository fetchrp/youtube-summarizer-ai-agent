from googleapiclient.discovery import build
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

youtube = build('youtube', 'v3', developerKey=os.getenv("YOUTUBE_API_KEY"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def fetch_youtube_info(video_id: str):
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()

    if "items" in response and len(response["items"]):
        title = response["items"][0]["snippet"]["title"]
        description = response["items"][0]["snippet"]["description"]
        return {"status": "valid", "title": title, "description": description}
    else:
        return {"status": "invalid", "title": "invalid", "description": "invalid"}

def get_summary(title: str, description: str):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Write a rough summary of what the YouTube video is about based on the title and description of the YouTube video.",
            },
            {
                "role": "user",
                "content": f"""
                The title of the video is:
                {title}

                The description of the video is: 
                {description}
                """
            }
        ],
        model="gpt-4o",
    )
    return response.choices[0].message.content


    
