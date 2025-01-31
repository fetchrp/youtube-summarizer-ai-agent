from uagents import Agent, Context, Model

agent = Agent(
    name="Example Agent",
    port=8001,
    mailbox=True,
    seed="Seed for Example Agent"
)

youtube_summarizer_agent = "agent1qg558vzx4yl5nkerzurmzce7775np92cemtt8jv9x7xx3y0s8halxjskx4a"

class Request(Model):
    video_id: str

class Response(Model):
    summary: str

@agent.on_event("startup")
async def startup(ctx: Context):
    await ctx.send(youtube_summarizer_agent, Request(video_id="2P1po37ztQI"))

@agent.on_message(Response)
async def message_handler(ctx: Context, sender: str, res: Response):
    ctx.logger.info(f"Summary: {res.summary}")

if __name__ == "__main__":
    agent.run()


