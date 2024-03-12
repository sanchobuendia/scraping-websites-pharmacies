from fastapi import FastAPI
from routes import resultprice, resultimage, upcsvimages, upcsvprice, scraperprices, scraperimages, upimages

app = FastAPI()

app.include_router(upcsvprice.router, tags=["upcsvprice"], prefix="/api")
app.include_router(upcsvimages.router, tags=["upcsvimages"], prefix="/api")
app.include_router(upimages.router, tags=["upimages"], prefix="/api")
app.include_router(scraperprices.router, tags=["scraperprices"], prefix="/api")
app.include_router(scraperimages.router, tags=["scraperimages"], prefix="/api")
app.include_router(resultprice.router, tags=["resultprice"], prefix="/api")
app.include_router(resultimage.router, tags=["resultimage"], prefix="/api")

# uvicorn main:app --reload
# http://127.0.0.1:8000/docs