from sqlalchemy.orm import Session
from models import City, Temperature
from schemas import CityCreate, TemperatureCreate


# CRUD для City
def get_cities(db: Session):
    return db.query(City).all()


def create_city(db: Session, city: CityCreate):
    db_city = City(name=city.name, country=city.country)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


# CRUD для Temperature
def get_temperatures(db: Session):
    return db.query(Temperature).all()


def create_temperature(db: Session, temperature: TemperatureCreate):
    db_temperature = Temperature(
        city_id=temperature.city_id,
        temperature=temperature.temperature,
        time=temperature.time
    )
    db.add(db_temperature)
    db.commit()
    db.refresh(db_temperature)
    return db_temperature
