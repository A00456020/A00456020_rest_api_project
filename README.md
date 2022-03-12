# A00456020_rest_api_project
<h1>REST API Project in Python using Django Framework</h1><br>
This is my repository for REST API Project for MCDA 5550.

<p>I am Parth Tarak Vaidya, A00456020, MCDA Fall 2021 cohort, Saint Mary's University, Halifax.</p>

<p>This repository contains REST API project that was implemented in Python using Django framework and Django REST Framework.</p>

<p>The database used is MySQL database created using the following sql commands:</p>
<p>
create database restapi_db;<br>
create user 'project_dbadmin'@'%' identified by "access";<br>
grant all on restapi_db.* to 'project_dbadmin'@'%';<br>
</p>

<h2>API Definition</h2>
<p>The API, usually when deployed using Django admin console, works on <a href="http://localhost:8000/">http://localhost:8000/</a></p>
<p>Just to list a few, The following functionalities have been implemented:</p>
<li>Add a new Hotel</li>
<li>Add a new Customer</li>
<li>Create a new Reservation</li>
<li>Get details of a Hotel by id</li>
<li>Get details of a Customer by id</li>
<li>Get details of a Reservation by id</li>
<li>Get list of all existing Hotels</li>
<li>Get list of all existing Customers</li>
<li>Get list of all existing Reservations</li>
<li>Get Confirmation Number of Reservation</li>
<p>Models and Attributes:</p>
<p>Hotel</p>
<ol>
<li>id: auto-increment integer primary key attribute</li>
<li>name: string "name" attribute with maximum length 100. Can't be null</li>
<li>website: string website name attribute with maximum length 100. Can't be null</li>
<li>country: string country name attribute with maximum length 100. Can't be null</li>
<li>city: [optional] string city name attribute with maximum length 100. Can be null</li>
</ol>
<p>Customer</p>
<ol>
<li>id: auto-increment integer primary key attribute</li>
<li>name: string "name" attribute with maximum length 100. Can't be null</li>
<li>mobile: string phone number attribute with maximum length 100. Can't be null, can't be blank</li>
<li>email: string email id attribute with maximum length 100. Can't be null, can't be blank</li>
</ol>
<p>Reservation</p>
<ol>
<li>id: auto-increment integer primary key attribute, also used for confirmation of reservation.</li>
<li>customer_id: integer customer id foreign key attribute. Can't be null and has to be present in Customers</li>
<li>customer_name: string customer's name attribute. Will be calculated during insertion from customer_id</li>
<li>hotel_id: integer hotel id foreign key attribute. Can't be null and has to be present in Hotels</li>
<li>hotel_name: string hotel's name attribute. Will be calculated during insertion from hotel_id</li>
<li>number_of_rooms: integer number of rooms in reservation attribute. Can't be null, default is 1</li>
<li>checkin_date: date attribute for check-in in standard ISO-8601 format (yyyy-mm-dd). Can't be null, can't be blank</li>
<li>checkout_date: date attribute for check-out in standard ISO-8601 format (yyyy-mm-dd). Can't be null, can't be blank</li>
<li>customer_phone: string customer's phone number attribute. Will be calculated during insertion from customer_id</li>
<li>hotel_website: string hotel's website name attribute. Will be calculated during insertion from hotel_id</li>
</ol>
<p>Possible URLs are:</p>
<li><a href="http://localhost:8000/hotels/">http://localhost:8000/hotels/</a></li>
<li><a href="http://localhost:8000/customers/">http://localhost:8000/customers/</a></li>
<li><a href="http://localhost:8000/reservations/">http://localhost:8000/reservations/</a></li>
<li><a href="http://localhost:8000/getListOfHotels/">http://localhost:8000/getListOfHotels/</a></li>
<li><a href="http://localhost:8000/reservationConfirmation/">http://localhost:8000/reservationConfirmation/</a></li>


<h2>Instructions and Sample API calls</h2>

<h3>The First Call, API CALL 1 as mentioned in the project Instructions document is implemented as follows:</h3>
<ul>
<li>request type: "GET"</li>
<li>request URL: http://127.0.0.1:8000/getListOfHotels/</li>
<li>request parameters: None</li>
<li>request body: Empty</li>
<li>Response:{<br>
    "hotels_list": [<br>
        {<br>
            "id": 1,<br>
            "name": "ahmedabad inn",<br>
            "country": "India",<br>
            "website": "ahmedabadinn.com",<br>
            "city": "Ahmedabad"<br>
        },<br>
        {<br>
            "id": 2,<br>
            "name": "rajkot inn",<br>
            "country": "India",<br>
            "website": "rajkotinn.com",<br>
            "city": "Rajkot"<br>
        },<br>
        {<br>
            "id": 3,<br>
            "name": "bhavnagar inn",<br>
            "country": "India",<br>
            "website": "bhavnagarinn.com",<br>
            "city": "Bhavnagar"<br>
        }<br>
    ]<br>
}</li>
</ul>

