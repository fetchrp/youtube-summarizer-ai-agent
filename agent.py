from uagents import Agent, Context, Model
from helper import get_summary, fetch_youtube_info
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="YouTube Summarizer Agent",
    port=8000,
    seed="Seed for YouTube Summarizer Agent",
    mailbox=True
)

class Request(Model):
    video_id: str

class Response(Model):
    summary: str

@agent.on_message(Request)
async def message_handler(ctx: Context, sender: str, req: Request):
    video_info = fetch_youtube_info(req.video_id)
    status = video_info["status"]
    title = video_info["title"]
    description = video_info["description"]
    if status == "valid":
        summary = get_summary(title, description)
        await ctx.send(sender, Response(summary=summary))
    else:
        await ctx.send(sender, Response(summary="This is an invalid video ID. Please try again."))


if __name__ == "__main__":
    agent.run()


