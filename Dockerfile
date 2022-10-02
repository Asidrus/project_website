FROM python:3.10
ENV HOME=/app
ENV APP_HOME=/app/website
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN pip install -r requirements.txt

# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /app/website/entrypoint.sh
# RUN chmod +x /app/website/entrypoint.sh

COPY . .
RUN python manage.py collectstatic --noinput
#ENTRYPOINT ["/app/website/entrypoint.sh"]
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "website.wsgi"]