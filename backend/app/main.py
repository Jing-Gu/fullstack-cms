from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.main import api_router_v1

app = FastAPI(title="Content Management API")

app.include_router(api_router_v1, prefix="/api/v1")


# Mount the static directory to serve the favicon
# app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Compas CMS API"}


# Route to serve the favicon
#@app.get("/favicon.ico", include_in_schema=False)
#async def favicon():
    #return RedirectResponse(url="/static/favicon.ico")


