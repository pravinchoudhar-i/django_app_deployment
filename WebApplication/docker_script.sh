echo "Enter tag name: "
read docker_tag

echo "Enter container name: "
read container_name

echo "Enter server port: "
read server_port

echo "Enter docker port: "
read docker_port


sudo docker build -t $container_name .
sudo docker stop $docker_tag
sudo docker run -d --rm --name $docker_tag -p$server_port:$docker_port $container_name

