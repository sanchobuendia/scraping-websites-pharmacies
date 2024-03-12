from fastapi import APIRouter, File, UploadFile, HTTPException
from settings import settings

router = APIRouter()

@router.post("/upimages/")
async def upimages(file: UploadFile = File(...)):
    """
    An asynchronous function for uploading image files to a designated storage location.

    Parameters:
    - file (UploadFile): The image file to be uploaded.

    Returns:
    - dict: A dictionary containing the uploaded file's filename upon successful upload.

    Raises:
    - HTTPException: If there are errors during file upload, an HTTP exception is raised
                     with a 500 status code and an error message.
    """
    contents = await file.read()
    try:
        # Open the specified file path and write the contents of the uploaded image file
        with open(f"{settings.storage_url}target_images/{file.filename}", "wb") as f:
            f.write(contents)

        # Return a dictionary with the filename upon successful file upload
        return {"filename": f"File {file.filename} uploaded successfully"}
    except Exception as e:
        # Raise an HTTPException with a 500 status code and an error message if an error occurs
        return HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")
