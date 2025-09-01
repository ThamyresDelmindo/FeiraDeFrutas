from fastapi import FastAPI, Depends, Form
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from datetime import datetime
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

DB_URL = "mysql+mysqlconnector://root:Th%40my123@localhost:3306/feira_de_frutas"

engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

class UserChoice(Base):
    __tablename__ = "user_choices"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), nullable=False)
    fruit = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
def submit(username: str = Form(...), fruit: str = Form(...), db: Session = Depends(get_db)):
    item = UserChoice(username=username.strip(), fruit=fruit.strip())
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"saved": True, "id": item.id}
