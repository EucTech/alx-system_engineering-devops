# Secure File Transfer Protocol (SFTP)

### Secure File Transfer Protocol (SFTP) is a network protocol for securely accessing, transferring and managing large files and sensitive data.


## How to use SFTP

1. open a command line terminal
2. type sftp "username@hostname"

## Example:
```sftp 407939ef5a69@407939ef5a.09417.alxcode```

## sftp commands

1. ls - lists the files in remote directory
2. lls - lists the files in your local machine
3. pwd - prints the remote server working directory
4. lpwd - prints the local working directory
5. cd - changes the remote working directory
6. lcd - changes directory in your local mechine
7. put - put is used to upload files from local mechine to remote server

```put filename```

8. mput - mput is used to upload multiple files from local mechine to remote server

### Example upload all files that ends with .txt from local mechine to remote server

```mput *.txt```

9. get - get is used to download files from remote server to local mechine
```get filename```

10. mget - mget is used to download multiple files from remote server to local mechine

### Example download all files that ends with .txt from remote server to local mechine

```mget *.txt```
