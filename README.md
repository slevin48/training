# Python Training
Learn Python, Numpy, Pandas, Scikit-Learn & Streamlit 


# 1. Get started with programming in Python
Download Python: https://www.python.org/ 

Why Python: Number 1 language according to [TIOBE index](https://www.tiobe.com/tiobe-index/) 

Agenda of [Python 101](doc/Python%20101.pptx):

| Chapter | | resources |
|---------|-|-----------|
|Datatypes|![](img/datatypes.jpg) | https://realpython.com/python-data-types/ |
|Loops & Conditions | ![](img/loops.jpg)|https://realpython.com/python-for-loop/|
|Functions | ![](img/functions.jpg)|https://realpython.com/defining-your-own-python-function/ |
|Modules|![](img/modules.jpg)|https://realpython.com/python-modules-packages/ |
|VScode|![](img/vscode.jpg)|https://realpython.com/python-development-visual-studio-code/ |
|Files management|![](img/files.jpg)|https://realpython.com/working-with-files-in-python/ |

**Hands on + exercise!!!**

Open Terminal, and run python:
```python
>>> print("Hello World")
```

# 2. Discover the Scientific Python ecosystem

* [Numpy 101](doc/Numpy%20101.pptx)
* [Pandas 101](doc/Pandas%20101.pptx)
* [Scikit-Learn 101](doc/Sklearn%20101.pptx)

# 3. Develop web apps with Streamlit

Install via PIP (package manager for Python): `$ pip install streamlit`

Or if you cannot find pip:
`$ python3 -m pip install streamlit`

Develop your first [app.py](code/app.py):
```python
import streamlit as st
st.write(“Hello World!”)
```

![app](img/app.png)

Read more: https://streamlit.io/

**Deploy with Heroku**

Heroku tutorial: https://devcenter.heroku.com/articles/getting-started-with-python
https://github.com/slevin48/streamlit

**Required files:**
1.	[setup.sh](code/setup.sh)
2.	[Procfile](code/Procfile)
3.	[requirements.txt](code/requirements.txt)

**Deploy with Streamlit Cloud**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/slevin48/training/main/app.py)

# 4. Version your code with Git & GitHub
Learn the basics about source control with Git: 
- https://git-scm.com/
- https://realpython.com/advanced-git-for-pythonistas/

