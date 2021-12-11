# docx-template

# Development Environment Setup

## Prerequisite
* Python3
* Pip
* Virtualenvironment

## Installation

1. Clone the repository
`git clone https://github.com/senthilsweb/zybots.git`

1. Change directory to `zybots\docx`
`cd zybots\docx`

1. Create virtual environment inside the project root
`virtualenv venv -p python3.7`

1. Activate the virtual environment from the bin folder inside the **venv**

`source ./venv/bin/activate`

1 Go to project root folder and then Install dependencies

`cd to root folder`

`pip install -r requirements.txt`

1 Start the sever

`gunicorn resources.api:app -b 127.0.0.1:3000`



## API available in this sample code

### Generate word file from docx template

```
POST http://127.0.0.1:3000/export/word
```

```
{
    "user": {
        "firstname": "John",
        "project": {
            "name": "Robot framework development"
        }
    },
    "template": {
        "file": "exp-template.docx"
    }
}
```
