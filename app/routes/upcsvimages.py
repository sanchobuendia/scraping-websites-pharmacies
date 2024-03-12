from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from pathlib import Path
from datetime import datetime
from settings import settings

router = APIRouter()

@router.post("/upcsvimages/")
async def upload_csv(csv_file: UploadFile = File(...)):
    """
    An asynchronous function for uploading and processing CSV files, specifically filtering
    rows where the 'REDE' column is set to 'DROGASIL' and saving the result to a storage location.

    Parameters:
    - csv_file (UploadFile): The CSV file to be uploaded and processed.

    Returns:
    - dict: A dictionary containing a success message upon successful file upload.

    Raises:
    - HTTPException: If there are errors during file processing, if the uploaded file
                     is not a CSV file, or if there are issues with the file content,
                     appropriate HTTP exceptions are raised with corresponding status codes
                     and error details.
    """
    try:
        # Check if the uploaded file has a valid CSV extension
        if not csv_file.filename.lower().endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        df = pd.read_csv(csv_file.file, sep=";", encoding='latin-1')

        df = df[df['NOME DAS IMAGENS'].notnull()]

        # Reset the index and drop any rows with NaN values
        df = df.reset_index(drop=True)

        # Get the current date and time for creating a unique file name
        today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Create a file path using the storage URL and the current date and time
        file_path = Path(f"{settings.storage_url}data_images/input_{today}.csv")

        # Save the processed DataFrame to the specified file path with 'latin-1' encoding
        df.to_csv(file_path, index=False, sep=";", encoding='latin-1')

        # Return a success message upon successful file upload
        return {"message": "File uploaded successfully"}

    except Exception as e:
        # Raise an HTTPException with a 500 status code if any other errors occur
        return HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

