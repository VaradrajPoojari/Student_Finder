# Student Finder for Professors

This project is a tool designed to help professors find students who match their research interests. Professors can input their area of research, and the system will match them with students whose research interests align with theirs.

## Getting Started

To run this project, you will need Docker installed on your system.

## Prerequisites
Docker: Install Docker

## Building the Docker Image
Use the following command to build the Docker image:

docker build --build-arg PINECONE_API_KEY="YOUR_PINECONE_API_KEY" -t your_image_name .
Replace YOUR_PINECONE_API_KEY with your actual Pinecone API key.

## Running the Docker Container
Once the image is built, run the Docker container using the following command:


docker run -p 5000:5000 your_image_name
The application will be accessible at http://localhost:5000.

## Usage

Access the application through your web browser at http://localhost:5000.
Enter your research interests as a professor.
The system will match you with students whose research interests align with yours.

## License

This project is licensed under the MIT License.


