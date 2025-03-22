# Xagi Demo Project

This repository contains an e-commerce application where users can select clothing models, and the models will virtually "wear" the selected clothes. The application consists of a FastAPI backend and a Next.js frontend.

## Overview

The application allows users to:
1. Browse through a collection of clothing items.
2. Select a model to virtually try on the clothes.
3. View the model wearing the selected outfit.

The backend is built using **FastAPI**, and the frontend is built using **Next.js**.

---

## Backend Setup (FastAPI)

The FastAPI backend serves as the API for the e-commerce application. It handles requests related to model and clothing data.

### Prerequisites
- Python 3.7 or higher
- Pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/UzitheI/xagi_demo_project.git
   cd xagi_demo_project
   ```
2. Create a virtual environment (optional but recommended):
   ```
     python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
     pip install -r requirements.txt
   ```
4. Run the FastAPI server:
   ```
     uvicorn main:app --reload
   ```
5. The FastAPI app will be running at http://127.0.0.1:8000. You can access the interactive API docs at http://127.0.0.1:8000/docs.

# Frontend Setup (Next.js)
The Next.js frontend provides the user interface for the e-commerce application.

### Prerequisites
- Node.js 16 or higner
- npm or yarn

### Installation
1. Navigate to the nextapp directory:
   ```
     cd xagi_demo
   ```
2. Install Dependencies:
   ```
     npm install
   ```
3. Run the server:
  ```
    npm run dev
  ```
### How it works
- Model Selection: Users can select a model from the available options.
- Virtual Try-On: The selected model will virtually wear the chosen clothes, and the result will be displayed on the screen.


   
