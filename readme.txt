POST -->	http://127.0.0.1:8000/auth/users/

#### Request Body / JSON ####
{
	"username": "TestUser",
	"password": "test@12345",
	"email": "test@localhost.com"
}

---------------------------------------------------------------------------------

POST -->	http://127.0.0.1:8000/auth/token/login/

#### Request Body / JSON ####
{
	"username": "TestUser",
	"password": "test@12345"
}

#### Response ####
{
	"auth_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

---------------------------------------------------------------------------------

POST -->	http://127.0.0.1:8000/auth/token/logout/

####  Request header ####

Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

---------------------------------------------------------------------------------

GET & POST -->	http://127.0.0.1:8000/restaurant/menu-items

####  Request header ####

Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#### Request Body / JSON ####
{
	"Title": "Pizza",
	"Price": 25.00,
	"Inventory": 50
}

---------------------------------------------------------------------------------

GET & PUT & PATCH -->	http://127.0.0.1:8000/restaurant/menu-items/1

#### Request header ####

Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#### Request Body / PUT & PATCH Method ####
{
	"Title": "IceCream",
	"Price": 15.00,
	"Inventory": 50
}

---------------------------------------------------------------------------------

GET & POST -->	http://127.0.0.1:8000/restaurant/booking/tables

#### Request header ####

Authorization : Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#### Request Body / POST Method ####
{
	"Name": "First Booking",
	"No_of_guests": 3,
	"BookingDate": "2023-05-10"
}

