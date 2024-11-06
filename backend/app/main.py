from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.api.v1.main import api_router_v1

app = FastAPI(title="Content Management API")

app.include_router(api_router_v1, prefix="/api/v1")


# Mount the static directory to serve the favicon
# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


# Route to serve the favicon
#@app.get("/favicon.ico", include_in_schema=False)
#async def favicon():
    #return RedirectResponse(url="/static/favicon.ico")


