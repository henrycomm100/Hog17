FROM nginx:1.17.9

LABEL maintainer="Henry.MJ<henry.ma@comm100.com>"

ENV NGINX_VERSION=1.17.9
ARG work_pwd=/data/html/


USER root

RUN apt-get -yq update && apt-get install -y curl && \
ln -sf /dev/stdout /var/log/nginx/access.log && \
ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME [ "/data" ]

WORKDIR ${work_pwd}

COPY index.html .

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

STOPSIGNAL SIGRTMAX

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -fs http://localhost/ || exit 1