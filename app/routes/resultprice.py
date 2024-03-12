from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
from utils.utils import recent_file_output
from settings import settings

router = APIRouter()

@router.get("/resultprice/")
async def result_price():
    """
    An asynchronous script for retrieving and returning the results of a pricing analysis.
    The script reads the most recent output CSV file, converts it to a JSON format, and returns
    the result as a JSON response.

    Returns:
    - JSONResponse: A JSON response containing the results in a dictionary format.

    Raises:
    - HTTPException 404: If the output CSV file is not found.
    - HTTPException 500: If there are internal server errors during script execution.
    """
    try:
        # Get the most recent output CSV file from the specified storage location
        file_path = recent_file_output(f'{settings.storage_url}results_price')
        file_full_path = f'{settings.storage_url}results_price/{file_path}'

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_full_path)

        # Replace NaN values with None in the DataFrame
        df.replace(np.nan, None, inplace=True)

        # Convert the DataFrame to a dictionary in records orientation
        df_dict = df.to_dict(orient="records")

        # Return a JSON response containing the results in dictionary format
        return JSONResponse(content=df_dict, media_type="application/json")
    
    except FileNotFoundError:
        # Raise an HTTPException with a 404 status code if the output file is not found
        raise HTTPException(status_code=404, detail="File not found")

    except Exception as e:
        # Raise an HTTPException with a 500 status code for other internal server errors
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

