FROM python:3.10.13-alpine3.19
ADD src/ /application
WORKDIR /application
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
	gcc \
	libc-dev \
	linux-headers \
	; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	apk del .build-deps;
EXPOSE 3001
VOLUME /application
CMD uwsgi --http :3001  --manage-script-name --mount /application=flask_app:app --enable-threads --processes 5