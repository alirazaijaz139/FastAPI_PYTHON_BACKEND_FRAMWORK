# FASTAPI
---

> **Definition:** **FastAPI** is a Python framework used to build APIs quickly and easily. It automatically checks data types, handles errors, and creates API documentation — all by itself.

---

## What Problem Exist Before FastAPI?

Imagine you are building a backend for:
- i) A website
- ii) A mobile app
- iii) An AI system

They all need to talk to a server.

### Old Problem:
- i) Nothing — APIs was slow.
- ii) Validation had not to be written manually.
- iii) Fancy name, at run time.
- iv) Performance was not great.

**FastAPI** is a modern Python Framework used to build APIs easily and very fast.

### 2) Why We Need FastAPI:

Backend development felt heavy and messy.

#### i) Manual Validation:
**Before:** Manual validation written by developer for every field.

#### With FastAPI:
If type(age) is **int**, sending "hello" raises automatic validation error. Clean code and easy.

#### ii) No API Documentation:
- Use Postman separately
- Write others separately

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> INFO: Uvicorn running on http://127.0.0.1:8000
> -> Visit http://127.0.0.1:8000/docs  (Swagger UI auto-generated!)
> ```

#### Extra Code Example:

```python
# FastAPI auto-validates data types
from fastapi import FastAPI
app = FastAPI()

@app.get("/age/{age}")
def check_age(age: int):
    return {"your_age": age}
```

> **Run:** `uvicorn main:app --reload` then visit `/age/25`

> **Output:**
> ```
> {"your_age": 25}
> # If you send /age/hello  ->  422 Unprocessable Entity (auto error!)
> ```

---

## With FastAPI:
- There's auto documentation
- Fill error to avoid read
- Handles everything

### iii) Slow Performance:
- Handles many requests efficiently
- Use in old systems

## Why FastAPI is Better than Competitors?

| Feature | Flask | Django | FastAPI |
|---------|-------|--------|---------|
| Speed | Medium | Slow | **Fast** |
| Validation | Manual | Manual | **Automatic** |
| Docs | Manual | Manual | **Auto (Swagger)** |
| Modern APIs | No | No | **Yes** |

## How FastAPI Works Internally:
- FastAPI sends request, reads URL, checks parameters
- Validates data, function runs, converts output to JSON
- Sends response — all automatically!

```python
from fastapi import FastAPI
app = FastAPI()
# Internally FastAPI:
# 1. Receives request
# 2. Reads URL & matches route
# 3. Checks parameters
# 4. Validates data (Pydantic)
# 5. Runs your function
# 6. Converts output to JSON
# 7. Sends response
```

> **Run:** `uvicorn main:app --reload`

> **Output:** FastAPI handles all 7 steps automatically!

#### Extra Code Example:

```python
# Seeing FastAPI speed with async
from fastapi import FastAPI
import asyncio
app = FastAPI()

@app.get("/fast")
async def fast_response():
    await asyncio.sleep(0)  # non-blocking
    return {"speed": "blazing fast!"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /fast  ->  {"speed": "blazing fast!"}`

---

## Move to Code — Simple Example (Hello World)

```python
# main.py
from fastapi import FastAPI
app = FastAPI()          # create application

@app.get("/")
def home():
    return {"message": "hello"}   # Data in dict
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> {"message": "hello"}
> -> Visit http://127.0.0.1:8000/docs for Swagger UI
> ```

#### Extra Code Example:

```python
# Multiple routes example
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"page": "home"}

