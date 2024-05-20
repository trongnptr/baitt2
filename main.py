from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(req: CalculationRequest):
    return {"result": req.a + req.b}

@app.post("/subtract")
def subtract(req: CalculationRequest):
    return {"result": req.a - req.b}

@app.post("/multiply")
def multiply(req: CalculationRequest):
    return {"result": req.a * req.b}

@app.post("/divide")
def divide(req: CalculationRequest):
    return {"result": req.a / req.b if req.b != 0 else "Cannot divide by zero"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
