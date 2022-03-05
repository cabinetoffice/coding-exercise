# Coding exercise API: Vayid Moussa
This is a sample API that has 3 endpoints.

1. /say-hello
2. /add
3. /join-words

The endpoints perform the following actions respectively.

1. Return "Hello World"
2. Given two numbers, add them together and return the sum
3. Given two words, join them with a dash and return the result

It has the SwaggerUI interface which can be viewed by visiting `/docs` or `/redoc` once the server is up and running.

# Requirements

This project was built using `Python 3.10.2` and uses the `fastapi` module.

The tests use the `unittest` module which comes bundled with python.

Running the API uses the `uvicorn` module, but it can be run on another ASGI server program if required.

# Installation

In the root project folder, open a terminal window and run the following command:

```bash
python3 -m venv .venv
```

This creates a virtual environment for you to install the dependencies required.

To activate this environment in your terminal run the command:

```batch
./.venv/Scripts/activate
```
On macOS you would have to run:

```bash
source .venv/bin/activate
```
You should see the virtual environment `.venv` activated by it displaying in your console window at the start in parentheses.

Now run the following command to install the dependencies:

```bash
python -m pip install -r requirements.txt
```

# Running the API

In a terminal window in the root project folder, make sure you have activated the virtual environment, then run the command:

```bash
python -m uvicorn main:app
```
You will see a message stating what ip address and port the server is running on to access the API.

# Running Tests

In the project folder, open a terminal and activate the virtual environment by running:

```batch
./.venv/Scripts/activate
```

Or if using a macOS device:

```bash
source .venv/bin/activate
```

Then run to see the output of the test results:

```bash
python -m unittest
```
