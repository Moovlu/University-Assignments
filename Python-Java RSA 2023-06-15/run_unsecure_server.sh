echo "--------------- Moving File ---------------"
cp ELCI-1.12.1.jar server/plugins

echo "--------------- Starting Server ---------------"
cd server
bash start.sh