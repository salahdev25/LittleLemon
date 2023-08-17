POST -->	http://127.0.0.1:8000/auth/users/

#### Request Body / JSON ####
```code
{
	"username": "TestUser",
	"password": "test@12345",
	"email": "test@localhost.com"
}
```
---------------------------------------------------------------------------------

POST -->	http://127.0.0.1:8000/auth/token/login/

#### Request Body / JSON ####
```code
{
	"username": "TestUser",
	"password": "test@12345"
}
```

#### Response ####
```code
{
	"auth_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```
---------------------------------------------------------------------------------

POST -->	http://127.0.0.1:8000/auth/token/logout/

####  Request header ####
```code
Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---------------------------------------------------------------------------------

GET & POST -->	http://127.0.0.1:8000/restaurant/menu-items

####  Request header ####

```code
Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Request Body / JSON ####
```code
{
	"Title": "Pizza",
	"Price": 25.00,
	"Inventory": 50
}
```
---------------------------------------------------------------------------------

GET & PUT & PATCH -->	http://127.0.0.1:8000/restaurant/menu-items/1

#### Request header ####

```code
Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Request Body / PUT & PATCH Method ####
```code
{
	"Title": "IceCream",
	"Price": 15.00,
	"Inventory": 50
}
```
---------------------------------------------------------------------------------

GET & POST -->	http://127.0.0.1:8000/restaurant/booking/tables

#### Request header ####

```code
Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Request Body / POST Method ####
```code
{
	"Name": "First Booking",
	"No_of_guests": 3,
	"BookingDate": "2023-05-10"
}
```
