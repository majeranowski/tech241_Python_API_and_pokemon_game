# APIs

#### What is API
Application Programming Interface

The main reason is to transfer data between systems.

Usually JSON is used in the process of transfering data

### Communication between client and server:

Client communicate to the API using HTTP methods:

HTTP Methods:
* GET
* POST
* PUT
* PATCH - also updates but does not replace like PUT. only modifies content
* DELETE

API sends HTTP request to the server. Server sends back the information requested in the language it was writte.
API converts to the language suitable for the client. Most cases JSON.

![Communication](MicrosoftTeams-image%20(3).png)

### HTTP
Hypertext Transfer Protocol (HTTP) is a method for encoding and transporting information between a client (such as a web browser) and a web server. HTTP is the primary protocol for transmission of information across the Internet.

HTTPS is a secured version with encryption

### HTTP Request Structure
![Communication](MicrosoftTeams-image%20(4).png)
Verb -> URL -> Version

HEADER:

Key Value Pairs

* key-value
* key-value
* key-value

Body:

Text, JSON , XML

```GET https://example.com 1.1

Content-Type : application/json
Date: Tue, 15 Nov 1994 08:12:31 GMT
Accept-Charset: utf-8

***No body required in a get request in most instances***
```
![Communication](MicrosoftTeams-image%20(5).png)
### HTTP Response structure
![Communication](MicrosoftTeams-image%20(6).png)
Response Code -> HTTP Version

HEADER

Key Value Pairs

* key-value
* key-value
* key-value


BODY

Text, JSON, XML

![Communication](MicrosoftTeams-image%20(7).png)
### REST APIs

Restful APIs because the way there way build are better to work with.

* Representational data flow (both ends need to read a format, representation needs to completely deliver the resource - all need to be send in one go, Documentation (client need to know how is likely to receive data he requested))
* URI's + naming (Uniform Resource Identifier - somewhere in the internet. not necessarily URL) - APIs gives proper names and how specific are the URLs e.g. queries ?id=1
* Statelessness -> API does not hold to a status of the request or the previous request. Every request is the new request even if the previous one is not finished.
* Caching -> time saving 


#### Types of APIs

* Open Source (e.g. postcodes, airbnb)
* APIs you need a key for (e.g. register IMDB)
* Paid APIs (e.g. Reddit)
* Private (Gov)

### Postman APP
# tech241_Python_API_and_pokemon_game
