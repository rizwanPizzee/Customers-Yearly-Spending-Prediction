# Ecommerce Store Customers Yearly Spending Prediction

## Purpose

This Flask web app predicts a customer's Yearly Amount Spent from four features.
It provides a simple web form (index.html) for entering feature values and returns the model prediction.

---
## Webiste
 - Link : https://customers-yearly-spending-predictio.vercel.app
## View The Nootbook

- Link 1: https://github.com/rizwanPizzee/Linear-Regression-E-commerce/blob/master/MLR.ipynb
- Link 2: https://nbviewer.org/github/rizwanPizzee/Linear-Regression-E-commerce/blob/master/MLR.ipynb

## Dataset

- **Filename used in the notebook:** `ecommerce.csv` (Link: https://www.kaggle.com/datasets/kolawale/focusing-on-mobile-app-or-website/data)

---

## Tools / Tech stack

- **Language:** Python
- **Notebook environment:** Jupyter Notebook
- **Libraries used:**
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
- **Web Stack:**
  - `Flask`
  - `HTML`
  - `CSS`

---

## ML models & techniques used

- **Linear Regression Model** — Supervised learning algorithm used to predict the customers yearly amount spendings.

---

## Project Structure

```
├── MLR.ipynb          # Nootbook conatins all EDA and ML related code
├── app.py             # Flask web application
├── models.py          # Machine learning pipeline
├── model.pkl          # Trained model (generated)
├── ecommerce.csv      # dataset
├── templates/
│   ├── index.html     # Main prediction interface
```
