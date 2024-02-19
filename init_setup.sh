echo "$(date): start"
echo "$(date): Creating virtual env"
python -m venv venv
echo "$(date): Activating venv"
venv/Scripts/activate
echo "$(date): Installing Dev requirements"
pip install -r requirements_dev.txt
echo "$(date): END"