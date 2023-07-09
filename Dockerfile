FROM python:3.10

WORKDIR /.

COPY requirements.txt /./

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --no-cache-dir -r reqr.txt

COPY rewrite_for_file ./rewrite_for_file

CMD ["python", "rewrite_for_file/main.py"]