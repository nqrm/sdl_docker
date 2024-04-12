FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f http://localhost || exit 1
