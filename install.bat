@echo off
REM Create a virtual environment named 'env'
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate

REM Install requirements from requirements.txt
pip install -r requirements.txt

REM Notify the user
echo Virtual environment 'env' is set up and requirements are installed.