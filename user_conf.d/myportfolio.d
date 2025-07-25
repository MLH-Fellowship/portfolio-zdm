server {
   listen 80;
   server_name zidannimlh.duckdns.org;

   if ($host = zidannimlh.duckdns.org) {
       return 301 https://$host$request_uri;
   }
}

server {
   listen 443 ssl;
   server_name zidannimlh.duckdns.org;

   location / {
       proxy_pass http://myportfolio:5000;
   }

   # Load the certificate files.
   ssl_certificate /etc/letsencrypt/live/zidannimlh.duckdns.org/fullchain.pem;
   ssl_certificate_key
       /etc/letsencrypt/live/zidannimlh.duckdns.org/privkey.pem;
   ssl_trusted_certificate
       /etc/letsencrypt/live/zidannimlh.duckdns.org/chain.pem;
}