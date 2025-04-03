from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory=[
    "templates",
])

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    context = {
        "request": request,
    }
    response = templates.TemplateResponse("index.html", context=context)
    return response

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9500)