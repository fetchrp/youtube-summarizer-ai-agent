![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)
![domain:entertainment](https://img.shields.io/badge/entertainment-3D8BD3)

**YouTube Summarizer AI Agent**

**Description**: This AI agent summarizes a YouTube video using the title and description of a YouTube video. The video ID is needed to fetch the title and description of a YouTube video.

**Input Data Model**
```
class Request(Model):
    video_id: str
```

**Output Data Model**
```
class Response(Model):
    summary: str
```

**Setup**
* Download [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/docs/)
* Get an [OpenAI API key](https://platform.openai.com/) and YouTube Data v3 API key and place it in the .env file
* Run ```python agent.py``` in your terminal

Documentation is WIP. 
