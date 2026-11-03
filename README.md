# SaleExpress

A web application built with Flask for user management and an online product catalog, featuring secure authentication, session control and a shopping cart.

## Overview

SaleExpress is a full-stack web project developed as part of my Systems Development course at ETEC. It covers the core flow of an online store: account creation, authentication, product browsing and cart management, using SQLite for persistence.

## Features

- User registration
- Login with hashed passwords
- Edit user profile data
- Account deletion (in progress)
- Session-based authentication (login and logout) with protected routes
- Product catalog
- Working shopping cart

## Tech Stack

| Layer     | Technology             |
|-----------|------------------------|
| Backend   | Python, Flask          |
| Database  | SQLite                 |
| Frontend  | HTML5, CSS3, JavaScript|
| Deploy    | Render                 |

## Security

- Passwords are stored as hashes using `werkzeug.security`
- Login credentials are verified with `check_password_hash`
- Flask `session` controls authentication and protects private routes

## Project Structure

```
SALEEXPRESS-COM-PYTHON/
├── app.py              Application entry point and routes
├── produto.py          Product data handling
├── templates/          HTML templates
├── static/             CSS, JavaScript and images
├── requirements.txt    Python dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DevFcodes/SALEEXPRESS-COM-PYTHON.git
   cd SALEEXPRESS-COM-PYTHON
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser at `http://127.0.0.1:5000`

## Screenshots

Add screenshots of the application here:

```
![Home page](docs/home.png)
![Product catalog](docs/catalog.png)
![Shopping cart](docs/cart.png)
```

## Roadmap

- Finish the account deletion feature
- Add a sidebar with category filters to the catalog
- Add automated tests for authentication and cart routes

## Author

**Fabricio**
GitHub: [@DevFcodes](https://github.com/DevFcodes)
Systems Development student at ETEC Uirapuru
