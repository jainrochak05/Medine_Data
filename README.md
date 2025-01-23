# Medicine Info API

This API provides detailed information about medicines based on a dataset of medical information. Users can query the API by providing a medicine name, and the API will return information such as composition, uses, and side effects. The API is built using Flask and includes robust error handling to ensure reliability.

## Features
- Retrieve medicine information such as composition, uses, and side effects.
- Perform partial match searches for medicine names.
- Detailed error messages for invalid inputs or missing data.
- Easily extensible to support additional features or data sources.

---

## Installation

### Prerequisites
- Python 3.8 or later
- `pip` package manager

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the `medicine_data.csv` file is placed in the root directory.

5. Run the Flask application:
   ```bash
   python app.py
   ```

---

## API Endpoints

### 1. `/get_medicine_info` (POST)
**Description**: Retrieves information about a medicine based on the provided name.

#### Request
- **Method**: POST
- **Headers**: `Content-Type: application/json`
- **Body**:
  ```json
  {
    "medicine_name": "<medicine_name>"
  }
  ```
  
#### Response
- **Success** (200):
  ```json
  [
    {
      "medicine_name": "Paracetamol",
      "composition": "Acetaminophen",
      "uses": "Relieves pain and fever",
      "side_effects": "Nausea, rash, liver damage"
    }
  ]
  ```
- **Error** (400):
  ```json
  {
    "error": "Medicine name is required"
  }
  ```
- **Error** (404):
  ```json
  {
    "error": "No matching medicine found"
  }
  ```
- **Error** (500):
  ```json
  {
    "error": "Dataset could not be loaded. Please check the file and try again."
  }
  ```

---

## Dataset Requirements
The dataset file `medicine_data.csv` should include the following columns:
- `Medicine Name`: The name of the medicine.
- `Composition`: The active ingredients of the medicine.
- `Uses`: The purpose or condition the medicine is used for.
- `Side_effects`: Potential side effects of the medicine.

Ensure all columns are named correctly and that the data is clean for optimal API functionality.

---

## Example Usage
### Sample cURL Request
```bash
curl -X POST http://127.0.0.1:5000/get_medicine_info \
-H "Content-Type: application/json" \
-d '{"medicine_name": "Paracetamol"}'
```

### Sample Python Request
```python
import requests

url = "http://127.0.0.1:5000/get_medicine_info"
data = {"medicine_name": "Paracetamol"}
response = requests.post(url, json=data)
print(response.json())
```

---

## Error Handling
The API is designed to handle various errors gracefully:
1. **Missing Dataset**: If the dataset file is not found, the API will return a 500 error.
2. **Invalid Input**: If the medicine name is not provided or is invalid, the API will return a 400 error.
3. **No Match Found**: If no medicine matches the query, the API will return a 404 error.

---

## Future Enhancements
- Add support for multilingual queries.
- Implement authentication and rate limiting.
- Integrate a live database for real-time updates.
- Add OCR support to extract medicine names from uploaded prescriptions.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the API.
