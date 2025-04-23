
# **Ad Campaign Budgeting System**

This project implements a system to manage daily and monthly advertising campaign budgets. It allows monitoring and managing budgets, turning campaigns on/off when budget limits are reached, and configuring the day and time when campaigns should run (dayparting).

## **Project Structure**

The system is developed using Django, Django REST Framework, and follows SOLID principles to maintain a clean and modular architecture.

## **Requirements**

- Python 3.8+
- Django 4.x
- Django REST Framework

---

## **Installation**

### 2. Create and activate the virtual environment

Create a virtual environment for the project:

```bash
python -m venv .venv
```

Activate the virtual environment:

- On Windows:

```bash
.venv\Scripts\activate
```

- On Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

Install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## **Database Configuration**

This project uses SQLite by default, but you can configure Django to use other databases like PostgreSQL or MySQL.

Edit the `settings.py` file to configure the database as needed.

---

## **Running the Project**

### 1. Migrate the database

Before running the server, apply the migrations:

```bash
python manage.py migrate
```

### 2. Run the development server

To run the development server, use:

```bash
python manage.py runserver
```

This will start the server at `http://127.0.0.1:8000/`.

---

## **Testing**

This project includes automated tests to ensure the system behaves as expected.

To run the tests, use:

```bash
python manage.py test
```

---

## **API**

The system provides an API to manage advertising campaigns. The API is configured with Django REST Framework.

The main API routes include:

- **GET /api/campaigns/** – List all campaigns.
- **POST /api/campaigns/** – Create a new campaign.
- **PUT /api/campaigns/{id}/** – Update an existing campaign.
- **DELETE /api/campaigns/{id}/** – Delete a campaign.

The full API documentation can be accessed directly in the browser if you are using Django REST Framework with Swagger or Redoc.

---

## **License**

This project is for use in a technical challenge only.
