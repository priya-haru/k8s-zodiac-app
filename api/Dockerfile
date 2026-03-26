FROM python:3.9-slim
WORKDIR /app
# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .
# Tell the container to listen on port 5000
EXPOSE 5000
CMD ["python", "app.py"]
