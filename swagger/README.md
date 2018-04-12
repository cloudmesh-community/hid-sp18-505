# Swagger/REST

# General
If docker is installed the entire application should run by running:

`
docker-compose up -d --build
`
Assuming you are in the root of the project.  

To see the Swgger UI visit http://127.0.0.1:5000/apidocs
To see the swagger.json specification visit http://127.0.0.1/api-docs
The swagger.json spec is generatate automatically by using the [Eve-Swagger plugin](https://github.com/pyeve/eve-swagger).  
To see the application's client open http://127.0.0.1:5000/index  

## Example curl calls
curl -i http://127.0.0.1:5000/  
curl -i http://127.0.0.1:5000/status  
curl -i http://127.0.0.1:5000/raingages  
curl -i http://127.0.0.1:5000/precipevents  

## Resources and References
https://github.com/frol/flask-restplus-server-example
https://gist.github.com/salmanwahed/13b67bc8d77f60a495be
https://travishorn.com/interactive-maps-with-vue-leaflet-5430527353c8
https://stackoverflow.com/questions/31210973/how-do-i-seed-a-mongo-database-using-docker-compose
