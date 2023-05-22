### Converting .pem key to .ppk for Linux Machine 
*Remember to change the .pem KeyPair to .ppk*
- To convert the private key to standard PEM format, type the following command 
		$ puttygen privatekey.ppk -O private-openssh -o privatekey.pem
		puttygen privatekey.ppk -O private-openssh -o privatekey.pem
		puttygen privatekey.pem -O private-openssh -o privatekey.ppk
- Access via the EC2 Instance Connect
- Access via PuTTY (SSH), use the public IP address
