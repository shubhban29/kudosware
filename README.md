# kudosware

To start with 

I have following end points 
# AUTH CONTROLLER

**/users/**

>This endpoint is for the creation of new users. we can create also create admin user with this end point. 
>>For user is_staff key in payload should be false and for admin account is_staff key in payload should be true

**/users/login/**

>This endpoint is for login. 
>>in request body you are requested to send email and password 
>> if login credentials are correct we get email id and token in Response

all the other endpoint are as described in the assignment sheet

# ToDo CONTROLLLER
**/getall**

> Get all the todo items this can be viewed by both user and admin


**/get/{id}**

> Get single the todo item this can be viewed by both user and admin


**/put/{id}**

> Update single ToDo item this can be accessed by admin


**/create/{id}**

> Create a new todo items this can be accessed by admin


**/delete/{id}**

> Delete a todo items this can be accessed by admin


# DEPLOYED LINKS

[SWAGGER INTERFACE](https://app.swaggerhub.com/apis-docs/shubhban29/kudosware-api-documentation/1.0.0)

[SWAGGER HEROKU DEPLOYMENT](https://kudosware-swagger.herokuapp.com/docs/)

[DJANGO HEROKU DEPLOYMENT](https://kudosware.herokuapp.com/)

