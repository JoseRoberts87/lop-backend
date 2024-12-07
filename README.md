# Getting Started

This project uses [uv](https://docs.astral.sh/uv/#project-management) as a project and dependency manager

To run the project for the first time after installing `uv` run the following command from the root directory
`uv install`

To run the project locally run
`uv run fastapi dev`


## Docker

`docker build -t lop-backend .`

`docker run -p 8000:80 fastapi-app`