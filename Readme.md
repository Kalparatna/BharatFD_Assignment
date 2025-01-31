
# 📝 Multilingual FAQ API (Django)

This is a backend project for managing FAQs with **multi-language support** and **WYSIWYG editor integration** using Django and CKEditor.  
It supports **automatic translations** and **caching** to optimize API responses.

---

## 🚀 Features  
✅ Store FAQs with **rich-text formatting** using CKEditor.  
✅ Support for **multiple languages** (English, Hindi, Bengali).  
✅ Automatic **Google Translate** integration.  
✅ **Fast API responses** with **Redis caching**.  
✅ REST API for CRUD operations.  
✅ Admin panel for FAQ management.  
✅ **Docker support** .  

---

## 📂 Directory Structure  

```
BharatFD-Assignment/
│── faq/                       
│   ├── migrations/            
│   ├── templates/               
│   ├── tests.py                 
│   ├── views.py                
│   ├── serializers.py         
│   ├── urls.py                  
│   ├── models.py              
│── project/                     
│── static/                      
│── templates/                  
│── manage.py                    
│── requirements.txt              
│── Dockerfile                     
│── README.md                     
```

---

## 🛠️ Installation  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/Kalparatna/BharatFD_Assignment.git
cd BharatFD_Assignment
```

### **2️⃣ Create and Activate a Virtual Environment**  
```sh
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **5️⃣ Apply Migrations**  
```sh
python manage.py migrate
```

### **6️⃣ Create a Superuser** (for Django Admin)  
```sh
python manage.py createsuperuser
```

### **7️⃣ Run the Development Server**  
```sh
python manage.py runserver
```

---

## 🔗 API Endpoints  

### **📌 Get FAQs (Default: English)**  
```sh
GET /api/faqs/
```
**Response**:  
```json
[
  {
    "id": 1,
    "question": "What is Django?",
    "answer": "Django is a Python framework."
  }
]
```

### **📌 Get FAQs in Hindi**  
```sh
GET /api/faqs/?lang=hi
```
**Response**:  
```json
[
  {
    "id": 1,
    "question": "Django क्या है?",
    "answer": "Django एक पायथन फ्रेमवर्क है।"
  }
]
```

### **📌 Get FAQs in Bengali**  
```sh
GET /api/faqs/?lang=bn
```

---

## 🔍 Running Tests  
To run unit tests, use:  
```sh
python manage.py test
```

---

## 🚀 Deployment with Docker  

### **1️⃣ Build the Docker Image**  
```sh
docker build -t BharatFD_Assignment .
```

### **2️⃣ Run the Container**  
```sh
docker run -p 8000:8000 BharatFD_Assignment
```

---
