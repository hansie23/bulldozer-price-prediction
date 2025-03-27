# Bulldozer Price Prediction

This project is a web application designed to predict the sale price of bulldozers based on various features and historical sales data.

Deployed live at: [https://bulldozer-price-prediction.streamlit.app/](https://bulldozer-price-prediction.streamlit.app/)

## Description

The application utilizes a pre-trained machine learning model (`price_prediction_model.pkl`) to estimate bulldozer prices. Users can input various characteristics of a bulldozer through an interactive interface built with Streamlit, and the application will provide a predicted sale price.

## How it Works

1.  **Input Features:** The user provides details about the bulldozer via the sidebar interface, including:
    * Sale Date
    * Model ID
    * Product Size
    * Year Made
    * Enclosure type
    * Base Model
    * And other relevant machine specifications.
2.  **Data Preprocessing:** The input data undergoes several preprocessing steps:
    * Date features (Year, Month, Day, DayOfWeek, DayOfYear) are extracted from the sale date.
    * Missing numerical values are filled using the median.
    * Categorical features are converted into numerical representations.
    * Flags are created for missing values in both numeric and categorical columns.
3.  **Prediction:** The preprocessed data, formatted into the correct feature order, is fed into the loaded model to generate the price prediction.
4.  **Output:** The predicted price is displayed to the user.

## Setup and Installation

1.  **Prerequisites:** Ensure you have Python installed on your system.
2.  **Clone the repository (Optional):**
    ```bash
    git clone <your-repository-url>
    cd bulldozer-price-prediction
    ```
3.  **Install Dependencies:** Install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Model File:** Make sure the `price_prediction_model.pkl` file is present in the project's root directory.

## Usage

To run the application locally, navigate to the project directory in your terminal and run the following command:

```bash
streamlit run app.py
