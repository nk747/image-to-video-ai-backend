from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import replicate
import os

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set your Replicate API token
os.environ["REPLICATE_API_TOKEN"] = "r8_Ao1SNGOiUDwTukeMfxZ09HVq0EcmWO24WocQH"

class Prompt(BaseModel):
    prompt: str
    image_url: str = None

@app.post("/generate-image")
async def generate_image(data: Prompt):
    try:
        output = replicate.run(
            "stability-ai/sdxl:latest",
            input={"prompt": data.prompt}
        )
        return {"image_url": output[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-video")
async def generate_video(data: Prompt):
    try:
        # Placeholder logic
        return {"video_url": "https://yourdomain.com/fake-video.mp4"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
