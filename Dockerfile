# set up the container.
FROM python:3.12-slim

# set the working dir.
WORKDIR /app

# copy the app dir.
COPY projects/frontend app

# uvのlockから入れる方法似直す
RUN pip install --no-cache-dir fastapi uvicorn

# expose the port.
EXPOSE 8000

# command to run the app using uvicorn.
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
