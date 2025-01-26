# Data Repository Service (DRS) API

This project implements the **Data Repository Service (DRS)** API specification using **FastAPI**. The DRS API provides a generic interface to data repositories, allowing data consumers to access data objects in a standardized way.

---

## **Features**

- **OpenAPI 3.0 Compliant**: Fully compliant with the DRS OpenAPI 3.0 specification.
- **Authentication**: Supports BasicAuth and BearerAuth for secure access.
- **Endpoints**:
  - `/service-info`: Retrieve information about the DRS service.
  - `/objects/{object_id}`: Get metadata and access methods for a DRS object.
  - `/objects/{object_id}/access/{access_id}`: Get a URL for fetching object bytes.
- **Unit Tests**: Includes unit tests for all endpoints and dependencies.
- **Scalable**: Designed for deployment on cloud platforms like AWS or Azure.

---

## **Technologies Used**

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Pydantic**: For data validation and settings management using Python type annotations.
- **Pytest**: For writing and running unit tests.
- **GitHub Actions**: For continuous integration (CI) and automated testing.

---

## **Getting Started**

### **Prerequisites**

- Python 3.7+
- Pip (Python package manager)

---

## **Installation**

### **Using `setup.py`**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/drs-fastapi.git
   cd drs-fastapi
   ```
2. **Install the package**:
   ```bash
   python setup.py install
   ```
3. **Run the application**:
   ```
   drs-api
   ```

### **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/drs-fastapi.git
   cd drs-fastapi
   ```
2. **Setting up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
### **Running the Application**

1. **Start the FastAPI Server**:
   ```
   uvicorn app.main:app --reload
   ```
2. **Access the API**:
   * Open your browser and go to http://127.0.0.1:8000.
   * Interactive API documentation (Swagger UI) is available at http://127.0.0.1:8000/docs.
  
### **Running Tests**

1. **Run unit tests**:
   ```bash
   pytest tests/
   ```
2. **View test coverage**:
   ```bash
   pytest --cov=app tests/
   ```

## **Running with Docker**

### **Build the Docker Image**
```bash
docker build -t drs-fastapi .
```
