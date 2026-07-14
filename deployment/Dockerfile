# Use a slim, production-ready base image to keep the container footprint small
FROM python:3.9-slim

# Set environment variables up front
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Create a non-root user with UID 1000 (Required by Hugging Face Spaces)
RUN useradd -m -u 1000 user
USER user

# Set the working directory directly inside the user's home space
WORKDIR $HOME/app

# Copy the application files ONCE, giving ownership directly to our non-root user
COPY --chown=user . $HOME/app

# Install Python dependencies safely under the user context
RUN pip3 install --no-cache-dir --user -r requirements.txt

# Expose port 7860 and bind to 0.0.0.0 (Required by Hugging Face Spaces)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
