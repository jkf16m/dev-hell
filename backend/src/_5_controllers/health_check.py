from _5_controllers import app

@app.get("/health")
def read_root():
    return "A healthy result"
