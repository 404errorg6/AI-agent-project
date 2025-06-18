# AI-agent project  
A python AI-agent project. Current directory is the default working directory.  
## Requirements
- Python with pip.  
## Setup  
- Create account on `https://aistudio.google.com` if you don't already have one.
- Create api key from `https://aistudio.google.com/apikey`.
- Copy it.
- Paste it in a `.env` file in root directory of `AI-agent-project`.
- Run `pip install -r requirements.txt`.
- Run the `main.py` with `python or python3 main.py <prompt>`.
- To change working directory, use `python3 main.py -d <directory_path>`.
- If only directory `name` is provided, tries to find `name` in current directory and sets it as working directory.
- If `directory_path` or `directory_name` doesn't exists, raises `FileNotFoundError`.
