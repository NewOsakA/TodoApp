# TodoApp

**TodoApp** is a web-based application for managing personal todo list. Integrating with [Neon](https://neon.tech/) and [Cloudinary](https://cloudinary.com/) for database storing.

---

## Getting Started

Follow these steps to set up the project locally.

---

### 1. Clone the Repository

```bash
git clone https://github.com/NewOsakA/TodoApp.git
```

### 2. Navigate to the project directory

```bash
cd TodoApp
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual environment

For Mac/Linux

```bash
source myenv/bin/activate
```

For Windows

```bash
.\myenv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Environment Setup

We provide a `sample.env` file with all necessary environment variables.
Create your own .env file by copying it:

### To create a .env file in terminal

For Mac/Linux

```bash
cp sample.env .env
```

For windows

```bash
copy sample.env .env
```

### 7. Setup Required Services

You'll need the following services to run the app properly:

* A PostgreSQL database
  via [neon.tech Postgre database](https://www.youtube.com/watch?v=kvIK2NpuF2I)
* A Cloudinary account for media
  uploads [Cloudinary tutorial](https://cloudinary.com/documentation/python_quickstart)

---


### 8. Database Setup (first time only)

Run the following commands to set up your database for the first time:

```bash
python manage.py makemigrations
```

and then

```bash
python manage.py migrate
```

### 9. Start the Development Server

```commandline
python manage.py runserver
```

Then open your browser and go to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)