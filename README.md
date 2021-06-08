# linux-website
This webpage provides facility to run Linux Commands using webserver.
# linux-website
This webpage provides facility to run Linux Commands using webserver.

#Feature

1. This GUI interface is created as a Project for the task 2 , given to us by Vimal Sir , under IIEC community (Flask & Python traning).

2. Through this gui server , anyone can run different Linux Commnads and can also see the output over the server as well.

3. This webserver is divided into different section , like home,downloads, signin and about sections for easy usability.
#Updates: Now 'signup' option is also available in the sigin page. Create your own userName and Password and use that to login.

4. To RUN Commands you have first goto the signin section and then signin with the username and password.
#Updates: Now there a  Terminal like interface is added run the command. Simply signin then you will a terminal icon on the top right corner. Click that icon to open terminal interface.

5. In the HELP section,you will get all the necessary instructions, in-order to run this server successfully.

6. Download section have the link of all the web-pages used in this server ,for if anyone required to download some particular file again.

#HELP
1. Since in the last update where you have to change/put your IP Address in each webpage ,in this update you only have to change/put your system IP Address at two location:
	a. htmldoc > ipaddr.js
	b. cgi-bin > ipaddr.txt

2. Use command "systemctl stop firewalld" to stop firewall.

3. Type "setenforce 0" to deactivate SELINUX security.

4. Put all the files from 'httpdoc' folder in the <u>/var/www/html</u> directory and all files from <b>cgi-bin</b> folder to <u>/var/www/cgi-bin</u> directory.<br>
Since i am using <b>httpd Apache Server</b>, so the location where to put all these files may vary depending on the server which you are using.

5. Make sure you have given all, the permission to your web-server application from the <b>/etc/sudoers</b> file.

6. Type command <b>"systemct start httpd" , to start httpd web-server.
