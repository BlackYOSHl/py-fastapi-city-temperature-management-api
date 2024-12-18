from fastapi import FastAPI
from database import engine, Base
import crud
from schemas import CityCreate, TemperatureCreate
from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session

# Ініціалізація бази даних
Base.metadata.create_all(bind=engine)

# Ініціалізація FastAPI
app = FastAPI()


# Ендпоінти для Cities
@app.get("/cities/")
def read_cities(db: Session = Depends(get_db)):
    return crud.get_cities(db)


@app.post("/cities/")
def add_city(city: CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db, city)


# Ендпоінти для Temperatures
@app.get("/temperatures/")
def read_temperatures(db: Session = Depends(get_db)):
    return crud.get_temperatures(db)


@app.post("/temperatures/")
def add_temperature(
        temperature: TemperatureCreate, db: Session = Depends(get_db)
):
    return crud.create_temperature(db, temperature)
