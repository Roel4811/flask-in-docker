# Simple Python Flask Dockerized Application
This will walk through the steps to get a Flask App running locally, with autoreload

- 1. Install Docker https://www.docker.com/docker-toolbox
- 2. fork this repo to your own GH account
- 3. clone it
- 4. go to web dir of this repo
- 5. run `docker-compose up`
- 6. go to `127.0.0.1:5000` (if it doesn't work, you can run `docker-machine ip`, this might be the IP you have to use)

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
- Don't commit to master, but make a new branch. This way your PR can be reviewed


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
static_tasks = [{
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
}]
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


## Ex. 3 People overview in HTML
With Jinja2 you can render html templates. Your goals is to get an overview of all people on this page.

Do this by performing following steps:
- call your own api `get many people` FUNCTION.
- extract the json of this response object (hints: use `response` attr of this object)
- transform this json into a dict with `json.loads`
- extract `people` from this dict
- pass this value to your template
- in your template loop over this dict (hint: Try to find out how this works in jinja2 docs)
- print the people dynamically

### extra
- Can you make filtering/pagination work for these routes? (hint: or can you explain why this already works?)
- Can you display the correct time (in ISO format) this page was rendered. (hint: try to find a library that does this & pass this variable to your template)

## Ex. 4 Tasks overview in HTML
Can you do Ex. 3 but then for tasks?

## Ex. 5 Can you add more functionality to this app?
For inspiration, check other tutorials. Feel fry to install other libraries etc.


