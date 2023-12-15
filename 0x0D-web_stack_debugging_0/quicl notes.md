# QuIcK nOtEs

### 1. Understanding of Web Stack

- A web stack consists of an operating system, web server (e.g., Nginx, Apache), database (e.g., MySQL), and a programming language (e.g., PHP, Python).
- These components work together to serve web pages to users.

### 4. Linux File System and Permissions

- `/etc`: Configuration files for system and applications.
- `/tmp`: Temporary files, cleared on reboot.
- `/var/log`: Log files for various system and application services.
- Use `chmod` to change file permissions and `chown` to change ownership.

### 6. Debugging Tools

- `curl`: Command-line tool for making HTTP requests. Useful for testing web servers.
- Example: `curl http://localhost:80` to test if a web server is running on port 80.

### 7. Networking Basics

- Ports: Communication endpoints for processes. HTTP usually runs on port 80, HTTPS on 443.
- IP Addresses: Unique addresses for devices on a network.
- Basic Commands: `ifconfig` for network interfaces, `netstat` for network connections, `ping` to test connectivity.

### 8. Logs

- Located in `/var/log/`.
- `tail -f /var/log/nginx/error.log` to follow Nginx error logs in real-time.
- Use `grep` to search for specific terms in log files.

These notes give a quick reference for each topic.

# STEPS

---

1. Run the Docker Container
2. List Running Containers
3. Connect to the Docker Container
4. **Install Apache**
5. Check Apache Status
6. Verify Apache Configuration
7. Ensure Web Root Contains Correct File
8. Test Apache Locally Inside Container
9. Exit the Docker Container
10. Test Apache from Host Machine
11. Document the Commands
