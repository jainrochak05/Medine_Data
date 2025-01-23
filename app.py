from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the dataset (Ensure 'medicine_data.csv' is in the correct directory)
try:
    dataset = pd.read_csv("medicine_data.csv")
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    dataset = None

@app.route('/get_medicine_info', methods=['POST'])
def get_medicine_info():
    try:
        # Ensure dataset is loaded
        if dataset is None:
            return jsonify({
                "error": "Dataset could not be loaded. Please check the file and try again."
            }), 500

        # Parse the incoming JSON request
        data = request.get_json()
        medicine_name = data.get("medicine_name", "").strip().lower()

        if not medicine_name:
            return jsonify({"error": "Medicine name is required"}), 400

        # Validate that necessary columns exist in the dataset
        required_columns = ["Medicine Name", "Composition", "Uses", "Side_effects"]
        for col in required_columns:
            if col not in dataset.columns:
                return jsonify({
                    "error": f"Dataset is missing the required column: '{col}'"
                }), 500

        # Normalize the 'Medicine Name' column for case-insensitive search
        dataset['Medicine Name'] = dataset['Medicine Name'].str.strip().str.lower()

        # Perform a partial match search (substring search)
        result = dataset[dataset['Medicine Name'].str.contains(medicine_name, na=False)]

        if not result.empty:
            # Extract the first matching row and build the response
            response = []
            for _, row in result.iterrows():
                response.append({
                    "medicine_name": row["Medicine Name"],
                    "composition": row.get("Composition", "N/A"),
                    "uses": row.get("Uses", "N/A"),
                    "side_effects": row.get("Side_effects", "N/A")
                })
            return jsonify(response), 200
        else:
            return jsonify({"error": "No matching medicine found"}), 404

    except Exception as e:
        # Handle unexpected errors and return details for debugging
        return jsonify({
            "error": "An internal server error occurred.",
            "details": str(e)
        }), 500

# Ensure the app listens on the correct port for Render deployment
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5004)))
