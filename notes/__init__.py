"""Top-level package for Notes OCR Transcriber."""
# notes/__init__.py

__app_name__ = "notes"
__version__ = "0.0.1"

(
	SUCCESS,
	OUTPUT_PATH_DOES_NOT_EXIST_ERROR,
	OUTPUT_PATH_IS_NOT_A_DIRECTORY_ERROR,
	IMAGE_PATH_DOES_NOT_EXIST_ERROR,
	IMAGE_PATH_IS_NOT_A_FILE_ERROR,
	IMAGE_PROCESSING_ERROR
) = range(6)

ERRORS = {
	OUTPUT_PATH_DOES_NOT_EXIST_ERROR: "Output directory does not exist",
	OUTPUT_PATH_IS_NOT_A_DIRECTORY_ERROR: "Output path is not a directory",
	IMAGE_PATH_DOES_NOT_EXIST_ERROR: "Image file does not exist",
	IMAGE_PATH_IS_NOT_A_FILE_ERROR: "Image path is not a file",
	IMAGE_PROCESSING_ERROR: "Failed to process image"
}