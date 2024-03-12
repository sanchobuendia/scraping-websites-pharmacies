from fastapi import APIRouter, HTTPException
import pandas as pd
from utils.results_images import Results
from utils.utils import recent_file_input
from settings import settings

router = APIRouter()

@router.post("/scraperimages/")
async def upload_csv():
    """
    An asynchronous script for processing a recently uploaded CSV file containing image data.
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
        file_path = recent_file_input(f'{settings.storage_url}data_images')
        file_full_path = f'{settings.storage_url}data_images/{file_path}'

        # Read the CSV file into a DataFrame with specific separator and encoding
        df = pd.read_csv(file_full_path, sep=";", encoding='latin-1')

        # Add a "MATCH" column initialized with False
        df["MATCH"] = False

        # Get the current date for creating a unique output file name
        today = pd.Timestamp("today").strftime("%Y-%m-%d")

        # Specify the output path for saving the processed results
        out_path = f"{settings.storage_url}results_images/output_{today}.csv"

        # Instantiate the Results class with relevant parameters
        out = Results(
            df=df,
            folder_path=f'{settings.storage_url}target_images',
            out_path=out_path,
            threshold=0.8,
            path_dict=f"{settings.storage_url}farmacias_dict/dict_url.json"
        )

        # Use the Results class to generate and save the processed results
        out.create_output()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
