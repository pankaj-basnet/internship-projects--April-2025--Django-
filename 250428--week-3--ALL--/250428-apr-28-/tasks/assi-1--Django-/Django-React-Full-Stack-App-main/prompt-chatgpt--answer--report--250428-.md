# subtitle not included in prompt and report answer from prompt

---
---
---



---
---
---



---
---
---

Perfect!  
Here’s the first one: **Plain `.md` format**, simple, clean, no extra styling — just **headings**, **bullet points**, and **code blocks**.

---

# Full Stack Django + React App Development Report

## 1. Backend Development (Django)

### 1.1 Project Setup
- Create a Django project named `backend`:
  ```bash
  django-admin startproject backend
  cd backend
  ```

- Create a Django app named `api`:
  ```bash
  python manage.py startapp api
  ```

- Install required packages:
  ```bash
  pip install djangorestframework
  pip install djangorestframework-simplejwt
  pip install python-dotenv
  pip install django-cors-headers
  ```

- Create `requirements.txt`:
  ```text
  djangorestframework
  djangorestframework-simplejwt
  python-dotenv
  django-cors-headers
  ```

---

### 1.2 settings.py Modifications
- Enable installed apps:
  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'api',
      'rest_framework',
      'corsheaders',
  ]
  ```

- Add middleware for CORS:
  ```python
  MIDDLEWARE = [
      ...
      'corsheaders.middleware.CorsMiddleware',
  ]
  ```

- Configure REST framework with JWT Authentication:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ),
      'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.IsAuthenticated',
      ],
  }
  ```

- Add JWT settings:
  ```python
  SIMPLE_JWT = {
      'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
      'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
  }
  ```

