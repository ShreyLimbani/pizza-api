# PIZZA-API

This is django rest framework based api which is used to store information about different types of Pizzas and interacting with those informations.

# Steps to run the project
1. Clone this repository into a folder on your computer
2. Download Python
3. Open terminal inside the folder with code.
4. Type `pip install -r requirements.txt` in the terminal window to install all the requirements to run the app.
5. Install MongoDB in your system. Connect it to the local database. Create a new database named `test`.
5. Type `py manage.py runserver` to start a localhost server for the app.
6. Open any web browser and go to this address - `http://127.0.0.1:8000/`. This will start the webapp.

# API Documentation

## Table of Contents
- [Pizza List GET API](#pizza-list-get-api)
- [Pizza List POST API](#pizza-list-post-api)
- [Pizza Details GET API](#pizza-details-get-api)
- [Pizza Details PUT API](#pizza-details-put-api)
- [Pizza Details DELETE API](#pizza-details-delete-api)
- [Size List GET API](#size-list-get-api)
- [Size List POST API](#size-list-post-api)
- [Size Details GET API](#size-details-get-api)
- [Size Details PUT API](#size-details-put-api)
- [Size Details DELETE API](#size-details-delete-api)
- [Shape List GET API](#shape-list-get-api)
- [Shape Details GET API](#shape-details-get-api)
- [Shape Details PUT API](#shape-details-put-api)
- [Shape Details DELETE API](#shape-details-delete-api)
- [Toppings List GET API](#toppings-list-get-api)
- [Toppings List POST API](#toppings-list-post-api)
- [Toppings Details GET API](#toppings-details-get-api)
- [Toppings Details PUT API](#toppings-details-put-api)
- [Toppings Details DELETE API](#toppings-details-delete-api)
- [Pizza Orders List GET API](#pizza-orders-list-get-api)
- [Pizza Orders List POST API](#pizza-orders-list-post-api)
- [Pizza Orders Details GET API](#pizza-orders-details-get-api)
- [Pizza Orders Details PUT API](#pizza-orders-details-put-api)
- [Pizza Orders Details DELETE API](#pizza-orders-details-delete-api)


# Pizza List GET API
Returns list of all the available pizza types

**API URL**: `<host>/pizzas/`

**Request Method**: `GET`

**Response Header**: `JSON`
```
[
    {
        "name": "Veggie Paradise",
        "description": "The awesome foursome! Golden Corn, Black Olives, Capsicum and Red Paprika"
    },
    {
        "name": "Margherita",
        "description": "A hugely popular margherita with a deliciously tangy single cheese topping."
    }
]
``` 


# Pizza List POST API
Create a new pizza type and returns the created pizza details

**API URL**: `<host>/pizzas/`

**Request Method**: `POST`

**Request Header**: `JSON`
```
{
	"name": "Farmhouse",
	"description": "Delightful combination of onion, capsicum, tomato and grilled mushroom."
}
```

**Response Header**: `JSON`
```
{
    "name": "Farmhouse",
    "description": "Delightful combination of onion, capsicum, tomato and grilled mushroom."
}
``` 


# Pizza Details GET API
Returns details of requested pizza type

**API URL**: `<host>/pizzas/<str:name>`

**Request Method**: `GET`

**Response Header**: `JSON`
```
{
	"name": "Farmhouse",
	"description": "Delightful combination of onion, capsicum, tomato with grilled mushroom."
}
```


# Pizza Details PUT API
Modifies the details of the requested pizza type

**API URL**: `<host>/pizzas/<str:name>`

**Request Method**: `PUT`

**Request Header**: `JSON`
```
{
	"name": "Farmhouse",
	"description": "Delightful combination of onion, capsicum, tomato with grilled mushroom."
}
```

**Response Header**: `JSON`
```
{
	"name": "Farmhouse",
	"description": "Delightful combination of onion, capsicum, tomato with grilled mushroom."
}
``` 


# Pizza Details DELETE API
Deletes the requested pizza type

**API URL**: `<host>/pizzas/<str:name>`

**Request Method**: `DELETE`

**Response Header**: `TEXT`
```
Pizza Deleted
``` 

# Size List GET API
Returns list of all the available sizes of pizza

**API URL**: `<host>/sizes/`

**Request Method**: `GET`

**Response Header**: `JSON`
```
[
    {
        "name": "Small",
        "description": "8-10 Inches with 6 Slices"
    },
    {
        "name": "Medium",
        "description": "10-12 Inches with 8 Slices"
    },
    {
        "name": "Large",
        "description": "12-14 Inches with 8 slices."
    }
]
``` 


# Size List POST API
Create a new size and returns the created size details

**API URL**: `<host>/sizes/`

**Request Method**: `POST`

**Request Header**: `JSON`
```
{
    "name": "Extra Large",
    "description": "14-16 Inches with 12 Slices"
}
```

**Response Header**: `JSON`
```
{
    "name": "Extra Large",
    "description": "14-16 Inches with 12 Slices"
}
``` 

# Size Details GET API
Returns details of requested size type

**API URL**: `<host>/sizes/<str:name>`

**Request Method**: `GET`

**Response Header**: `JSON`
```
{
    "name": "Small",
    "description": "8-10 Inches with 6 Slices"
}
```


# Size Details PUT API
Modifies the details of the requested size type

**API URL**: `<host>/sizes/<str:name>/`

**Request Method**: `PUT`

**Request Header**: `JSON`
```
{
	"name": "Small",
	"description": "8-10 Inches with 8 Slices"
}
```

**Response Header**: `JSON`
```
{
	"name": "Small",
	"description": "8-10 Inches with 8 Slices"
}
``` 


# Size Details DELETE API
Deletes the requested size type

**API URL**: `<host>/sizes/<str:name>`

**Request Method**: `DELETE`

**Response Header**: `TEXT`
```
Size Deleted
``` 

# Shape List GET API
Returns list of all the available shapes

**API URL**: `<host>/shapes/`

**Request Method**: `GET`

**Response Header**: `JSON`
```
[
    {
        "name": "Regular",
        "description": "Regular circle shaped pizza."
    },
    {
        "name": "Square",
        "description": "Square shaped pizza."
    }
]
``` 


# Shape Details GET API
Returns details of requested shape

**API URL**: `<host>/shapes/<str:name>`

**Request Method**: `GET`

**Response Header**: `JSON`
```
{
    "name": "Regular",
    "description": "Regular circle shaped pizza."
}
```

# Shape Details PUT API
Modifies the details of the requested shape

**API URL**: `<host>/shapes/<str:name>`

**Request Method**: `PUT`

**Request Header**: `JSON`
```
{
	"name": "Regular",
	"description": "Circle shaped pizza."
}
```

**Response Header**: `JSON`
```
{
    "name": "Regular",
    "description": "Circle shaped pizza."
}
``` 


# Shape Details DELETE API
Deletes the requested shape

**API URL**: `<host>/shapes/<str:name>`

**Request Method**: `DELETE`

**Response Header**: `TEXT`
```
Shape Deleted
``` 

# Toppings List GET API
Returns list of all the available toppings

**API URL**: `<host>/toppings/`

**Request Method**: `GET`

**Response Header**: `JSON`
```
[
    {
        "name": "Onion",
        "description": "Few slices of onion spread across the surface"
    },
    {
        "name": "Tomato",
        "description": "Few slices of tomato spread across the surface"
    },
    {
        "name": "Corn",
        "description": "Few pieces of corn sprinkled across the surface"
    },
    {
        "name": "Capsicum",
        "description": "Few slices of capsicum spread across the surface"
    },
    {
        "name": "Cheese",
        "description": "Single layer of cheese spread over the surface"
    },
    {
        "name": "Jalapeno",
        "description": "Few pieces of jalapeno spread across the surface"
    },
    {
        "name": "Paneer",
        "description": "Few pieces of paneer spread across the surface"
    },
    {
        "name": "Mushrooms",
        "description": "Few pieces of mushroom spread across the surface"
    }
]
``` 


# Toppings List POST API
Create a new topping type and returns the created topping details

**API URL**: `<host>/toppings/`

**Request Method**: `POST`

**Request Header**: `JSON`
```
{
    "name": "Onion",
    "description": "Few slices of onion spread across the surface"
}
```

**Response Header**: `JSON`
```
{
    "name": "Onion",
    "description": "Few slices of onion spread across the surface"
}
``` 

# Toppings Details GET API
Returns details of requested topping type

**API URL**: `<host>/toppings/<str:name>`

**Request Method**: `GET`

**Response Header**: `JSON`
```
{
    "name": "Onion",
    "description": "Few slices of onion spread across the surface"
}
```

# Toppings Details PUT API
Modifies the details of the requested topping

**API URL**: `<host>/toppings/<str:name>`

**Request Method**: `PUT`

**Request Header**: `JSON`
```
{
    "name": "Onion",
    "description": "Few slices of onion spread across the surface"
}
```

**Response Header**: `JSON`
```
{
    "name": "Onion",
    "description": "Few slices of onion spread across the surface"
}
``` 


# Toppings Details DELETE API
Deletes the requested topping

**API URL**: `<host>/toppings/<str:name>`

**Request Method**: `DELETE`

**Response Header**: `TEXT`
```
Topping Deleted
``` 

# Pizza Orders List GET API
Returns list of all the orders made

**API URL**: `<host>/pizza-orders/`

**Request Method**: `GET`

**Response Header**: `JSON`
```
[
    {
        "pizza": 2,
        "shape": 1,
        "size": 3,
        "toppings": [
            3,
            5,
            7
        ]
    },
    {
        "pizza": 2,
        "shape": 2,
        "size": 1,
        "toppings": [
            2,
            5
        ]
    }
]
``` 


# Pizza Orders List POST API
Create a new order and returns the created order details

**API URL**: `<host>/orders/`

**Request Method**: `POST`

**Request Header**: `JSON`
```
{
    "pizza": 2,
    "shape": 2,
    "size": 1,
    "toppings": [
        2,
        5
    ]
}
```

**Response Header**: `JSON`
```
{
    "pizza": 2,
    "shape": 2,
    "size": 1,
    "toppings": [
        2,
        5
    ]
}
``` 

# Pizza Orders Details GET API
Returns details of requested order

**API URL**: `<host>/pizza-orders/<int:order-id>`

**Request Method**: `GET`

**Response Header**: `JSON`
```
{
    "pizza": 2,
    "shape": 2,
    "size": 1,
    "toppings": [
        2,
        5
    ]
}
```

# Pizza Orders Details PUT API
Modifies the details of the requested order

**API URL**: `<host>/orders/<int:order-id>`

**Request Method**: `PUT`

**Request Header**: `JSON`
```
{
    "pizza": 2,
    "shape": 2,
    "size": 1,
    "toppings": [
        2,
        5
    ]
}
```

**Response Header**: `JSON`
```
{
    "pizza": 2,
    "shape": 2,
    "size": 1,
    "toppings": [
        2,
        5
    ]
}
``` 


# Pizza Orders Details DELETE API
Deletes the requested order

**API URL**: `<host>/orders/<int:order-id>`

**Request Method**: `DELETE`

**Response Header**: `TEXT`
```
Order Deleted
``` 