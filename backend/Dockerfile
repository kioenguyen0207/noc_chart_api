FROM python:3.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 443
# CMD [ "python", "run.py" ]
# ENTRYPOINT ["./gunicorn.sh"]
CMD [ "gunicorn", "run:app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:443" ]