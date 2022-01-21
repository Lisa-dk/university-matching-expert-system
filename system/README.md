# University Matching Program for Turkish Students

This programme aims to output a list of bachelors degree engineering studies in the Netherlands for Turkish high school students based on their diploma, subject choices, grades, english level and preferences. 

## Project description
The admission requirements change for each study programme and university. Therefore, the process of finding a study programme that matches a student's qualities, and preferences is difficult to research, and takes a lot of time. In consultation with the CEO’s of a consulting company, ‘Bluedot’ found in Turkey, which  guides students in the process of choosing and applying for a university programme in the United States of America (USA), the United Kingdom (UK) and the Netherlands, we have build this programme with the hopes of facilitating the university matching process for both the experts and the students/clients.


## How to Install and Run the Program

In order to run the program, you need to install python and the tkinter package. The tkinter package can be installed using pip. 

### Module versions

We used python version `3.10.0`. Furthermore, we used some modules from the standard library like webbrowser, os, re and enum.

We used the following module versions in our program:

| Module | Version |
| ----------- | ----------- |
| pip | `21.3.1` |
| Pillow | `8.4.0` or `9.0.0`|
| tkinter | `8.6` |

### Installing

First make sure, python and pip are installed and up-to-date. 
You can update pip with the following commands:

``` python -m pip install --upgrade pip ```

or 

``` python3 -m pip install --upgrade pip ```

The tkinter package should be included in your python version, but to be sure you can check this (and the tkinter version) by opening python in your terminal and running the following commands:

``` 
import tkinter
tkinter.TkVersion
```

When you have the correct versions of python and pip installed, you can install the Pillow package by typing one of the following commands in your terminal:

```  python -m pip install --upgrade Pillow ```

or 

```  python3 -m pip install --upgrade Pillow ```

[comment]: <> (For windows:)

[comment]: <> (``` pip install tk ```)

[comment]: <> (For MACOS:)

[comment]: <> (``` pip3 install tk ```)

### Running

To run the program, first make sure you are in the correct directory (the directory this README file is in).
Then type one of the following commands in your terminal:

``` python main.py ```

or

``` python3 main.py ```
