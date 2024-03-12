from fastapi import APIRouter, HTTPException
import pandas as pd

from utils.results_prices import Results
from utils.utils import recent_file_input
from utils.models import ScraperPriceBody
from settings import settings

router = APIRouter()

@router.post("/scraperprices/")
async def upload_csv():
    """
    An asynchronous script for processing a recently uploaded CSV file containing pricing data.
    The script reads the CSV file, performs specific processing using the Results class,
    and saves the results to a storage location.

    Returns:
    - dict: A dictionary containing a success message upon successful execution.

    Raises:
    - HTTPException 404: If the input CSV file is not found.
    - HTTPException 500: If there are internal server errors during script execution.
    """
    try:
        # Get the most recent CSV file from the specified storage location
        file_path = recent_file_input(f'{settings.storage_url}data_price')
        file_full_path = f'{settings.storage_url}data_price/{file_path}'

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_full_path)

        # Instantiate the Results class with the DataFrame and a dictionary path
        out = Results(df, path_dict=f"{settings.storage_url}farmacias_dict/dict_url.json")

        # Get the current date for creating a unique output file name
        today = pd.Timestamp("today").strftime("%Y-%m-%d")

        # Specify the output path for saving the processed results
        out_path = f"{settings.storage_url}results_price/output_{today}.csv"

        # Use the Results class to generate and save the processed results
        out.output(out_path=out_path)

        # Return a success message upon successful script execution
        return {'message': 'Results saved'}

    except FileNotFoundError:
        # Raise an HTTPException with a 404 status code if the input file is not found
        raise HTTPException(status_code=404, detail="File not found")

    except Exception as e:
        # Raise an HTTPException with a 500 status code for other internal server errors
        raise HTTPException(status_code=500, detail=f"Internal server error, scraperprices: {str(e)}")

