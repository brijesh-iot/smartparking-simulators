# Code Repo for RDS Setup and Device Simulator scripts

#### Useful GitHub commands

```bash
git clone git@github.com:awssmartparking/edge-repo.git

git init
git add -A
git commit -m "Initial Load"
git remote add origin git@github.com-awssmartparking:awssmartparking/edge-repo.git
git push -u origin master
```

#### Useful commands

```bash
npm init
npm install mysql
```

#### Install MySQL tools on Ubuntu

```bash
# To install MySQL Client
--------------------------------------------------------------------------------------------------------
sudo apt-get install mysql-client

# To connect remote database
--------------------------------------------------------------------------------------------------------
mysql -u admin -h __hostname__ --port 3306 --password 

# Common Database commands
--------------------------------------------------------------------------------------------------------
show databases;
show tables;
create schema __database__;
commit;

# To install MySQL Server 
--------------------------------------------------------------------------------------------------------
sudo apt-get install mysql\*
```

#### Login to private EC2 using SSM

```bash
aws ssm start-session --target i-025ebfb13a4627739 --document-name AWS-StartPortForwardingSession --parameters "portNumber"=["22"],"localPortNumber"=["9989"] --region us-east-1 --profile __awsprofile__
```

#### How to access Database/RDS which is in not publicly accessible.

- First login to any EC2 using ssh directly if on public ip address.
  If EC2 is on private ip address then use SSM to login to EC2.
- After you get connection to EC2, setup putty using the above forwarded port (localPortNumber in SSM)
  1. Open Putty
  2. Session -> Host Name : localhost, Port: 9989
  3. SSH -> Auth -> Private key file
  4. SSH -> Tunnels -> Source port: 127.0.0.5:6000, Destination: smartparking.cfxumdhjfp62.us-east-1.rds.amazonaws.com:3306
  5. Open MySQL client and connect with 127.0.0.6:6000
  
  
#### Run Simulation scripts 

- First we need to copy cert.pem and private.key from S3 bucket to simulator python scripts directory
  ( You can delete the existing .pem & .key file and use -- sudo vi cert.pem )
  
```bash
sudo vi cert.pem
sudo vi private.key

python 1-DeviceRgistration.py

```  

#### Note

- Make sure you provide the proper value of CoreName in smartparking-iot-core-repo -> configuration.json (Same value provided in CloudFormation Template)
- Modify file smartparking-iot-core-repo -> alerts -> mysqlconfig.json
- Modify file smartparking-iot-core-repo -> device-register -> config.json
- Modify file smartparking-iot-core-repo -> device-status -> config.json
- Find and execute database scripts from smartparking-iot-core-repo -> dbscript.txt
