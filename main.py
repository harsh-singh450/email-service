from fastapi import FastAPI
from routers import transactional, newsletters, marketing, system_notifications

app = FastAPI(
    title="Email Alert System",
    description="A centralized system for sending different types of emails.",
    version="1.0.0"
)

# Include all the routers from the routers directory
app.include_router(transactional.router)
app.include_router(newsletters.router)
app.include_router(marketing.router)
app.include_router(system_notifications.router)


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Email Alert System API!"}