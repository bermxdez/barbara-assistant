# Barbara Assistant

Barbara Assistant is a simple weather assistant built in Python.  
It prompts the user for their name, allows weather lookup by city, and stores the search history locally in a JSON file.

## Features

- Interactive console menu (check weather, view search history, exit)
- Input validation for name and city
- Integration with the wttr.in API
- Local data persistence using JSON
- Modular file structure with separation of concerns
- English-based code and clean organization for portfolio presentation

## Technologies used

- Python 3.10+
- requests (for HTTP requests)
- Standard Python libraries: `json`, `datetime`
- Local Python modules organized in `api/`, `utils/`, `storage/`

## How to run

1. Clone this repository  
2. Navigate to the project folder and create a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the assistant:

   ```bash
   python3 main.py
   ```
