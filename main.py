from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from image_detect import detect_emotions
import uuid


app = FastAPI()
STATIC_IMAGES = 'STATIC_IMAGES/'
@app.post('/image/detect')
async def image_detect_emotions(file: UploadFile = File(...)):
    contents = await file.read()
    file.filename = f"{uuid.uuid4()}.png"
    file_dir = f'{STATIC_IMAGES}{file.filename}'

    with open(file_dir, 'wb') as f:
        f.write(contents)

    emotions = detect_emotions(file_dir)
    return JSONResponse(content=emotions)
