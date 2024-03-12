from typing import List, Optional
from pydantic import BaseModel

class ScraperPriceBody(BaseModel):
    """
    A Pydantic model for the request body of the /scraperprices/ endpoint.
    """
    file_path: str