# Dakota Patient Advocate Solutions — static site
# Served by Caddy. Railway sets $PORT at runtime; the Caddyfile binds to it.

FROM caddy:2-alpine

COPY Caddyfile /etc/caddy/Caddyfile
COPY . /usr/share/caddy

# Fail the build rather than the deploy if the Caddyfile is malformed
RUN caddy validate --config /etc/caddy/Caddyfile --adapter caddyfile

EXPOSE 8080

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
