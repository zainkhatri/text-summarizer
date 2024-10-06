# Step 1: Use an official Python runtime as a parent image
FROM python:3.9

# Step 2: Install Rust (required to build tokenizers)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Copy the requirements file into the container at /app
COPY requirements.txt .

# Step 5: Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the current directory contents into the container at /app
COPY . .

# Step 7: Make port 5000 available to the world outside this container
EXPOSE 5000

# Step 8: Define environment variable
ENV FLASK_ENV=production

# Step 9: Run the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "summary:app"]
