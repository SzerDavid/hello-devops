# 1 Project dokumentáció – Python + Flask demo app

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
```
### 2.2 Buildelés

A projektet a következő lépések alapján lehet előkészíteni és futtatni:

- Virtuális környezet létrehozása:

    python -m venv venv

- Virtuális környezet aktiválása:

    .\venv\Scripts\activate

- Függőségek telepítése:

    pip install -r requirements.txt

- Alkalmazás indítása:

    python app.py

#### 2.4 Dockerizálás

A projekt tartalmaz egy Dockerfile-t, amely:

- a python:3.12-slim base image-re épül,

- bemásolja a requirements.txt fájlt és telepíti a függőségeket,

- bemásolja az app.py fájlt,

- a konténer indulásakor elindítja az alkalmazást a 8080-as porton.

Docker image buildelése

    docker build -t szerdavid/hello-devops:latest .

Docker konténer futtatása

    docker run -p 8080:8080 szerdavid/hello-devops:latest

Ezután az alkalmazás Docker konténerből futva is elérhető HTTP-n:
    http://localhost:8080

##### 3.2 CI – pipeline + free registry (Docker Hub)

A projekt GitHub Actions CI pipeline-t használ, amely:

- pullolja a kódot a GitHub repóból,

- bejelentkezik a Docker Hub-ba GitHub Secrets segítségével:

    DOCKERHUB_USERNAME

    DOCKERHUB_TOKEN

- buildeli a Docker image-et a Dockerfile alapján,

- pusholja az image-et egy free registry-be (Docker Hub).

A workflow fájl helye:

    .github/workflows/deploy.yaml


A pipeline az alábbi image-et hozza létre és pusholja a Docker Hubra:

    docker.io/szerdavid/hello-devops:latest

Példa:

    docker.io/szerdavid/hello-devops:latest

Image lehúzása és futtatása a registryből

    docker pull szerdavid/hello-devops:latest
    docker run -p 8080:8080 szerdavid/hello-devops:latest

Példa:

    docker pull szerdavid/hello-devops:latest
    docker run -p 8080:8080 szerdavid/hello-devops:latest