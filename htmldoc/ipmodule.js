import {ip} from './ipaddr.js';
	document.getElementById('xip').innerText = ip;
	var anchore = document.getElementsByTagName('a');
	anchore[0].href = 'http://'+ip;
	anchore[1].href = 'http://'+ip+'/downloads.html';
	anchore[2].href = 'http://'+ip+'/login.html';
	anchore[3].href = 'http://'+ip+'/help.html';
	anchore[4].href = 'http://'+ip+'/about.html';

 
