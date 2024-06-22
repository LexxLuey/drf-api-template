## API Documentation

### Overview

This API allows you to manage the inventory and suppliers of an online store. You can perform CRUD operations on inventory items and suppliers, as well as view relationships between them.

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/LexxLuey/drf-api-template.git
   cd drf-api-template
   ```

2. **Create and Activate Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.dev.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

### Endpoints

Please visit the [swagger docs](http://127.0.0.1:8000/api/schema/docs/) for a more detailed documentation of all endpoints.

#### Inventory Management

- **List Items**

  - **URL**: `/api/inventory/`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all inventory items.
  - **Response**: JSON array of items

- **Create Item**

  - **URL**: `/api/inventory/`
  - **Method**: `POST`
  - **Description**: Creates a new inventory item.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "description": "string",
      "price": "float",
      "date_added": "YYYY-MM-DD",
      "suppliers": [{ "name": "string", "contact_info": "string" }],
      "suppliers_id": [1, 2]
    }
    ```
  - **Response**: JSON object of the created item

- **Retrieve Item**

  - **URL**: `/api/inventory/{id}/`
  - **Method**: `GET`
  - **Description**: Retrieves details of a specific inventory item.
  - **Response**: JSON object of the item

- **Update Item**

  - **URL**: `/api/inventory/{id}/`
  - **Method**: `PUT`
  - **Description**: Updates an inventory item.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "description": "string",
      "price": "float",
      "date_added": "YYYY-MM-DD",
      "suppliers": [{ "name": "string", "contact_info": "string" }],
      "suppliers_id": [1, 2]
    }
    ```
  - **Response**: JSON object of the updated item

- **Delete Item**

  - **URL**: `/api/inventory/{id}/`
  - **Method**: `DELETE`
  - **Description**: Deletes an inventory item.
  - **Response**: `204 No Content`

- **Item Suppliers**
  - **URL**: `/api/inventory/{id}/suppliers/`
  - **Method**: `GET`
  - **Description**: Retrieves suppliers for a specific inventory item.
  - **Response**: JSON array of suppliers

#### Supplier Management

- **List Suppliers**

  - **URL**: `/api/suppliers/`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all suppliers.
  - **Response**: JSON array of suppliers

- **Create Supplier**

  - **URL**: `/api/suppliers/`
  - **Method**: `POST`
  - **Description**: Creates a new supplier.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "contact_info": "string"
    }
    ```
  - **Response**: JSON object of the created supplier

- **Retrieve Supplier**

  - **URL**: `/api/suppliers/{id}/`
  - **Method**: `GET`
  - **Description**: Retrieves details of a specific supplier.
  - **Response**: JSON object of the supplier

- **Update Supplier**

  - **URL**: `/api/suppliers/{id}/`
  - **Method**: `PUT`
  - **Description**: Updates a supplier.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "contact_info": "string"
    }
    ```
  - **Response**: JSON object of the updated supplier

- **Delete Supplier**

  - **URL**: `/api/suppliers/{id}/`
  - **Method**: `DELETE`
  - **Description**: Deletes a supplier.
  - **Response**: `204 No Content`

- **Supplier Items**
  - **URL**: `/api/suppliers/{id}/items/`
  - **Method**: `GET`
  - **Description**: Retrieves items supplied by a specific supplier.
  - **Response**: JSON array of items

### Management Commands

#### Create Suppliers

To create multiple suppliers, use the management command:

```bash
python manage.py create_suppliers <num_suppliers>
```

Example:

```bash
python manage.py create_suppliers 20
```

#### Create Items

To create multiple items and randomly attach them to suppliers, use the management command:

```bash
python manage.py create_items <num_items>
```

Example:

```bash
python manage.py create_items 50
```

### Running Tests

To run the tests, use the following commands:

```bash
python manage.py test
```

### Conclusion

This documentation provides the basic setup and usage instructions for the API. For further details and advanced usage, please refer to the source code, comments within the codebase and the [swagger docs](http://127.0.0.1:8000/api/schema/docs/).
