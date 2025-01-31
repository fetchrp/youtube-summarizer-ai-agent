![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)
![domain:entertainment](https://img.shields.io/badge/entertainment-3D8BD3)

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

Documentation is WIP. 
