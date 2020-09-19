FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install Flask==1.1.1 Flask-RESTful==0.3.8