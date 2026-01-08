from fastapi import FastAPI
app = FastAPI(
    titlle= "Netflix Clone API",
    version= "0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "Backend",
        "version": "0.1.0"
    }
