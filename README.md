## 🏡 California House Price Prediction — Flask + Machine Learning

A **Flask-based Machine Learning web application** that predicts the **median house value** in California based on various housing and demographic factors.
This project demonstrates an end-to-end ML workflow: **data preprocessing, model training, pipeline integration, and web deployment.**

---

###  Features

* **Random Forest Regression Model** for accurate price prediction
* **Preprocessing pipeline** with `ColumnTransformer` and `OneHotEncoder`
* **Flask web app** with user-friendly input form
* Model and pipeline saved using **Joblib**
* Input validation with clean exception handling
* Easy to deploy on **Render / Hugging Face / Localhost**

---

### Project Structure

```
California-House-Price-Prediction/
│
├── app.py                  # Flask web application
├── model.pkl               # Trained Random Forest model
├── pipeline.pkl            # Data preprocessing pipeline
├── housing.csv             # Original dataset
├── templates/
│   └── index.html          # Web interface (HTML form + prediction result)
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
```

---

### Tech Stack

| Category                 | Technology                          |
| ------------------------ | ----------------------------------- |
| **Programming Language** | Python                              |
| **Framework**            | Flask                               |
| **Libraries**            | Pandas, NumPy, Scikit-learn, Joblib |
| **Frontend**             | HTML, Bootstrap                     |
| **Version Control**      | Git, GitHub                         |
| **Tools**                | VS Code, Jupyter Notebook           |

---

### Dataset Description

Dataset used: **California Housing Dataset** (available via `sklearn.datasets.fetch_california_housing()` or CSV file).
**Features include:**

| Feature            | Description                                  |
| ------------------ | -------------------------------------------- |
| longitude          | Geographic coordinate                        |
| latitude           | Geographic coordinate                        |
| housing_median_age | Median age of houses in the district         |
| total_rooms        | Total number of rooms per block              |
| total_bedrooms     | Total number of bedrooms per block           |
| population         | Population of the district                   |
| households         | Number of households                         |
| median_income      | Median income of households                  |
| ocean_proximity    | Categorical feature (INLAND, NEAR BAY, etc.) |
| median_house_value | Target variable (in USD)                     |

---

### Model Training Overview

1. Loaded dataset and handled missing values
2. Used **StratifiedShuffleSplit** for splitting data
3. Built a preprocessing pipeline with:

   * `SimpleImputer` (median strategy)
   * `StandardScaler` (for numeric)
   * `OneHotEncoder` (for categorical)
4. Trained a **RandomForestRegressor** model
5. Saved both model and pipeline using `joblib.dump()`

---

### How to Run the Project

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Dilkhushkumarcse/California-House-Price-Prediction.git
cd California-House-Price-Prediction
```

#### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
# source venv/bin/activate   # (Mac/Linux)
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the Application

```bash
python app.py
```

#### 5️⃣ Open in Browser

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### Web Form Input Example

| Field              | Example  |
| ------------------ | -------- |
| Longitude          | -122.23  |
| Latitude           | 37.88    |
| Housing Median Age | 41       |
| Total Rooms        | 880      |
| Total Bedrooms     | 129      |
| Population         | 322      |
| Households         | 126      |
| Median Income      | 8.3252   |
| Ocean Proximity    | NEAR BAY |

---

### Example Output

> 🏠 **Predicted Median House Value:** $452,678.90

---

### requirements.txt

```txt
Flask
pandas
numpy
scikit-learn
joblib
```
