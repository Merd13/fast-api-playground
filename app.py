from fastapi import FastAPI
import uvicorn

# Init
app = FastAPI(debug=True)


# Route
@app.get('/api/v1/health')
async def health_check():
    return {"status": "UP"}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")
