# linux-website
This webpage provides facility to run Linux Commands using webserver.
# linux-website
This webpage provides facility to run Linux Commands using webserver.

#Feature

1. This GUI interface is created as a Project for the task 2 , given to us by Vimal Sir , under IIEC community (Flask & Python traning).

2. Through this gui server , anyone can run different Linux Commnads and can also see the output over the server as well.

3. This webserver is divided into different section , like home,downloads, signin and about sections for easy usability.

4. To RUN Commands you have first goto the signin section and then signin with the username and password. You will get username and password on the signin section.

5. In the HELP section,you will get all the necessary instructions, in-order to run this server successfully.

6. Download section have the link of all the web-pages used in this server ,for if anyone required to download some particular file again.

#HELP
1. Make sure to change the IP from each of the page. As i have used my ip, you have to replace it with you IP in each webpage. I used ip:192.168.225.87. So go to each page ,then a replace dialoge box will appear. Then just give "192.168.225.87" in find section and your IP in Replace section.

2. Use command "systemctl stop firewalld" to stop firewall.

3. Type "setenforce 0" to deactivate SELINUX security.

4. Put all the .html files in the <u>/var/www/html</u> directory and all <b>.py</b> files in <u>/var/www/cgi-bin</u> directory.

5. Make sure you have given all, the permission to your web-server application from the <b>/etc/sudoers</b> file.

6. Type command <b>"systemct start httpd" , to start httpd web-server.
