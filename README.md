# 🏠 HouseFinder - AI-Powered House Price Prediction

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-success?logo=django)](https://www.djangoproject.com/)
[![License](https://img.shields.io/github/license/yourusername/housefinder)](LICENSE)
[![Made with ❤️ by Pratap](https://img.shields.io/badge/Made%20by-Pratap%20Choubey-critical)](mailto:pratapchoubey.ai@gmail.com)

**HouseFinder** is a modern AI-powered web app that predicts house prices based on features like bedrooms, bathrooms, area, condition, and nearby schools. Built with Django and a trained machine learning model (RandomForest + GridSearch), it delivers accurate, real-time price estimations.

![HouseFinder Demo](https://user-images.githubusercontent.com/your-demo-gif.gif)

---

## 🚀 Features

- 🎯 **Real-Time Price Prediction** using Machine Learning
- 🧠 **AI Model Integration** (RandomForestRegressor with GridSearchCV)
- 🏠 **Clean UI/UX**: Modern, responsive, animated frontend
- 📊 Dynamic data entry for features like bedrooms, bathrooms, area, etc.
- 🔗 Connected via Django templates, views, and ML models
- 📂 Modular code: Easily scalable & customizable

---

## 🛠️ Tech Stack

| Technology       | Description                     |
|------------------|---------------------------------|
| 🐍 Python        | Backend Language                |
| 🌿 Django        | Web Framework                   |
| 🤖 Scikit-Learn  | Machine Learning Model          |
| 🧠 RandomForest  | Regression Algorithm             |
| 📄 HTML/CSS/JS   | Frontend                        |
| 🎨 Font Awesome  | UI Icons                        |

---

## 📸 Screenshots

| Home Page | Prediction Page | About Page |
|-----------|-----------------|------------|
| <img width="500" alt="Home" src="https://github.com/user-attachments/assets/03689116-d84c-459f-a23a-3d86d65bebe9" /> | <img width="500" alt="Predict" src="https://github.com/user-attachments/assets/5b9f508a-17ea-4dc5-8717-f8bf3fd998f5" /> | <img width="500" alt="About" src="https://github.com/user-attachments/assets/d573c203-184c-490f-93db-d2d4885d2110" /> |


---
🧠 Model Info
Algorithm: Random Forest Regressor

Optimization: GridSearchCV

Inputs:

Bedrooms

Bathrooms

Living Area (sqft)

House Condition

Nearby Schools

💡 Example Prediction
Input	Output
Bedrooms: 3	₹ 52,45,000
Bathrooms: 2	
Area: 1500 sqft


## 🧑‍💻 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/housefinder.git
cd housefinder

📁 Project Structure
arduino
Copy
Edit
housefinder/
├── manage.py
├── houseprediction/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── home/
│   ├── views.py
│   ├── templates/
│   │   ├── home.html
│   │   └── predict.html
│   ├── model.pkl
│   └── ...
├── static/
│   ├── css/
│   └── images/

Condition: 4	
Schools Nearby: 3	

