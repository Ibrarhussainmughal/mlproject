# 🚀 Student Performance Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange)
![Bootstrap](https://img.shields.io/badge/UI-Premium-purple)

A premium Machine Learning web application that predicts student math scores based on various demographic and educational factors. Built with a robust Python backend and a modern, glassmorphism-inspired UI.

## 🌟 Live Demo
👉 **[Click here to view the Live App](https://mlproject-zwjt.onrender.com)**

## ✨ Features
- **🤖 Advanced AI Model**: Uses CatBoost and Scikit-Learn for high-accuracy predictions.
- **🎨 Premium UI**: A stunning, responsive interface with dark mode and glassmorphism effects.
- **⚡ Real-time Prediction**: Instant results based on user inputs.
- **📱 Mobile Responsive**: Works perfectly on all devices.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3 (Custom Premium Design), Jinja2
- **Backend**: Flask (Python)
- **Machine Learning**: CatBoost, XGBoost, Scikit-Learn, Pandas, Numpy
- **Deployment**: Render (Gunicorn)

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ibrarhussainmughal/mlproject.git
   cd mlproject
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   python app.py
   ```

5. **Open in Browser**
   Visit `http://127.0.0.1:5000`

## 📂 Project Structure
```
mlproject/
├── artifacts/          # Trained models and preprocessors
├── notebook/           # Jupyter notebooks for EDA and training
├── src/                # Source code for ML pipeline
│   ├── components/     # Data ingestion, transformation, training
│   └── pipeline/       # Prediction pipeline
├── static/             # CSS and assets
├── templates/          # HTML files
├── app.py              # Flask application entry point
└── requirements.txt    # Project dependencies
```

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License.