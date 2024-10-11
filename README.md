## AWS Credentials Finder (Windows)

This **NetExec** module is designed to search for files named **"credentials"** on remote servers running **Windows**. It is ideal for locating AWS configuration files in security environments, allowing quick identification of the paths where these critical files are stored.

### Features:
- Scans Windows servers for files named `credentials`.
- Returns the full paths of the files found on the remote system.
- Perfect for security audits and penetration testing focused on AWS configuration.

### Installation
```bash
git clone https://github.com/dev-fortress/aws-credentials.git  
```

```bash
cd aws-credentials  
```

```bash
cp aws-credentials.py /usr/lib/python3/dist-packages/nxc/modules/  
```

### Usage:
1. NetExec winrm IP-Address -u username -p password -M aws-credentials
2. NetExec winrm IP-Address -u username -p password -M aws-credentials -o SEARCH_PATH=C:\\Users\\username\\pruebas\\
3. Review the returned paths to analyze the files found.

## Additional Resources
- [Docs NetExec](https://github.com/Pennyw0rth/NetExec)

## License
This project is licensed under the MIT License. For more information, see the file. [LICENSE](LICENSE). 
