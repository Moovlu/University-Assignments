echo "--------------- Moving File ---------------"
cp mcpi_sec/ELCI-1.12.1.jar server/plugins

echo "--------------- Starting Server ---------------"
cd server
bash start.sh