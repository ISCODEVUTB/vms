import uvicorn
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware

from controller.vehicle_controller import VehicleController
from logic.vehicle import Vehicle

from controller.payment_method_controller import PaymentMethodController
from logic.payment_method import PaymentMethod

app = FastAPI()
vh_c = VehicleController()
pm_c = PaymentMethodController()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"200": "Welcome To Vehicle Management System"}


@app.get("/api/vehicle")
async def root():
    return vh_c.show()


@app.post("/compare_vehicle")
async def compare_vehicle(value: str = Query(...)):
    vehicles = vh_c.compare(value)
    return vehicles


@app.post("/api/vehicle")
async def add(id_vehicle: int, model: str, description: str, brand: str, type_v: str, weight: float, age: int,
              price: float, status: str):
    if vh_c.compare(str(id_vehicle)):
        return "A vehicle with the same ID already exists"
    else:
        return vh_c.add(Vehicle(id_vehicle=id_vehicle, model=model, description=description, brand=brand, type_v=type_v,
                                weight=weight, age=age, price=price, status=status))


@app.post("/api/delete_vehicle")
async def delete(value: str = Query(...)):
    vehicles = vh_c.delete(value)
    return vehicles


@app.get("/api/payment_method")
async def root():
    return pm_c.show()


@app.post("/api/payment_method")
async def add(payment_method: str):
    return pm_c.add(PaymentMethod(payment_method=payment_method))


@app.post("/api/select_payment_method")
async def select(value: str = Query(...)):
    selected_payment = pm_c.select(value)
    return selected_payment

if __name__ == '__main__':
    uvicorn.run(app, port=33507)
