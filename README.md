# Smart AI Calculator

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-yellow?logo=javascript&logoColor=white)
![Google AI](https://img.shields.io/badge/Google%20Gemini-AI-green?logo=google&logoColor=white)

**Smart AI Calculator — Calculate. Learn. Understand.**  

A modern and intelligent calculator web app powered by **Flask (Python)** and **Google Gemini AI**, featuring real-time calculations, a sleek responsive UI, and **AI-powered step-by-step math explanations**.

---

# Table of Contents

1. [Features](#features)  
2. [Technologies Used](#technologies-used)  
3. [Project Structure](#project-structure)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Screenshots](#screenshots)  
7. [Author](#author)

---

## Features

- Perform real-time calculations (addition, subtraction, multiplication, division, etc.)  
- Responsive, modern UI with gradient design and smooth animations  
- **AI Explain** — uses **Google Gemini** to explain math expressions step-by-step  
- History section to track recent calculations  
- Keyboard input support  
- Secure `.env` handling for API keys  
- Works on both desktop and mobile screens  

---

## Technologies Used

- **Python (Flask)** — Backend logic and API handling  
- **Google Generative AI (Gemini)** — AI explanations for math problems  
- **HTML5** — App structure and layout  
- **CSS3** — Gradient UI, responsiveness, and glassmorphism design  
- **JavaScript (Fetch API)** — Handles frontend logic and API requests  
- **dotenv** — Manages API keys securely  
- **Git & GitHub** — Version control and hosting  

---

## Project Structure
```
calculator-project/
│
├── app.py 
├── index.html
├── style.csst
├── requirements.txt]
├── .gitignore
├── .env # 
└── README.md 
```

---

## Installation

### 1. Clone the Repository
```bash
   git clone https://github.com/vetrikarunanithi/smart-ai-calculator.git
   cd smart-ai-calculator
```
### 2. Create a Virtual Environment
```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
```
### 3. Install Dependencies
```bash
   pip install -r requirements.txt
```
### 4. Set Up Environment Variables
```bash
   GEMINI_API_KEY=your_google_gemini_api_key_here
```
### 5. Run the Flask Server
```bash
   python app.py
```
---

## Usage
- Open index.html in your browser.
- Enter numbers and operations like 8 + 8 / 2.
- Press = to calculate results in real time.
- Click “Explain with AI” 🤖 to get a detailed step-by-step explanation using Google Gemini.
- View your recent operations in the History section.

## Live Demo
[updating soon](https://smart-ai-calculator-alpha.vercel.app/)

---

## Author
**Vetriselvan Karunanithi**  
GitHub: [vetrikarunanithi](https://github.com/vetrikarunanithi)  

LinkedIn: [Vetriselvan Karunanithi](https://www.linkedin.com/in/vetriselvank)

