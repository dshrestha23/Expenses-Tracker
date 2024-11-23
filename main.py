from fastapi import FastAPI
from routes import expenses, auth
import uvicorn

app = FastAPI(title="Expense Tracker API")

# Register routes
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
# app.include_router(expenses.router, prefix="/api", tags=["Expenses"])


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Expense Tracker API!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
