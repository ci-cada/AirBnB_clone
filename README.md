<p align="center">
  <img src="img/front.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">HolbertonBnB</h1>
<p align="center">AirBnB Clone</p>

<p align="center">
  <img src="img/console.png" alt="console image">
</p>

---

## Description of the project

HolbertonBnB is a complete web application that intergrates; a database storage, a back-end API that provides a communication and a front-end interfacing as a clone of AirBnB.

This project currently only implements the back end console.

## Classes

## Storage

## The console
The console is a command line interpreter that permits management of the back end of HolbertonBnB i.e. creating updating and destroying.
It can be used to handle and manipulate all the classes used by the application.

### Installation
To use the AirBnB Clone console, follow these steps:
  1. Clone the repository:

  ```
   git clone https://github.com/your-username/airbnb-clone-console.git
  ```
  2. Navigate to the projects directory:

  ```
  cd airbnb_clone
  ```
  3. Start the application:

  ```
  python3 console.py
  ```

### Execution
The console can run both interactively and non-interactively.

To run the console in interactive mode, run the file `console.py` by itself:

```
$ ./console.py
```
When in interactive mode, the console will display a prompt for input:

```
$ ./console.py
(hbnb)
```

To run the console in non-interactive mode, pipe any command(s) into the execution of the `console.py` file at the command line:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

To quit the console, enter the command `quit`, or input an EOF signal(`ctrl-D`)

```
$ ./console.py
(hbnb) quit
$
```
```
$ ./console.py
(hbnb) EOF
$
```
### Console commands


## Testing :test_tube:
To run the entire test suite simultaneously:

```
python3 unittest -m discover tests
```

Alternatively, you can specify a single test to run:

```
python3 unittest -m tests/test_console.py
```
