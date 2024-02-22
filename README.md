# notes-ocr-transcriber
Transcribes an image with words in it into a editable text file.

## How to use
After cloning the repository, create a virtual environment and install prerequisites.

```
python3 -m -m venv ./venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Convert an image containing words into an editable text file using the following comamnd (note: parsing handwritten text is inconsistent).

```
python3 -m notes transcribe -i /path/to/image/note.jpeg -o /output/directory/
```
