"""This module transcribes a note image and writes to a file."""
# notes/transcriber.py

from pathlib import Path
import cv2
import easyocr

from notes import OUTPUT_PATH_DOES_NOT_EXIST_ERROR, OUTPUT_PATH_IS_NOT_A_DIRECTORY_ERROR, IMAGE_PATH_DOES_NOT_EXIST_ERROR, IMAGE_PATH_IS_NOT_A_FILE_ERROR, IMAGE_PROCESSING_ERROR, SUCCESS

def transcribe(image: str, output_dir: str) -> int:
	image_path = Path(image)
	output_dir_path = Path(output_dir)
	if not image_path.exists():
		return IMAGE_PATH_DOES_NOT_EXIST_ERROR
	if not image_path.is_file():
		return IMAGE_PATH_IS_NOT_A_FILE_ERROR
	if not output_dir_path.exists():
		return OUTPUT_PATH_DOES_NOT_EXIST_ERROR
	if not output_dir_path.is_dir():
		return OUTPUT_PATH_IS_NOT_A_DIRECTORY_ERROR

	if output_dir and not output_dir[len(output_dir) - 1] == '/':
		output_dir += '/'
	output_file_name = output_dir + image_path.name.replace(".", "_") + ".txt";

	image_encoded = cv2.imread(image)
	reader = easyocr.Reader(['en'], gpu=False)
	text_raw = reader.readtext(image)

	output_file_path = Path(output_file_name)
	output_file_path.touch()

	print(f'Writing transcription to {output_file_name}');

	full_transcription = ""

	for t in text_raw:
		bbox, text, score = t
		full_transcription += text
		full_transcription += "\n"

	output_file_path.write_text(full_transcription)

	return SUCCESS