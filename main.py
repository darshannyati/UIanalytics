from uuid import uuid4
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select
from datetime import datetime
import uvicorn


from models import User
from database import get_session, create_db_and_tables

app = FastAPI()

SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/info/")
async def read_user_info(
    id: str,
    language: str,
    platform: str,
    gender: str,
    city: str,
    state: str,
    country: str,
    session: SessionDep
):
    try:
        rid = str(uuid4())
        request_time = datetime.utcnow()

        user = User(
            id=id,
            rid=rid,
            language=language,
            platform=platform,
            gender=gender,
            city=city,
            state=state,
            country=country,
            success=False,
            request_time=request_time,
            success_time=None
        )
        session.add(user)
        session.commit()
        session.refresh(user)

        return {
            "rid": rid,
            "paywall": {"test": "test"},
            "request_time": request_time.isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.post("/update-success/{rid}")
async def update_success(rid: str, session: SessionDep):
    try:
        statement = select(User).where(User.rid == rid)
        user = session.exec(statement).first()

        if not user:
            print(f"Debug: No user found with rid={rid}")  # Debugging line
            raise HTTPException(status_code=404, detail="User not found")
        
        user.success = True
        user.success_time = datetime.utcnow()
        session.add(user)
        session.commit()

        return {"status": "success", "rid": rid, "success_time": user.success_time.isoformat()}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)