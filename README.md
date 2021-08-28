# API-Shortner  

This api-shortner was created using django along with sqlite and redis as a caching server

## Instructions

Once code is cloned
1. setup Virtualenv if you want
2. Install ```requirements.txt```
3. Install Redis (I had to do this separately through brew for redis-server command to work)
4. Run ```redis-server```
5. go into urlshortner folder and run ``` python manage.py``` runserver in secondary terminal window
6. test away I used curl for post requests as show below

to short url api endpoint is /shorten

```shell 
curl -d "url=https://www.youtube.com/watch?v=axB4vVqnSuc" http://127.0.0.1:8000/shorten
```
## DB Schema
id - auto generated/ auto incremented starts at 1
long_url - original url that is sent with initial post request
hashed - returned hash that is used as the short url unique identifier

## Psuedo code

### short/views.py
create redis server connection for local cache

create home function which is basically a very simple home page, it gets the current site and returns a response with text


shortit function which is given the long_url
it gives the hashed url a max of 7 characters and it checks if the hashed url exists, if it does, it calls the function again to generate a fresh one


short_url function gets the long_url and passes it to the shortit function which returns the hash. the function then gets the current website data and creates the shortned url using the local domain name, in this case we are just using the local callback ip 127.0.0.1


redirector function is used for the get request, the main purpose of this function is to get the hash_id from the request, check if redis contains said hash id and if not return a false which fails the redirect.
If the id exists, then the hash_code is decoded which returns the proper hash_id to be fetched from the database afterwhich the url is replaced with the long url through a redirect.

### short/models.py
this is where the model for each short url is created, as explained in the database schema, it contains the hash and the long_url and the hash

### short/urls.py
contains the api endpoints which point to the specified functions within views



## CI/CD and tech stack choice

I chose python because I like python, pretty much for everything, it just works and its easy to understand as well as work with

redis was used as a caching server because it is very simple and can be localized. But mostly because its quick to setup and pretty much painless to use

sqlite was used as the database in this case because of its simplicity and locality in that its just a file and has a tiny footprint

CI/CD In this case, I dont think there really is any CI/CD, I was able to dockerize this whole application which involved two separate containers linked to each other,one running redis and another running the web application. It worked but there were a lot of kinks running it locally because of the limits I have on my system.

## Limitations

This is quite limited in this scenario because it is running locally. If I put this in production I would use aws api gateway with a dynamodb backend which would allow for easy scaling and redis can be intergrated as the cacheing agent while also being scaled as needed. 

When it comes to a physical server, the best way to scale this would be to create multiple instances of the docker container running the webserver with 1 redis cacheing server. Then setup a load balancer that would delegate requests to the web servers. Now ive never done this personally so Im not confident this would be a good long term solution and having one redis instance would become a bottleneck but that can be addressed by doing the same thing and having multiple redis containers that are load balanced.


