# Project dokumentáció – Python + Flask demo app

Ez egy egyszerű "Hello world" jellegű webalkalmazás Python + Flask segítségével,
amely HTTP-n a `http://localhost:8080` címen érhető el és egy szöveget ad vissza.

## 2.1 Alkalmazás

- Az alkalmazás Python + Flask alapú.
- A fő fájl: `app.py`.
- Az app a 8080-as porton fut, és a `/` végponton az alábbi szöveget adja vissza:

> "Hello Hello! Az app fut a 8080 Porton."

Lokális futtatás (Docker nélkül):

```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
