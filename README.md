# imgprcs# 🖼️ Full‑Stack Image Processor Application

A **production‑style full‑stack image processing web app** built with **FastAPI, OpenCV, NumPy, Pandas, PostgreSQL** on the backend and **React (Vite + TypeScript), Axios, Chart.js** on the frontend.

This project is designed to be **portfolio‑ready**, demonstrating backend APIs, image processing, authentication, data persistence, frontend state management, and Dockerised deployment.

---

## 🚀 Features

### 🔐 Authentication

* JWT‑based signup & login
* Password hashing (bcrypt)
* Protected API routes

### 🖼️ Image Processing

* Upload images
* Grayscale
* Blur
* Edge detection
* Brightness & contrast adjustment
* Saturation adjustment

### 📊 Analytics

* Image statistics: mean, std, min, max
* Chart visualisation (Chart.js)
* Metadata persistence (resolution, format)

### 🕹️ UX

* Undo / redo (Ctrl+Z / Ctrl+Y)
* Image edit history
* Menu bar
* Validation & error handling

### 🗄️ Persistence

* Store original & edited images
* Store analytics in PostgreSQL

### 🐳 DevOps

* Docker & Docker Compose

---

## 🧱 Architecture

```
┌──────────────────┐
│   React (Vite)   │
│  TypeScript UI   │
│  Chart.js        │
│  Axios           │
└─────────▲────────┘
          │ JWT / JSON / Images
          ▼
┌──────────────────┐
│     FastAPI      │
│  Auth (JWT)      │
│  OpenCV          │
│  NumPy / Pandas  │
│  Pydantic        │
└─────────▲────────┘
          │ SQLAlchemy
          ▼
┌──────────────────┐
│  PostgreSQL DB   │
│  Users           │
│  Images          │
│  Image Stats     │
└──────────────────┘
```

---

## 🔑 JWT Authentication Flow

1. User signs up / logs in
2. Backend issues JWT token
3. Token stored in `localStorage`
4. Axios attaches token to headers
5. Protected endpoints validate token

---

## 🖌️ Image Editing Flow

1. Upload image
2. Backend returns metadata + stats
3. User applies edits (sliders/buttons)
4. Each edit saved in undo/redo stack
5. Final image persisted on save

---

## ⚠️ Validation & Error Handling

### Backend

* Pydantic schema validation
* File type & size checks
* Auth dependency guards
* Consistent HTTP status codes

### Frontend

* Required input checks
* Disabled actions when invalid
* API error handling via Axios interceptors

---

## 🐳 Running the Project

```bash
# Backend
docker compose up --build

# Frontend
npm install
npm run dev
```

---

## 📦 Tech Stack

**Backend**

* FastAPI
* OpenCV
* NumPy, Pandas
* PostgreSQL
* SQLAlchemy
* JWT (python‑jose)

**Frontend**

* React + Vite
* TypeScript
* Axios
* Chart.js

---

## 🌟 Why This Project Matters

This project demonstrates:

* Real‑world API design
* Secure authentication
* Image processing pipelines
* State management (undo/redo)
* Database‑backed analytics
* Dockerised full‑stack deployment

Perfect as a **Data / Software / Full‑Stack portfolio project**.

---

## 📌 Future Improvements

* Async background processing
* Image thumbnails
* Cloud storage (S3)
* CI/CD pipeline
* Role‑based access

---

👤 **Author**: *Sheetu*
