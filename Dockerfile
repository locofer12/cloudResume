FROM nginx:alpine

# Copiar los archivos de tu proyecto al directorio HTML de NGINX
COPY . /usr/share/nginx/html/

# Reemplazar la configuración de NGINX para que escuche en el puerto 8080
RUN sed -i 's/listen\(.*\)80;/listen\180;/g' /etc/nginx/conf.d/default.conf

# Exponer el puerto 8080
EXPOSE 8080