<h3>The Second Call, API CALL 2 as mentioned in the project Instructions document is implemented as follows:</h3>
<ul>
<li>request type: "POST"</li>
<li>request URL: http://127.0.0.1:8000/reservationConfirmation/</li>
<li>request parameters: None</li>
<li>request body: <br>
    {<br>
    "hotel_id": 2,<br>
    "checkin_date": "2022-03-19",<br>
    "checkout_date": "2022-03-25",<br>
    "customer_id": 1,<br>
    "number_of_rooms": 4<br>
}<br></li>
<li>Response:<br>
    {<br>
    "confirmation_number": 11<br>
}<br></li>
</ul>

<h5>To get the list of all the hotels, use:</h5>

<ul>
<li>request type: "GET"</li>
<li>request URL: http://127.0.0.1:8000/hotels/</li>
<li>request parameters: None</li>
<li>request body: Empty</li>
<li>Response:[
    {
        "id": 1,
        "name": "ahmedabad inn",
        "country": "India",
        "website": "ahmedabadinn.com",
        "city": "Ahmedabad"
    },
    {
        "id": 2,
        "name": "rajkot inn",
        "country": "India",
        "website": "rajkotinn.com",
        "city": "Rajkot"
    },
]</li>
</ul>


<h5>To get a hotel details by id, for example 2, use:</h5>

<ul>
<li>request type: "GET"</li>
<li>request URL: http://127.0.0.1:8000/hotels/2</li>
<li>request parameters: None</li>
<li>request body: Empty</li>
<li>Response:[
    {
        "id": 2,
        "name": "rajkot inn",
        "country": "India",
        "website": "rajkotinn.com",
        "city": "Rajkot"
    }
]</li>
</ul>

<h5>To get the list of all the customers, use:</h5>

<ul>
<li>request type: "GET"</li>
<li>request URL: http://127.0.0.1:8000/customers/</li>
<li>request parameters: None</li>
<li>request body: Empty</li>
<li>Response:[
    {
        "id": 1,
        "name": "Parth",
        "mobile": "9029897921",
        "email": "vdpar2000@gmail.com"
    }
]</li>
</ul>

<h5>To get a customer's details by id, for example 1, use:</h5>

<ul>
<li>request type: "GET"</li>
<li>request URL: http://127.0.0.1:8000/customers/1</li>
<li>request parameters: None</li>
<li>request body: Empty</li>
<li>Response:[
    {
        "id": 1,
        "name": "Parth",
        "mobile": "9029897921",
        "email": "vdpar2000@gmail.com"
    }
]</li>
</ul>

<h5>To add a new Hotel to database, use:</h5>
<ul>
<li>request type: "POST"</li>
<li>request URL: http://127.0.0.1:8000/hotels/</li>
<li>request parameters: None</li>
<li>request body: <br>
    {
    "name": "rajkot inn",
    "country": "India",
    "website": "rajkotinn.com",
    "city": "Rajkot"
}<br></li>
<li>Response:<br>
    {
    "id": 4,
    "name": "rajkot inn",
    "country": "India",
    "website": "rajkotinn.com",
    "city": "Rajkot"
}<br></li>
</ul>

<h5>To add a new Customer to database, use:</h5>
<ul>
<li>request type: "POST"</li>
<li>request URL: http://127.0.0.1:8000/customers/</li>
<li>request parameters: None</li>
<li>request body: <br>
    {
    "name": "Parth",
    "mobile": "9029897921",
    "email": "vdpar2000@gmail.com"
}<br></li>
<li>Response:<br>
    {
    "id": 3,
    "name": "Parth",
    "mobile": "9029897921",
    "email": "vdpar2000@gmail.com"
}<br></li>
</ul>

<h5>To make a new Reservation and add it to database, use:</h5>
<ul>
<li>request type: "POST"</li>
<li>request URL: http://127.0.0.1:8000/reservations/</li>
<li>request parameters: None</li>
<li>request body: <br>
    {
    "hotel_id": 2,
    "checkin_date": "2022-03-19",
    "checkout_date": "2022-03-25",
    "customer_id": 1,
    "number_of_rooms": 4
}<br></li>
<li>Response:<br>
    {
    "id": 12,
    "hotel_id": 2,
    "customer_id": 1,
    "hotel_name": "rajkot inn",
    "customer_name": "Parth",
    "customer_phone": "9029897921",
    "hotel_website": "rajkotinn.com",
    "number_of_rooms": 4,
    "checkin_date": "2022-03-19",
    "checkout_date": "2022-03-25"
}<br></li>
</ul>

Thank you,<br>
Parth Vaidya.
