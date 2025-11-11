```markdown
# 🏡 California House Price Prediction (Flask + Machine Learning)

A **Machine Learning + Flask web application** that predicts California housing prices based on various features such as location, median income, and housing statistics.  
This project demonstrates **data preprocessing, model training, and web deployment** — perfect for showcasing end-to-end Data Science & Full Stack ML skills.

---

## Features

- Trained **Random Forest Regressor** using `scikit-learn`
- Preprocessing with `Pipeline` and `ColumnTransformer`
- **Flask web app** for real-time predictions
- User input via interactive HTML form
- Model and preprocessing pipeline stored using `joblib`
- Evaluation metrics like RMSE and R² (internally logged)
- Organized project structure ready for deployment (Render / HuggingFace / etc.)

---

## Project Structure

```

house_price_prediction/
│
├── app.py                    # Flask web application
├── model.pkl                 # Trained Random Forest model (ignored in Git)
├── pipeline.pkl              # Data preprocessing pipeline (ignored in Git)
├── housing.csv               # Original dataset (California Housing)
├── input.csv                 # Test input for prediction
├── templates/
│   └── index.html            # Frontend HTML form
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

````

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS |
| **Backend** | Flask |
| **Machine Learning** | Scikit-learn, Pandas, NumPy |
| **Model** | Random Forest Regressor |
| **Pipeline** | ColumnTransformer + StandardScaler + OneHotEncoder |
| **Deployment** | Localhost (can be deployed to Render / HuggingFace) |

---

## Dataset

Used the **California Housing Dataset**, which contains data from the 1990 U.S. Census.

**Features:**
- `longitude`, `latitude`
- `housing_median_age`
- `total_rooms`, `total_bedrooms`
- `population`, `households`
- `median_income`
- `ocean_proximity` *(categorical)*

**Target:**
- `median_house_value` (in USD)

---

## Model Training

The model is trained using a **RandomForestRegressor** after applying:
- Median imputation for missing values  
- Feature scaling (`StandardScaler`)  
- One-hot encoding for categorical variables  

Training pipeline (`pipeline.pkl`) and model (`model.pkl`) are saved using `joblib`.

---

## How to Run Locally

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Dilkhushkumarcse/House-Price-Prediction.git
cd House-Price-Prediction
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# source venv/bin/activate  # For macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app

```bash
python app.py
```

Then open your browser and visit:
👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## Example Input (in Web Form)

| Feature            | Example Value |
| ------------------ | ------------- |
| Longitude          | -122.23       |
| Latitude           | 37.88         |
| Housing Median Age | 41            |
| Total Rooms        | 880           |
| Total Bedrooms     | 129           |
| Population         | 322           |
| Households         | 126           |
| Median Income      | 8.3252        |
| Ocean Proximity    | NEAR BAY      |

---

## Sample Output

> 🏠 **Predicted Median House Value:** $356,789.42

---

## 🧾 Future Improvements

* Add **Bootstrap UI** for a modern look
* Integrate **Model Evaluation Metrics** dashboard
* Deploy live on **Render / Hugging Face Spaces**
* Add **API endpoint** for JSON-based predictions

---

## 👨‍💻 Author

**Dilkhush Kumar**
🎓 B.Tech in Computer Science and Engineering (CSE)
💼 Aspiring Data Scientist & ML Engineer
📧 [[Email](mailto:dilkhush4kr@gmail.com)]
🌐 [GitHub Profile](https://github.com/Dilkhushkumarcse)

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on [GitHub](https://github.com/Dilkhushkumarcse/House-Price-Prediction)!
Your support motivates me to build more Data Science and AI projects.

````
<img width="568" height="481" alt="Screenshot 2025-11-11 135650" src="https://github.com/user-attachments/assets/c743a836-0b31-45db-84a8-24415d792216" />

