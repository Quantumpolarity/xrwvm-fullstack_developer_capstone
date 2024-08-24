# 1. Use an official Python runtime as the base image
FROM python:3.12.0-slim-bookworm

# 2. Set environment variables
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1

# 3. Define the application directory in the container
ENV APP=/app

# 4. Set the working directory inside the container
WORKDIR $APP

# 5. Copy the requirements file to the container
COPY requirements.txt $APP

# 6. Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# 7. Copy the rest of the application code to the container
COPY . $APP

# 8. Expose the port the application will run on
EXPOSE 8000

# 9. Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# 10. Set the entrypoint to the shell script that sets up the environment
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# 11. Define the command to run your application
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
