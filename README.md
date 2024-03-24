## Docker-compose.yml: Configuration File -> Usage

To run the entire application using Docker Compose, follow these steps:

1. Make sure Docker and Docker Compose are installed on your system.

2. Navigate to the root directory of the project.

3. Run the following command with root access:

```bash
docker-compose up
```

Folder Structure
```bash
vehicle-recognition-app-main/
│
├── Backend/
│   ├── static/
│   │   ├── output
│   │   └── uploads
│   ├── app.py
│   ├── image_processing.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── Frontend/
│   ├── index.html
│   └── static/
│       ├── styles.css
│       └── script.js
├── Docker-compose.yml
└── README.md
```
