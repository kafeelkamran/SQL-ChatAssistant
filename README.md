# SQLite Chat Assistant 🚀

A lightweight FastAPI-based backend that interacts with an SQLite database to process user queries.  

## 🔹 Features
- **FastAPI** for handling requests  
- **Pydantic** for data validation  
- **SQLite** as the database  
- **Gradio** or **Frontend Support** (if applicable)  
- **REST API** endpoint for querying  

---

## 📌 Installation & Setup

### **1️⃣ Clone the Repository**
    ```sh
      git clone https://github.com/kafeelkamran/sqlite-chat-assistant.git
      cd sqlite-chat-assistant

### 2️⃣ Create & Activate Virtual Environment

      python -m venv venv
      venv\Scripts\activate

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 🚀 Running the Application
Start FastAPI Server

    uvicorn backend.main:app --host 0.0.0.0 --port 10000 --reload

### 🔥 Deploying the App
1️⃣ Deploy Locally
Use localhost:7860 for frontend if using Gradio.

    python app.py

2️⃣ Deploy to a Cloud Server
For production, use:

    uvicorn backend.main:app --host 0.0.0.0 --port 10000 --workers 4

### 🛠 Tech Stack
- Backend: FastAPI
- Database: SQLite
- Web Server: Uvicorn
- Frontend (Optional): Gradio / React

### 🤝 Contributing
- Fork the repo
- Create a branch: git checkout -b feature-branch
- Commit changes: git commit -m "Added feature"
- Push: git push origin feature-branch
- Open a PR
