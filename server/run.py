from fastapi import FastAPI
from APIs.commutator import commutator as cm

def create_app():
    app = FastAPI(title="Journal++")
    app.include_router(cm)
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