- Database setting remains default (SQLite3):
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```

- Enable all CORS origins:
  ```python
  CORS_ALLOW_ALL_ORIGINS = True
  CORS_ALLOW_CREDENTIALS = True
  ```

---

### 1.3 Models (models.py)
- Create a simple `Note` model:
  ```python
  from django.db import models

  class Note(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.title
  ```

- Run migrations:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

### 1.4 Serializers (serializers.py)
- Create serializers for the Note model:
  ```python
  from rest_framework import serializers
  from .models import Note

  class NoteSerializer(serializers.ModelSerializer):
      class Meta:
          model = Note
          fields = '__all__'
  ```

---

### 1.5 Views (views.py)
- Define API views for CRUD operations:
  ```python
  from rest_framework import viewsets
  from .models import Note
  from .serializers import NoteSerializer
  from rest_framework.permissions import IsAuthenticated

  class NoteViewSet(viewsets.ModelViewSet):
      queryset = Note.objects.all()
      serializer_class = NoteSerializer
      permission_classes = [IsAuthenticated]
  ```

---

### 1.6 URL Routing (urls.py)
- Create API routes:
  ```python
  from django.urls import path, include
  from rest_framework.routers import DefaultRouter
  from .views import NoteViewSet

  router = DefaultRouter()
  router.register(r'notes', NoteViewSet)

  urlpatterns = [
      path('', include(router.urls)),
  ]
  ```

- Link app urls in project `urls.py`:
  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('api.urls')),
  ]
  ```

---

### 1.7 Create Superuser
- Create an admin user for testing:
  ```bash
  python manage.py createsuperuser
  ```

---

### 1.8 Admin Setup (admin.py)
- Register Note model:
  ```python
  from django.contrib import admin
  from .models import Note

  admin.site.register(Note)
  ```

---

## 2. Frontend Development (React)

### 2.1 Project Setup
- Create Vite React project:
  ```bash
  npm create vite@latest frontend -- --template react
  cd frontend
  npm install
  ```

- Install Axios and React Router DOM:
  ```bash
  npm install axios react-router-dom
  ```

---

### 2.2 Project Structure
- Organize files:
  ```
  src/
    assets/
    components/
    pages/
    styles/
    api.js
    App.jsx
    constants.js
    main.jsx
  ```

---

### 2.3 App.jsx
- Setup Routes and Protected Routes:
  ```jsx
  import react from "react";
  import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
  import Login from "./pages/Login";
  import Register from "./pages/Register";
  import Home from "./pages/Home";
  import NotFound from "./pages/NotFound";
  import ProtectedRoute from "./components/ProtectedRoute";

  function Logout() {
    localStorage.clear();
    return <Navigate to="/login" />;
  }

  function RegisterAndLogout() {
    localStorage.clear();
    return <Register />;
  }

  function App() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          } />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/register" element={<RegisterAndLogout />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    );
  }

  export default App;
  ```

---

### 2.4 ProtectedRoute.jsx
- Protecting authenticated routes:
  ```jsx
  import { Navigate } from "react-router-dom";

  export default function ProtectedRoute({ children }) {
    if (!localStorage.getItem("token")) {
      return <Navigate to="/login" />;
    }
    return children;
  }
  ```

---

### 2.5 API Communication (api.js)
- Axios setup for authentication and API calls:
  ```javascript
  import axios from 'axios';

  const API = axios.create({
    baseURL: 'http://localhost:8000/api/',
  });

  API.interceptors.request.use((req) => {
    const token = localStorage.getItem('token');
    if (token) {
      req.headers.Authorization = `Bearer ${token}`;
    }
    return req;
  });

  export default API;
  ```

---

### 2.6 Authentication Pages

#### Login.jsx
- Handle login and store token:
  ```jsx
  import { useState } from "react";
  import API from "../api";

  export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const login = async () => {
      const { data } = await API.post("token/", { username, password });
      localStorage.setItem("token", data.access);
      window.location = "/";
    };

    return (
      <form onSubmit={(e) => {e.preventDefault(); login();}}>
        <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    );
  }
  ```

---

#### Register.jsx
- Handle new user registration:
  ```jsx
  import { useState } from "react";
  import API from "../api";

  export default function Register() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const register = async () => {
      await API.post("register/", { username, password });
      window.location = "/login";
    };

    return (
      <form onSubmit={(e) => {e.preventDefault(); register();}}>
        <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
        <button type="submit">Register</button>
      </form>
    );
  }
  ```

---

### 2.7 Home.jsx
- Display and manage notes:
  ```jsx
  import { useEffect, useState } from "react";
  import API from "../api";

  export default function Home() {
    const [notes, setNotes] = useState([]);
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");

    useEffect(() => {
      fetchNotes();
    }, []);

    const fetchNotes = async () => {
      const { data } = await API.get("notes/");
      setNotes(data);
    };

    const addNote = async () => {
      await API.post("notes/", { title, content });
      fetchNotes();
    };

    return (
      <div>
        <h1>My Notes</h1>
        <form onSubmit={(e) => {e.preventDefault(); addNote();}}>
          <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />
          <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Content"></textarea>
          <button type="submit">Add Note</button>
        </form>
        <ul>
          {notes.map(note => (
            <li key={note.id}>{note.title} - {note.content}</li>
          ))}
        </ul>
      </div>
    );
  }
  ```

---

### 2.8 NotFound.jsx
- 404 page:
  ```jsx
  export default function NotFound() {
    return <h1>404 - Page Not Found</h1>;
  }
  ```

---

## 3. Conclusion

- Django backend handles user authentication and CRUD operations securely using JWT.
- React frontend interacts with the Django backend through protected APIs.
- Axios automatically attaches tokens for authenticated requests.
- React Router DOM is used for navigation and route protection.
- Project structured for scalability and future development.

---

✅ **Plain .md format DONE.**

---

Now, do you want me to start giving you the **styled GitHub README version** next? 🚀 (It'll have emojis, highlights, badges, little more "professional" GitHub polish.)  
Just reply **yes**! ✅

---
---
---



---
---
---



---
---
---



---
---
---


