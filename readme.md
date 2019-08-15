**IMPORTS**
1. Flask
    * Imports Flask as a class
    * Hence the capital "F"
2. Jsonify
    * used to convert python dictionaries
3. Request
    * used to capture request data that is sent to the endpoint

**DECORATORS**
* *what are they*
    * ```A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate. ```

* *why do they matter to flask*
    * ```Flask, uses decorators extensively that results in a elegant and intuitive code (and that also results in a huge popularity of this micro framework recently). Decorator uses can be found throughout the framework, from defining routes to adding hooks to application/request lifecycle.```

**ORDER OF EVENTS**

1. Build default route
    * put in app.route decorator
    * build in simple function to return string

2. Build Store
    * Need to have some data to return
    * Would use database in normal circumstances
    * Using a dictionary is good for in-memory or testing
3. Build ```GET``` Endpoint
    * define endpoint URL
    * define methods 
        * default is get
            * not listing any assumes to use default
        * Methods is a list
        * Can contain any HTTP verbs
    * make use of jsonify
        * Used to turn python dictionaries into JSON
        * Will result in error if just returning dictionary
4. Build ```POST``` Endpoint
    * define endpoint URL
    * define methods 
        * default is get
            * not listing any assumes to use default
            * need to specific the method
        * Use URL variable to specific the name
            * Use the specified variable passed into the function
        * Use request
            * get_json() returns the data sent as json
            * gets from encoded data
        * Need to define info as a dictionary to add to current dictionary
        * Methods is a list
        *   Can contain any HTTP verbs
    * make use of jsonify
        * Used to turn python dictionaries into JSON
        * Will result in error if just returning dictionary
5. Challenges
    * use URL variables pass in

