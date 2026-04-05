# Ecommerce API – Task 6: Filtering, Searching, and Ordering

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Task 6 Features

### Search
Search products by `name` or `description`:
```
GET /api/products/?search=phone
```

### Ordering
Sort by `price` or `name`:
```
GET /api/products/?ordering=price       # ascending
GET /api/products/?ordering=-price      # descending
GET /api/products/?ordering=name
```

### Combined Example
```
GET /api/products/?search=phone&ordering=-price
```

## Postman Collection
Import `Ecommerce_API_Task6.postman_collection.json` into Postman.

Total requests: **13**
- **Products** folder: 11 requests (CRUD + pagination)
- **Search & Filters** folder: 2 requests
  - Search Products: `GET /api/products/?search=phone`
  - Sort Products by Price: `GET /api/products/?ordering=-price`

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create product |
| GET | `/api/products/{id}/` | Get product |
| PUT | `/api/products/{id}/` | Full update |
| PATCH | `/api/products/{id}/` | Partial update |
| DELETE | `/api/products/{id}/` | Delete product |
| GET | `/api/products/?search=<kw>` | Search by name/description |
| GET | `/api/products/?ordering=<field>` | Sort by field |
