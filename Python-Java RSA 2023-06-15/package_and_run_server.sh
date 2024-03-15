echo "--------------- Packaging new .jar file ---------------"
(cd ELCI-master && mvn package)

echo "--------------- Moving File ---------------"
mv ELCI-master/target/ELCI-1.12.1.jar server/plugins

echo "--------------- Starting Server ---------------"
cd server
bash start.sh