1 Install requirements
pip install -r requirements.txt

2 Create database
python setup_database.py

3 Train model
python seed_memory.py

4 Run API
uvicorn main:app --reload