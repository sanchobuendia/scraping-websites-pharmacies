from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from datetime import datetime
from pathlib import Path
from settings import settings


router = APIRouter()

@router.post("/upcsvprice/")
async def uploadprice(csv_file: UploadFile = File(...)):
    """
    An asynchronous function for uploading and processing CSV files containing pricing data.

    Parameters:
    - csv_file (UploadFile): The CSV file to be uploaded and processed.

    Returns:
    - dict: A dictionary containing a success message upon successful file upload.

    Raises:
    - HTTPException: If there are errors during file processing or if the uploaded file
                     is not a CSV file, appropriate HTTP exceptions are raised with
                     corresponding status codes and error details.
    """
    try:
        # Check if the uploaded file has a valid CSV extension
        if not csv_file.filename.lower().endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        df = pd.read_csv(csv_file.file, sep=";", encoding='latin-1')

        # Drop rows with all NaN values and convert all columns to strings
        df = df[df['APRESENTAÇÃO'].notnull()]
        df = df.astype(str)

        # Get the current date and time for creating a unique file name
        today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Create a file path using the storage URL and the current date and time
        file_path = Path(f"{settings.storage_url}data_price/input_{today}.csv")

        # Save the processed DataFrame to the specified file path
        df.to_csv(file_path, index=False)

        # Return a success message upon successful file upload
        return {"message": "File uploaded successfully"}

    except Exception as e:
        # Raise an HTTPException with a 500 status code if any other errors occur
        return HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


