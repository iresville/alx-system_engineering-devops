echo "Backing up Master Server 251279-web-01	ubuntu	100.25.190.203"
scp -r ubuntu@100.25.190.203:~/apache2 ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/
scp -r ubuntu@100.25.190.203:~/docker ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/
scp -r ubuntu@100.25.190.203:~/nginx ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/
scp -r ubuntu@100.25.190.203:~/sql ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/
scp -r ubuntu@100.25.190.203:~/deploy_webstatic ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/
scp -r ubuntu@100.25.190.203:~/firewall ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/
scp -r ubuntu@100.25.190.203:~/puppet ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/
scp ubuntu@100.25.190.203:~/start_services.sh ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-01/

echo "Done!"

# =====================================================================================================================================

echo "Backing up Serve 2 251279-web-02	ubuntu	54.175.134.168"
scp -r ubuntu@54.175.134.168:~/apache2 ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/
scp -r ubuntu@54.175.134.168:~/docker ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/
scp -r ubuntu@54.175.134.168:~/nginx ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/
scp -r ubuntu@54.175.134.168:~/sql ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/
scp -r ubuntu@54.175.134.168:~/deploy_webstatic ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/
scp -r ubuntu@54.175.134.168:~/firewall ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/
scp -r ubuntu@54.175.134.168:~/puppet ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/
scp ubuntu@54.175.134.168:~/start_services.sh ~/Desktop/alx-system_engineering-devops/server_recovery/server-web-02/

echo "Done!"

# =====================================================================================================================================

echo "Backing up Load Balancer Server 251279-lb-01	ubuntu	52.205.100.118"
scp -r ubuntu@52.205.100.118:~/0-custom_http_response_header ~/Desktop/alx-system_engineering-devops/server_recovery/server-lb-01/
scp -r ubuntu@52.205.100.118:~/1-install_load_balancer_HAproxy ~/Desktop/alx-system_engineering-devops/server_recovery/server-lb-01/
scp -r ubuntu@52.205.100.118:~/ssl ~/Desktop/alx-system_engineering-devops/server_recovery/server-lb-01/

echo "Done!"
