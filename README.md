# Smart Job Application Tracker (Python CLI)

A command-line based job application tracking system built using Python.  
This project helps users manage and track job applications efficiently with features such as status updates, filtering, and persistent storage.

---

## 📌 Features

- Add new job applications  
- View all applications  
- Update application status  
- Withdraw applications (soft delete)  
- Filter applications by status  
- Persistent storage using CSV  
- Clean and user-friendly CLI interface  

---

## 🧠 Project Motivation

While applying for multiple jobs, keeping track of application statuses across platforms becomes difficult.  
This project was built to simulate a real-world tracking system while demonstrating strong Python fundamentals and clean software design.

---

## 🏗️ Project Architecture

The application follows a layered architecture:

CLI Layer → User interaction

Service Layer → Business logic

Model Layer → Data representation & validation

Storage Layer → File persistence



---

## 📁 Folder Structure

     smart-job-application-tracker/
     │
     ├── cli/
     │ └── menu.py
     │
     ├── models/
     │ └── job_application.py
     │
     ├── services/
     │ └── application_manager.py
     │
     ├── storage/
     │ └── storage_handler.py
     │
     ├── data/
     │ └── applications.csv
     │
     ├── main.py
     ├── README.md
     ├── requirements.txt
     └── .gitignore



---

## ⚙️ Technologies Used

- Python 3  
- Object-Oriented Programming (OOP)  
- CSV file handling  
- Exception handling  
- Datetime module  
- Command Line Interface (CLI)  

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

    git clone https://github.com/your-username/smart-job-application-tracker.git

    cd smart-job-application-tracker

2️⃣ Run the application

    python main.py

---

## 🧪 Sample Menu

    1. Add application
    2. View all applications
    3. Update application status
    4. Withdraw application
    5. Filter applications by status
    6. Exit

---

## 📊 Supported Application Statuses

    Applied
    Interview
    Rejected
    Offer
    Withdrawn
    Other

---

## 💡 Key Design Decisions

* **Soft delete approach**

    Applications are never removed from storage; instead, their status is updated to Withdrawn.

* **CSV-based persistence**

    Lightweight and readable storage format suitable for CLI applications.

* **Centralized validation**

    Validation logic is implemented in the domain model to avoid duplicated checks.

* **Clean separation of concerns**

    Each layer handles a single responsibility.

---

## 🚀 Future Improvements

* GUI version using Tkinter or PyQt
* Web version using Flask or FastAPI
* Resume parsing integration
* Application analytics dashboard
* ML-based job outcome prediction

---

## 👨‍💻 Author
**Jithesh Shetty** \
B.Tech Computer Science Engineering (AI & ML)

---

## ⭐ Feedback
If you found this project useful, feel free to star the repository ⭐ \
Suggestions and improvements are welcome.

