FROM python:3.10

WORKDIR /.

COPY requirements.txt /./

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD ["python", "src/Lamel_window/main.py"]