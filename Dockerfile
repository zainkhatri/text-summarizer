# Use an official Python runtime as a parent image
FROM python:3.9

# Install Rust (required to build tokenizers)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Set Flask debug mode based on the desired environment
ENV FLASK_DEBUG=0

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "summary:app"]
