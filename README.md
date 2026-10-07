# 📧 Fake Email Detection

## 📌 About the Project

**Fake Email Detection** is a Machine Learning project that classifies email messages as **Spam** or **Ham (Legitimate)** based on their textual content.

The project uses **TF-IDF (Term Frequency–Inverse Document Frequency)** for text feature extraction and **Multinomial Naive Bayes** for email classification.

A **Streamlit web application** is also included, allowing users to enter an email message and get a prediction.

---

## 🎯 Objectives

* Detect spam or suspicious emails automatically.
* Convert email text into numerical features using TF-IDF.
* Train a machine learning classification model.
* Evaluate the model using standard classification metrics.
* Save the trained model for future predictions.
* Build a simple web interface using Streamlit.

---

## 🧠 Machine Learning Approach

The project follows this workflow:

```text
Email Text
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Multinomial Naive Bayes
    ↓
Prediction
    ↓
Spam / Ham
```

### 1. TF-IDF Vectorization

TF-IDF converts email text into numerical features that can be used by a machine learning model.

The vectorizer is configured with:

* `lowercase=True`
* `stop_words="english"`
* `max_features=5000`

### 2. Multinomial Naive Bayes

**Multinomial Naive Bayes** is a machine learning algorithm that works particularly well with text classification problems.

It learns patterns from labeled email messages and predicts whether a new email is **Spam** or **Ham**.

---

## 📊 Dataset

The project uses the **Enron Spam Email Dataset**.

### Dataset Details

| Property      |                 Value |
| ------------- | --------------------: |
| Dataset File  | `enron_spam_data.csv` |
| Total Emails  |                33,716 |
| Columns       |                     5 |
| Dataset Shape |          `(33716, 5)` |
| Problem Type  | Binary Classification |
| Classes       |            Spam / Ham |

### Dataset Columns

| Column       | Description                         |
| ------------ | ----------------------------------- |
| `Message ID` | Unique identifier of the email      |
| `Subject`    | Subject line of the email           |
| `Message`    | Main content of the email           |
| `Spam/Ham`   | Target label indicating Spam or Ham |
| `Date`       | Date associated with the email      |

### Class Distribution

The dataset contains approximately:

* **17,171 Spam emails**
* **16,545 Ham emails**
* **33,716 Total emails**

The dataset is used to train and evaluate the email classification model.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **TF-IDF**
* **Multinomial Naive Bayes**
* **Jupyter Notebook**
* **Streamlit**
* **Joblib / Pickle**

---

## 📁 Project Structure

```text
fake-email-detection/
│
├── Fake Mail.ipynb
├── app.py
├── enron_spam_data.csv
├── fake_email_model.pkl
├── tfidf_vectorizer.pkl
├── README.md
└── .gitignore
```

### File Description

| File                   | Purpose                                                     |
| ---------------------- | ----------------------------------------------------------- |
| `Fake Mail.ipynb`      | Data analysis, preprocessing, model training and evaluation |
| `app.py`               | Streamlit web application                                   |
| `enron_spam_data.csv`  | Email dataset                                               |
| `fake_email_model.pkl` | Saved trained machine learning model                        |
| `tfidf_vectorizer.pkl` | Saved TF-IDF vectorizer                                     |
| `README.md`            | Project documentation                                       |

---

## 🔄 Data Processing

The following steps are performed during model development:

1. Load the email dataset.
2. Inspect the dataset structure.
3. Handle missing values where required.
4. Prepare the email text.
5. Separate features and target labels.
6. Convert text into numerical features using TF-IDF.
7. Split the data into training and testing sets.
8. Train the Multinomial Naive Bayes model.
9. Evaluate the model.
10. Save the trained model and vectorizer.

---

## 📚 Train-Test Split

The dataset is divided into training and testing data.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

### Parameters

* `test_size=0.2` → 20% of the data is used for testing.
* `random_state=42` → Ensures reproducible results.
* `stratify=y` → Maintains the same class distribution in training and testing data.

---

## 🤖 Model Pipeline

The project uses a machine learning pipeline:

```python
Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_features=5000
    )),
    ("model", MultinomialNB())
])
```

This combines text feature extraction and classification into a single workflow.

---

## 📈 Model Evaluation

The model can be evaluated using the following metrics:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **Confusion Matrix**

### Why These Metrics?

**Accuracy:**
Measures the overall percentage of correctly classified emails.

**Precision:**
Measures how many emails predicted as spam are actually spam.

**Recall:**
Measures how many actual spam emails are correctly detected.

**F1-Score:**
Provides a balance between precision and recall.

> Add the exact metric values from your final notebook here rather than using estimated values.

---

## 🖥️ Streamlit Application

The project includes a Streamlit application that allows users to enter an email and classify it.

### Application Workflow

```text
User enters email
       ↓
Text is processed
       ↓
Saved TF-IDF Vectorizer
       ↓
Saved ML Model
       ↓
Prediction
       ↓
Spam / Ham
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/naveen057/qqq.git
```

### 2. Open the Project Directory

```bash
cd qqq
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

If a `requirements.txt` file is added later:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Example

### Example Input

```text
Congratulations! You have won a free prize.

Click the link below to claim your reward.
```

### Example Output

```text
Prediction: Spam
```

### Another Example

```text
Hi John,

Please find the meeting schedule attached.
Let's discuss the project tomorrow.

Regards,
David
```

### Example Output

```text
Prediction: Ham
```

---

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing
* Text preprocessing
* TF-IDF feature extraction
* Machine Learning classification
* Multinomial Naive Bayes
* Train-test splitting
* Stratified sampling
* Model evaluation
* Model serialization
* Streamlit application development

---

## 🚀 Future Improvements

* Compare Naive Bayes with Logistic Regression and SVM.
* Perform hyperparameter tuning.
* Add confidence/probability scores to predictions.
* Improve text preprocessing.
* Detect phishing links and suspicious URLs.
* Add sender-based features.
* Support multiple languages.
* Deploy the application online.
* Add a confusion matrix and performance dashboard.

---

## 📌 Project Highlights

* **33K+ email records**
* **5 dataset columns**
* **TF-IDF text feature extraction**
* **Multinomial Naive Bayes classification**
* **Saved ML model**
* **Streamlit prediction interface**
* **End-to-end NLP classification workflow**

---

## 📚 Dataset Source

The project uses the **Enron Spam Email Dataset** for spam/ham email classification.

---

## 👨‍💻 Author

**Naveen**

GitHub: [naveen057](https://github.com/naveen057?utm_source=chatgpt.com)
