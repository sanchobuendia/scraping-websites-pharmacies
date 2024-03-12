from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
from pathlib import Path
import numpy as np
from settings import settings

router = APIRouter()

@router.get("/filter_result_prices/{filename}")
async def filter_result_prices(filename: str):
    """
    An asynchronous script for searching and retrieving results from a pricing analysis file.
    The script constructs the file path based on the provided filename, checks if the file exists,
    reads the CSV file into a DataFrame, converts it to a dictionary format, and returns the result
    as a JSON response.

    Parameters:
    - filename (str): The filename (excluding "output_") of the pricing analysis file to search for.

    Returns:
    - Union[JSONResponse, str]: A JSON response containing the results in a dictionary format,
                                or a string indicating that the file was not found.

    Raises:
    - HTTPException 500: If there are internal server errors during script execution.
    """
    try:
        # Construct the file path based on the provided filename
        folder_path = settings.storage_url + 'results_price'
        filename = "output_" + filename + ".csv"
        file_path = Path(folder_path) / filename

        # Check if the file exists
        if file_path.is_file():
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Replace NaN values with None in the DataFrame
            df.replace(np.nan, None, inplace=True)

            # Convert the DataFrame to a dictionary in records orientation
            df_dict = df.to_dict(orient="records")

            # Return a JSON response containing the results in dictionary format
            return JSONResponse(content=df_dict, media_type="application/json")
        else:
            # Return a string indicating that the file was not found
            return "File not found"

    except Exception as e:
        # Raise an HTTPException with a 500 status code for other internal server errors
        raise HTTPException(status_code=500, detail=str(e))

