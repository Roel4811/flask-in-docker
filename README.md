# Simple Python Flask Dockerized Application
This will walk through the steps to get a Flask App running locally, with autoreload

- 1. fork this dir to your own GH account
- 2. clone it
- 3. go to web dir
- 4. run `docker-compose up`
- 5. go to `127.0.0.1:5000` (if it doesn't work, you can run `docker-machine ip`, this might be the IP you have to use)

# To install new libraries
- `Add them to requirements.txt`
- run `docker-compose build`

# Style Guide
- Never use tabs, instead use 4 spaces
- Use single quotes for strings, e.g. `foo = 'bar'` instead of `foo = "bar"`
- Use Doc strings for all your functions, explain what they do
- Use descriptive file names, e.g. `index` instead of `i`
- Try to keep it DRY
- Use comments where needed

# Exercises

## Ex. 1 Finish the people API
In the function descriptions (of `api/people.py`) is described what it should do. Make sure it does!

Hints:
- Try to use build-in python functions where you can.
- You can use stackoverflow!
- Use the style guide


## Ex. 2 Create a tasks API, in a new file `api/tasks.py`
Use the following fixtures
```
static_tasks = {
    'id': 1,
    'name': 'Clean up',
    'status': 'done'
},
{
    'id': 2,
    'name': 'Fix your car',
    'status': 'todo',

},
{
    'id': 3,
    'name': 'programming some Flask',
    'status': 'work in progress',
}
```

Requirements
- create a get single API
- create a get many API
  - filters:
    - name (like filter)
    - status (equals filter)

  - sort_by:
    - id
    - name
    - status

  - pagination
    - results_per_page (default=1)
    - page_number (default = 0)

Hints
- reuse some functions of the people API, (maybe put those 'helper' function in a new file??)


## Ex. 3




