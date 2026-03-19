from fastapi import FastAPI
app = FastAPI()

@app.get("/shipment")
def get_shipment():
    return {"content" : "wooden table",
            "weight" : 100,
            "destination" : "New York"
            }