@app.get("/about")
def about():
    return {"page": "about", "author": "FastAPI Dev"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /      ->  {"page": "home"}
> GET /about ->  {"page": "about", "author": "FastAPI Dev"}
> ```

## Swagger UI:
- Open browser — visit /docs
- i) Test APIs with URL
- ii) Send data, see response in browser

---

## FastAPI: HTTP Methods

### i) GET:

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/rest")
def get_user(user_id: int):
    return {"user_id": user_id}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /rest?user_id=1  ->  {"user_id": 1}`

#### Extra Code Example:

```python
# GET with list of items
from fastapi import FastAPI
app = FastAPI()

items = ["apple", "banana", "cherry"]

@app.get("/items")
def get_items():
    return {"items": items}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /items  ->  {"items": ["apple", "banana", "cherry"]}`

### ii) POST:

```python
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/create")
def create(name: str, age: int):
    return {"created": name, "age": age}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `POST /create  ->  {"created": "Ali", "age": 25}`

#### Extra Code Example:

```python
# POST with Pydantic model
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /items  body: {"name":"Book","price":9.99}
> ->  {"item_name": "Book", "price": 9.99}
> ```

---

### iii) PUT — Replace All:

Get=read, Post=create, Put=replace all, Patch=update certain, Delete=remove

```python
@app.put("/replace/{user_id}")
def replace(user_id: int, name: str, age: int):
    return {"replaced": user_id, "name": name, "age": age}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `PUT /replace/1  ->  {"replaced": 1, "name": "Ali", "age": 25}`

#### Extra Code Example:

```python
# PUT to update full user record
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"id": user_id, "updated": user}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `PUT /users/5  ->  {"id":5,"updated":{"name":"Ali","email":"ali@mail.com"}}`

### iv) PATCH:

```python
@app.patch("/users/{user_id}")
def patch_user(user_id: int, name: str = None):
    return {"patched_id": user_id, "name": name}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `PATCH /users/3?name=Ahmed  ->  {"patched_id": 3, "name": "Ahmed"}`

#### Extra Code Example:

```python
# PATCH only specific field
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class PartialUser(BaseModel):
    name: Optional[str] = None
    age:  Optional[int] = None

@app.patch("/update/{uid}")
def partial_update(uid: int, data: PartialUser):
    return {"id": uid, "changes": data}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> PATCH /update/2  body: {"age": 30}
> ->  {"id": 2, "changes": {"name": null, "age": 30}}
> ```

### v) DELETE:

```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"deleted": user_id}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `DELETE /users/1  ->  {"deleted": 1}`

#### Extra Code Example:

```python
# DELETE with confirmation message
from fastapi import FastAPI
app = FastAPI()

users = {1: "Ali", 2: "Sara", 3: "Ahmed"}

@app.delete("/users/{uid}")
def remove_user(uid: int):
    if uid in users:
        removed = users.pop(uid)
        return {"message": f"{removed} deleted"}
    return {"error": "User not found"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> DELETE /users/1  ->  {"message": "Ali deleted"}
> DELETE /users/9  ->  {"error": "User not found"}
> ```

---

## Parameters:

Used to identify a specific resource. Path — used to specifically identify a resource.

```python
@app.get("/users/{id}")
def get_user(id: int):
    return {"user_id": id}
# i)  id — value comes from URL
# ii) int — check type from URL
# iii) function runs if data valid
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /users/5    ->  {"user_id": 5}
> GET /users/abc  ->  422 Unprocessable Entity
> ```

#### Extra Code Example:

```python
# Multiple path parameters
from fastapi import FastAPI
app = FastAPI()

@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /users/1/posts/3  ->  {"user_id": 1, "post_id": 3}`

---

## Query Parameters:

Query parameter use & filtering at searching.

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/user-search")
def search(search: str = None, item: str = None):
    return {"search": search, "item": item}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /user-search?search=Ali  ->  {"search": "Ali", "item": null}`

#### Extra Code Example:

```python
# Query param with limit & skip (pagination)
from fastapi import FastAPI
app = FastAPI()

items = ["a","b","c","d","e","f","g","h","i","j"]

@app.get("/items")
def get_items(skip: int = 0, limit: int = 3):
    return {"items": items[skip : skip + limit]}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /items?skip=0&limit=3  ->  {"items": ["a", "b", "c"]}
> GET /items?skip=3&limit=3  ->  {"items": ["d", "e", "f"]}
> ```

### Optional Query Parameter by nature:

```python
@app.get("/user")
def get_user(category: str = None):
    if category:
        return {"category": category, "items": f"items of {category}"}
    return {"category": "none", "all items": "showing all"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /user              ->  {"category":"none","all items":"showing all"}
> GET /user?category=bag ->  {"category":"bag","items":"items of bag"}
> ```

#### Extra Code Example:

```python
# Optional query param with default value
from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/search")
def search(q: Optional[str] = None, page: int = 1):
    return {"query": q, "page": page}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /search           ->  {"query": null, "page": 1}
> GET /search?q=python  ->  {"query": "python", "page": 1}
> ```

---

## Body Parameter:

Optional mean: may or may not send it. Default = None. Body Parameter — used when client sends structured data (JSON).

```python
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {"created": user.name, "age": user.age}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /users  body: {"name": "Ali", "age": 22}
> ->  {"created": "Ali", "age": 22}
> ```

#### Extra Code Example:

```python
# Body with multiple fields validation
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/products")
def add_product(product: Product):
    return {"product": product.name, "price": product.price,
            "available": product.in_stock}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /products  body: {"name":"Pen","price":1.5,"in_stock":true}
> ->  {"product": "Pen", "price": 1.5, "available": true}
> ```

---

## Pydantic Model:

Real Life: sign up form, payment info

```python
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: User):
    return {"registered": user.username}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /register  body: {"username":"Ali","password":"1234"}
> ->  {"registered": "Ali"}
> ```

#### Extra Code Example:

```python
# Pydantic with nested model
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Address(BaseModel):
    city: str
    country: str

class UserFull(BaseModel):
    name: str
    address: Address

@app.post("/signup")
def signup(user: UserFull):
    return {"welcome": user.name, "city": user.address.city}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /signup body: {"name":"Ali","address":{"city":"Lahore","country":"PK"}}
> ->  {"welcome": "Ali", "city": "Lahore"}
> ```

## Real Life Examples:
- Path: Search user by ID
- Query: Search, Predict?
- Body: Register user

---

## Advance Topics:

### i) Pydantic Validation:

Pydantic Validation is data validation — uses type hints in the request body. Every time FastAPI uses it, it auto validates.

```python
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /items  body: {"name":"Book","price":9.99}  ->  {"name":"Book","price":9.99}
> # If price is "abc"  ->  422 Validation Error auto!
> ```

#### Extra Code Example:

```python
# Pydantic auto validation check
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Score(BaseModel):
    student: str
    marks: int

@app.post("/score")
def add_score(score: Score):
    grade = "A" if score.marks >= 80 else "B"
    return {"student": score.student, "grade": grade}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /score  body: {"student":"Ali","marks":85}  ->  {"student":"Ali","grade":"A"}
> POST /score  body: {"student":"Ali","marks":"x"}  ->  422 Validation Error
> ```

---

## Validate Incoming Data:

- Validate incoming data against the model
- Convert type (if needed)
- Check if type(s) is int — if validation fails, return error

### Basic Model (Data Shape):

class User(BaseModel) — BaseModel acts as a class that describes the structure of your data.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

u = User(name="Ali", age=25)
print(u)
```

> **Run:** `python main.py`

> **Output:**
> ```
> name="Ali" age=25
> # User(name="Ali", age="hello")  ->  ValidationError
> ```

#### Extra Code Example:

```python
# BaseModel with default values
from pydantic import BaseModel
from typing import Optional

class Profile(BaseModel):
    username: str
    bio: Optional[str] = "No bio yet"
    followers: int = 0

p = Profile(username="ali")
print(p)
```

> **Run:** `python main.py`

> **Output:** `username="ali" bio="No bio yet" followers=0`

### Field() — Constants and Metadata:

Field() is used to add validation rules and metadata (description, min/max length, etc.)

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(min_length=5)
    name:  str = Field(min_length=2, max_length=50)
    age:   int = Field(ge=1, le=120)
```

> **Run:** `python main.py`

> **Output:**
> ```
> User(email="a@b.c", name="Ali", age=25)  ->  valid
> User(email="a", ...)  ->  ValidationError: min_length
> ```

#### Extra Code Example:

```python
# Field with description for Swagger docs
from pydantic import BaseModel, Field

class Product(BaseModel):
    name:  str   = Field(..., description="Product name", min_length=2)
    price: float = Field(..., description="Price in USD", gt=0)
    qty:   int   = Field(default=1, description="Quantity", ge=1)

p = Product(name="Book", price=9.99)
print(p)
```

> **Run:** `python main.py`

> **Output:** `name="Book" price=9.99 qty=1`

---

## Metadata (Extra Information):

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name:        str   = Field(min_length=2, description="product name")
    description: str   = Field(description="description", example="nice")
    price:       float = Field(description="price", example=9.99)
```

> **Run:** `python main.py`

> **Output:** -> Swagger UI shows these descriptions automatically at /docs

#### Extra Code Example:

```python
# metadata with alias
from pydantic import BaseModel, Field

class Item(BaseModel):
    item_name: str   = Field(alias="name", min_length=1)
    item_cost: float = Field(alias="cost", gt=0)

i = Item(**{"name": "Pen", "cost": 1.5})
print(i)
```

> **Run:** `python main.py`

> **Output:** `item_name="Pen" item_cost=1.5`

---

## EmailStr:

```python
from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    name:  str
    email: EmailStr

u = UserModel(name="Ali", email="ali@example.com")
print(u)
```

> **Run:** `pip install "pydantic[email]"` then `python main.py`

> **Output:**
> ```
> name="Ali" email="ali@example.com"
> # ali@.com  ->  raises ValidationError
> ```

#### Extra Code Example:

```python
# EmailStr in FastAPI registration
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
app = FastAPI()

class Register(BaseModel):
    username: str
    email:    EmailStr

@app.post("/register")
def register(data: Register):
    return {"user": data.username, "email": data.email}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /register  body: {"username":"Ali","email":"ali@mail.com"}
> ->  {"user": "Ali", "email": "ali@mail.com"}
> ```

---

## Optional Field in Pydantic:

```python
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name:  Optional[str] = None
    email: Optional[str] = None
```

> **Run:** `python main.py`

> **Output:**
> ```
> Product()              ->  name=None email=None  (no error)
> Product(name="Book")   ->  name="Book" email=None
> ```

#### Extra Code Example:

```python
# Optional with default value
from pydantic import BaseModel
from typing import Optional

class Config(BaseModel):
    theme:    Optional[str]  = "light"
    language: Optional[str]  = "en"
    debug:    Optional[bool] = False

c = Config()
print(c)
c2 = Config(theme="dark")
print(c2)
```

> **Run:** `python main.py`

> **Output:**
> ```
> theme="light" language="en" debug=False
> theme="dark"  language="en" debug=False
> ```

### Optional Parameters:
- Without optional: must provide a value, otherwise give error
- With optional: default value assigned None, not required

---

## i) Optional with Path, Body, Parameters:

```python
from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/products")
def get_products(category: Optional[str] = None, limit: int = 10):
    return {"category": category, "limit": limit}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /products               ->  {"category": null, "limit": 10}
> GET /products?category=bags ->  {"category": "bags", "limit": 10}
> ```

#### Extra Code Example:

```python
# Optional path + body together (PATCH)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Update(BaseModel):
    name:  Optional[str] = None
    email: Optional[str] = None

@app.patch("/users/{uid}")
def update(uid: int, data: Update):
    return {"id": uid, "updates": data}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> PATCH /users/1  body: {"name":"Ali"}
> ->  {"id":1,"updates":{"name":"Ali","email":null}}
> ```

### ii) Optional with Header:

```python
from fastapi import FastAPI, Header
from typing import Optional
app = FastAPI()

@app.get("/discover")
def discover(api_key: Optional[str] = Header(None)):
    if api_key is None:
        return {"detail": "No key"}
    return {"received_api_key": api_key}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /discover  (no header)     ->  {"detail": "No key"}
> GET /discover  api-key: abc123 ->  {"received_api_key": "abc123"}
> ```

#### Extra Code Example:

```python
# Required header example
from fastapi import FastAPI, Header, HTTPException
app = FastAPI()

@app.get("/secure")
def secure_route(x_token: str = Header(...)):
    if x_token != "secret123":
        raise HTTPException(status_code=403, detail="Invalid token")
    return {"status": "Authorized"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /secure  x-token: secret123  ->  {"status": "Authorized"}
> GET /secure  x-token: wrong      ->  403 Invalid token
> ```

---

## Status Code:

- 200 — success
- 201 — created
- 400 — client error
- 404 — not found
- 500 — server error

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/", status_code=200)
def home():
    return {"message": "ok"}

@app.post("/create", status_code=201)
def create():
    return {"message": "created"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /        ->  200 OK       {"message": "ok"}
> POST /create ->  201 Created  {"message": "created"}
> ```

#### Extra Code Example:

```python
# Using status module constants
from fastapi import FastAPI, status
app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
def health():
    return {"status": "healthy"}

@app.post("/data", status_code=status.HTTP_201_CREATED)
def add_data():
    return {"result": "data added"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /health  ->  200  {"status": "healthy"}
> POST /data   ->  201  {"result": "data added"}
> ```

---

## Common Status Codes — Returning Custom Status Code:

```python
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "ok"}

@app.post("/users")
def create_user():
    current = {"name": "Ali"}
    return JSONResponse(content=current, status_code=201)
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /       ->  200  {"message": "ok"}
> POST /users ->  201  {"name": "Ali"}
> ```

#### Extra Code Example:

```python
# Return different status codes based on logic
from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()

users = {"ali": "pass123"}

@app.post("/login")
def login(username: str, password: str):
    if username in users and users[username] == password:
        return JSONResponse({"status": "logged in"}, status_code=200)
    return JSONResponse({"error": "Invalid"}, status_code=401)
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /login?username=ali&password=pass123  ->  200 {"status": "logged in"}
> POST /login?username=ali&password=wrong    ->  401 {"error": "Invalid"}
> ```

---

### model.dump() — convert Pydantic into Python dictionary:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Ali", age=25)
print(user.model_dump())
```

> **Run:** `python main.py`

> **Output:** `{'name': 'Ali', 'age': 25}`

#### Extra Code Example:

```python
# model.dump() with exclude fields (hide password)
from pydantic import BaseModel

class User(BaseModel):
    name:     str
    age:      int
    password: str

user = User(name="Ali", age=25, password="secret")
safe_data = user.model_dump(exclude={"password"})
print(safe_data)
```

> **Run:** `python main.py`

> **Output:** `{'name': 'Ali', 'age': 25}  # password excluded safely!`

---

## Exception Handling:

FastAPI is the standard way to return a non-200 response in JSON body.

```python
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):
    user = None
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /users/99  ->  404  {"detail": "User not found"}
> GET /users/1   ->  200  (if user exists)
> ```

#### Extra Code Example:

```python
# Multiple exception types
from fastapi import FastAPI, HTTPException
app = FastAPI()

products = {1: "Laptop", 2: "Phone"}

@app.get("/products/{pid}")
def get_product(pid: int):
    if pid <= 0:
        raise HTTPException(status_code=400, detail="ID must be positive")
    if pid not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": products[pid]}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /products/0  ->  400 "ID must be positive"
> GET /products/9  ->  404 "Product not found"
> GET /products/1  ->  200 {"product": "Laptop"}
> ```

---

### Global Exception Handler:

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
app = FastAPI()

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )
```

> **Run:** `uvicorn main:app --reload`

> **Output:** Any HTTPException  ->  handled globally with custom format

#### Extra Code Example:

```python
# Global 404 custom handler
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return JSONResponse(
        {"error": "Page not found", "path": str(request.url)},
        status_code=404
    )
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /nonexistent  ->  404 {"error":"Page not found","path":"http://..."}`

---

#### Login Example:

```python
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "1234":
        return {"status": "login successful"}
    raise HTTPException(status_code=403, detail="Invalid credentials")
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /login?username=admin&password=1234  ->  200 {"status":"login successful"}
> POST /login?username=admin&password=bad   ->  403 {"detail":"Invalid credentials"}
> ```

#### Extra Code Example:

```python
# Login with token response
from fastapi import FastAPI, HTTPException
app = FastAPI()

USERS = {"ali": "pass123", "sara": "mypass"}

@app.post("/login")
def login(username: str, password: str):
    if USERS.get(username) == password:
        return {"token": f"token-{username}", "type": "bearer"}
    raise HTTPException(403, "Wrong credentials")
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST username=ali&password=pass123  ->  {"token":"token-ali","type":"bearer"}
> POST username=ali&password=wrong    ->  403 {"detail":"Wrong credentials"}
> ```

---

## Full Example — Validation, Optional, Status Code, Exception:

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
app = FastAPI()

class User(BaseModel):
    name:  str = Field(min_length=2)
    age:   int = Field(ge=1, le=120)
    email: Optional[str] = None

@app.post("/users", status_code=201)
def create_user(user: User):
    if user.age < 18:
        raise HTTPException(400, "Must be 18+")
    return {"created": user.name}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> POST /users  {"name":"Ali","age":25}  ->  201 {"created":"Ali"}
> POST /users  {"name":"Ali","age":10}  ->  400 "Must be 18+"
> ```

#### Extra Code Example:

```python
# Full example with GET + validation
from fastapi import FastAPI, HTTPException
from typing import Optional
app = FastAPI()

db = {1: "Ali", 2: "Sara", 3: "Ahmed"}

@app.get("/users/{uid}")
def get_user(uid: int, show_upper: Optional[bool] = False):
    if uid not in db:
        raise HTTPException(404, "Not found")
    name = db[uid]
    return {"name": name.upper() if show_upper else name}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /users/1                 ->  {"name": "Ali"}
> GET /users/1?show_upper=true ->  {"name": "ALI"}
> GET /users/99                ->  404 "Not found"
> ```

---

## Dependency Injection (DI):

> **Definition of DI:** Dependency Injection is a design pattern where FastAPI automatically provides required resources (like database connections, authentication checks) to your route functions — so you don't have to create them manually every time inside each function.

### Problem without DI:
- Duplicate code everywhere
- Write same logic inside every function
- Hard to test and maintain

```python
# WITHOUT DI — duplicate DB code (BAD)
import sqlite3

def get_user():
    conn   = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    conn.close()
    return result

def get_product():
    conn   = sqlite3.connect("database.db")  # repeated!
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    conn.close()
    return result
```

> **Run:** `python main.py`

> **Output:** Both functions connect to DB separately — code duplication problem!

#### Extra Code Example:

```python
# Duplication problem clearly shown
def check_auth_route1():
    token = "abc"  # duplicated in every route
    if token != "secret": return "Denied"
    return "Route 1 data"

def check_auth_route2():
    token = "abc"  # same code again!
    if token != "secret": return "Denied"
    return "Route 2 data"

# With DI: write auth logic ONCE, inject everywhere!
```

> **Run:** `python main.py`

> **Output:** This shows WHY DI is needed — eliminate code repetition

---

## i) Authentication Logic Repeated Without DI:

```python
from fastapi import FastAPI, HTTPException
app = FastAPI()

def get_public_token():
    return "public-token"

def get_private_token():
    token = "secret-token"
    if token != "secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token
```

> **Run:** `python main.py`

> **Output:** Each function handles auth separately -> duplicate logic!

#### Extra Code Example:

```python
# Auth duplication across routes (problem)
from fastapi import FastAPI, HTTPException, Header
from typing import Optional
app = FastAPI()

@app.get("/page1")
def page1(x_token: Optional[str] = Header(None)):
    if x_token != "mytoken":
        raise HTTPException(401, "Unauthorized")
    return {"page": 1}

@app.get("/page2")
def page2(x_token: Optional[str] = Header(None)):
    if x_token != "mytoken":  # same check again!
        raise HTTPException(401, "Unauthorized")
    return {"page": 2}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** Both routes repeat same auth check — DI solves this!

---

### iii) Global Variables — Silent Bugs?

Using global variables inside routes creates silent bugs — state is shared across all requests.

```python
from fastapi import FastAPI
app = FastAPI()

# SILENT BUG — global variable shared across all users!
request_count = 0

@app.get("/count")
def get_count():
    global request_count
    request_count += 1          # all users share this!
    return {"count": request_count}

# User A visits -> count = 1
# User B visits -> count = 2  (sees User A's data!)
# This causes WRONG results for every user!
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> User A: GET /count  ->  {"count": 1}
> User B: GET /count  ->  {"count": 2}  <- WRONG! B sees A's state
> User C: GET /count  ->  {"count": 3}  <- WRONG! shared global bug!
> ```

#### Extra: Fix with DI — No Global Variable

```python
from fastapi import FastAPI, Depends
app = FastAPI()

# FIXED — each request gets its own fresh state via DI
def get_session():
    session = {"user_data": None, "request_id": id(object())}
    return session

@app.get("/data")
def get_data(session = Depends(get_session)):
    # Each request gets a NEW session — no sharing!
    return {"session_id": session["request_id"],
            "message": "fresh session, no bug!"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> User A: GET /data  ->  {"session_id": 1234, "message": "fresh session, no bug!"}
> User B: GET /data  ->  {"session_id": 5678, "message": "fresh session, no bug!"}
> Each user gets THEIR OWN fresh session — bug fixed with DI!
> ```

### iv) History?

DI pattern comes from software engineering to make code clean, reusable, and testable.

#### v) Definition One-line:

> "DI = Let FastAPI call a function for you before your route runs, and inject its result."

> **Another Definition of DI:**
>
> **Dependency Injection** is like a **waiter in a restaurant**. You (the route function) don't go to the kitchen yourself to get ingredients (DB, auth, config). Instead, the waiter (FastAPI) brings everything you need automatically before you start working.
>
> In technical terms: *"DI is a technique where an object or function receives the things it depends on (its dependencies) from an external source rather than creating them itself."*
>
> **Result:** Less code duplication, easier testing, cleaner architecture.

---

## How DI Works:

FastAPI uses the Dependency function. You write a dependency function and FastAPI calls it for you before your route, then injects the result.

```python
import sqlite3
from fastapi import FastAPI, Depends
app = FastAPI()

def get_db():
    conn = sqlite3.connect("database.db")
    try:
        yield conn
    finally:
        conn.close()   # auto cleanup!

@app.get("/users")
def get_users(db = Depends(get_db)):
    cursor = db.execute("SELECT * FROM users")
    return cursor.fetchall()
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /users  ->  returns all users from DB
> DB connection created and closed automatically!
> ```

#### Extra Code Example:

```python
# DI with authentication dependency (written ONCE)
from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional
app = FastAPI()

def verify_token(x_token: Optional[str] = Header(None)):
    if x_token != "secret123":
        raise HTTPException(401, "Invalid token")
    return x_token

@app.get("/data")
def get_data(token = Depends(verify_token)):
    return {"data": "secret data", "token": token}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /data  x-token: secret123  ->  {"data":"secret data","token":"secret123"}
> GET /data  x-token: wrong      ->  401 Invalid token
> ```

---

## with DI — Profile Example:

```python
from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional
app = FastAPI()

def verify_token(x_token: Optional[str] = Header(None)):
    if x_token is None:
        raise HTTPException(status_code=403, detail="Not Found")
    return x_token

@app.get("/profile")
def get_profile(token: str = Depends(verify_token)):
    return {"profile": "Ahmed", "token": token}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /profile  x-token: abc  ->  {"profile":"Ahmed","token":"abc"}
> GET /profile  (no header)   ->  403 "Not Found"
> ```

#### Extra Code Example:

```python
# DI with query parameter dependency (reusable)
from fastapi import FastAPI, Depends
app = FastAPI()

def common_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/items")
def get_items(params: dict = Depends(common_params)):
    return {"params": params}

@app.get("/products")
def get_products(params: dict = Depends(common_params)):
    return {"params": params}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /items?skip=5&limit=3     ->  {"params":{"skip":5,"limit":3}}
> GET /products?skip=0&limit=5  ->  {"params":{"skip":0,"limit":5}}
> ```

---

## Dependencies Depend upon Other Dependencies:

> **Chained Dependencies:** Dependencies can depend on other dependencies. FastAPI resolves the entire chain automatically. This is called "nested" or "chained" dependencies — very powerful for layered auth/logic.

```python
from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional
app = FastAPI()

def get_token(x_token: Optional[str] = Header(None)):
    if not x_token:
        raise HTTPException(401, "Token missing")
    return x_token

def get_current_user(token: str = Depends(get_token)):
    return {"user": "Ali", "token": token}

@app.get("/me")
def get_me(user = Depends(get_current_user)):
    return user
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /me  x-token: abc  ->  {"user":"Ali","token":"abc"}
> GET /me  (no token)    ->  401 "Token missing"
> ```

#### Extra Code Example:

```python
# 3-level dependency chain
from fastapi import FastAPI, Depends
app = FastAPI()

def dep_a():                     return "A"
def dep_b(a = Depends(dep_a)):   return f"{a}->B"
def dep_c(b = Depends(dep_b)):   return f"{b}->C"

@app.get("/chain")
def chain(c = Depends(dep_c)):
    return {"chain": c}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /chain  ->  {"chain": "A->B->C"}`

---

## Benefits of Dependency Injection:

> **Benefits of DI:**
> 1. No code duplication — write once, use everywhere.
> 2. Clean and readable code.
> 3. Easy to test — mock/override dependencies in testing.
> 4. Auto lifecycle management — e.g. DB connection auto-closed with yield.
> 5. Scalable — add new dependencies without changing route functions.

```python
# DI benefit: write auth ONCE, use in many routes
from fastapi import FastAPI, Depends, HTTPException, Header
from typing import Optional
app = FastAPI()

def auth(x_token: Optional[str] = Header(None)):
    if x_token != "valid":
        raise HTTPException(401, "Denied")
    return x_token

@app.get("/a", dependencies=[Depends(auth)])
def route_a(): return {"route": "A"}

@app.get("/b", dependencies=[Depends(auth)])
def route_b(): return {"route": "B"}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /a  x-token: valid  ->  {"route":"A"}
> GET /b  x-token: valid  ->  {"route":"B"}
> GET /a  (no token)      ->  401 Denied
> ```

#### Extra Code Example:

```python
# DI benefit: easy mocking in tests
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
app = FastAPI()

def get_db():
    return {"db": "real_database"}

@app.get("/data")
def get_data(db = Depends(get_db)):
    return db

# Override with fake DB in tests
def fake_db():
    return {"db": "test_database"}

app.dependency_overrides[get_db] = fake_db
client = TestClient(app)
print(client.get("/data").json())
```

> **Run:** `python main.py`

> **Output:** `{"db": "test_database"}  # Using fake DB in tests!`

---

## Class Based DI:

> **Class Based DI:** When a dependency has parameters (like search, filters, pagination), you can wrap it in a class. FastAPI will instantiate the class automatically and inject it using Depends().

```python
from fastapi import FastAPI, Depends
app = FastAPI()

class QueryMaker:
    def __init__(self, search: str = ""):
        self.search = search

@app.get("/search")
def search_item(Filters: QueryMaker = Depends()):
    return {"search": Filters.search}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /search             ->  {"search": ""}
> GET /search?search=Ali  ->  {"search": "Ali"}
> ```

#### Extra Code Example:

```python
# Class Based DI with multiple params (pagination)
from fastapi import FastAPI, Depends
app = FastAPI()

class PaginationParams:
    def __init__(self, page: int = 1, size: int = 10, sort: str = "asc"):
        self.page = page
        self.size = size
        self.sort = sort

@app.get("/products")
def list_products(params: PaginationParams = Depends()):
    return {"page": params.page, "size": params.size, "sort": params.sort}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /products                          ->  {"page":1,"size":10,"sort":"asc"}
> GET /products?page=2&size=5&sort=desc  ->  {"page":2,"size":5,"sort":"desc"}
> ```

---

## Query Parameter with DI:

> **Query Parameter with DI:** You can pass query parameters through a dependency function. This keeps route functions clean and reuses the same query logic across multiple endpoints without repeating code.

```python
from fastapi import FastAPI, Depends
from typing import Optional
app = FastAPI()

def search_filter(q: Optional[str] = None, limit: int = 5):
    return {"q": q, "limit": limit}

@app.get("/books")
def get_books(filters = Depends(search_filter)):
    return {"books_filter": filters}
```

> **Run:** `uvicorn main:app --reload`

> **Output:** `GET /books?q=python&limit=3  ->  {"books_filter":{"q":"python","limit":3}}`

#### Extra Code Example:

```python
# Reuse same query filter across multiple routes
from fastapi import FastAPI, Depends
from typing import Optional
app = FastAPI()

def common_filter(search: Optional[str] = None, page: int = 1):
    return {"search": search, "page": page}

@app.get("/users")
def get_users(f = Depends(common_filter)):
    return {"users_filter": f}

@app.get("/orders")
def get_orders(f = Depends(common_filter)):
    return {"orders_filter": f}
```

> **Run:** `uvicorn main:app --reload`

> **Output:**
> ```
> GET /users?search=Ali   ->  {"users_filter":{"search":"Ali","page":1}}
> GET /orders?page=2      ->  {"orders_filter":{"search":null,"page":2}}
> ```
