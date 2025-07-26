server {
   listen 443 ssl;
   server_name zidannimlh.duckdns.org;

   location / {
       proxy_pass http://myportfolio:5000;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
   }

   # SSL configuration
   ssl_certificate /etc/letsencrypt/live/zidannimlh.duckdns.org/fullchain.pem;
   ssl_certificate_key /etc/letsencrypt/live/zidannimlh.duckdns.org/privkey.pem;
   ssl_trusted_certificate /etc/letsencrypt/live/zidannimlh.duckdns.org/chain.pem;
   
   # SSL settings
   ssl_session_cache shared:le_nginx_SSL:10m;
   ssl_session_timeout 1440m;
   ssl_session_tickets off;
   ssl_protocols TLSv1.2 TLSv1.3;
   ssl_prefer_server_ciphers off;
   ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
}