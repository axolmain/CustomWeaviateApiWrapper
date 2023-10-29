<p align="center">
<img src="https://img.shields.io/github/languages/code-size/axolmain/CustomWeaviateApiWrapper" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/last-commit/axolmain/CustomWeaviateApiWrapper" alt="GitHub last commit" />
<img src="https://img.shields.io/github/commit-activity/m/axolmain/CustomWeaviateApiWrapper" alt="GitHub commit activity month" />
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT license" />
</p>

<p></p>
<p></p>

# 📌 Overview

CustomWeaviateApiWrapper is a Python library that provides a convenient and simplified way to interact with the Weaviate API. It utilizes essential dependencies like Flask, requests, and weaviate-client for seamless integration.

## 🔍 Table of Contents

* [📁 Project Structure](##project-structure)

* [📝 Project Summary](##project-summary)

* [💻 Stack](##stack)

* [📄 License](##license)

## 📁 Project Structure

```bash
├── .gitignore
├── .idea
│   ├── .gitignore
│   ├── WeviateApi.iml
│   ├── aws.xml
│   ├── inspectionProfiles
│   │   ├── Project_Default.xml
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   └── modules.xml
├── README.md
├── app.py
└── requirements.txt
```

## 📝 Project Summary

This project was created to test a self-hosted Weaviate instance and to learn how to use the Weaviate API. The project is a simple API wrapper that allows the user to create, read, update, and delete objects in a Weaviate instance. The wrapper currently only allows the user to create, read, update, and delete classes in a Weaviate instance.

To create the Weaviate instance, I used Docker to create a container that runs the Weaviate instance. The Weaviate instance is hosted on a virtual machine on Hostinger. The Weaviate instance is accessible through the internet and can be accessed by anyone during this testing phase. The container uses 4 modules:
- semitechnologies/qna-transformers:distilbert-base-cased-distilled-squad
- semitechnologies/reranker-transformers:cross-encoder-ms-marco-MiniLM-L-6-v2
- semitechnologies/sum-transformers:facebook-bart-large-cnn-1.0.0
- semitechnologies/weaviate:1.21.8

These modules are not used by this Flask API wrapper as of 29/10/23.

The Flask wrapper is to be used on a local machine and is not hosted on the internet. The wrapper is used to test the Weaviate instance and to learn how to use the Weaviate API. The wrapper is not intended to be used in a production environment. It uses Flask together with SwaggerUI to allow for easier testing of the API endpoints and a quick visualization of the Models. 

Testing software is always the most tedious part of engineering, but it's also arguably the most important part. This Flask wrapper streamlines the testing process for my custom Weaviate instance and also allows me to learn how to use the Weaviate python library for future development.

[Software Demo Video](https://youtu.be/SbZFCgqNyaM)

## Cloud Database

The cloud database used in this project is as mentioned above, a self-hosted Weaviate instance, deployed on a virtual machine provided by Hostinger via Docker. Weaviate is an open-source, GraphQL and RESTful API-enabled, database that allows for the storage, search, and retrieval of data.

The base structure of my Weaviate database is as follows:
```bash
└── Classes
    └── ClassName
        ├── ID
        └── Properties
            ├── fileTextEmbeddings
            │    ├── id
            │    └── text
            │
            └── id
```
This structure allows for the storage of files and easy development in the future when adding actual files and embeddings.

## 💻 Stack

- [flask](https://pypi.org/project/Flask/): A lightweight web framework for building web applications.
- [requests](https://pypi.org/project/requests/): A versatile HTTP library for making HTTP requests.
- [cryptography](https://pypi.org/project/cryptography/): Provides cryptographic recipes and primitives.
- [weaviate-client](https://pypi.org/project/weaviate-client/): Python client for interacting with Weaviate, a knowledge graph.
- [Authlib](https://pypi.org/project/Authlib/): A powerful authentication library for securing web applications.
- [flask-restx](https://pypi.org/project/flask-restx/): An extension for Flask that adds support for quickly building REST APIs.
- [werkzeug](https://pypi.org/project/Werkzeug/): A comprehensive WSGI web application library.
- [jsonschema](https://pypi.org/project/jsonschema/): A library for validating JSON data against a given schema.

## Useful Websites

- [Weaviate](https://weaviate.io/)
- [YouTube](https://www.youtube.com/watch?v=klTvEwg3oJ4)
- [Creating SwaggerUI with Flask](https://medium.com/the-ai-analytics-corner/swagger-ui-to-your-python-flask-api-9bf1c8fc0178)

# Future Work

- Add tests for file upload
- Add tests for QnA search
- Add tests for user Authentication

# 📄 License

The MIT License (MIT)

Copyright (c) 2023 Sebastian Dunn

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.