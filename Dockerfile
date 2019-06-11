FROM ctftraining/base_image_nginx_mysql_php_56

LABEL Author="glzjin <i@zhaoj.in>" Blog="https://www.zhaoj.in"

COPY src /var/www/html
