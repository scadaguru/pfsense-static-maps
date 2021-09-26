# pfsense bulk import DHCP entries for static IP assignments:


# What it does?
A Python script that will read static-ips.csv file and will generate static-map.xml file to be imported in to pfsense vis GUI so pfsense will have static DHCP reservation for all your devices listed in csv file. 

# Update static-ips.csv file
Update default static-ips.csv with your information mentioned below:
Note: hostname can be empty if you don't want it

| MAC | IP  | Description | Hostname |
| --- | --- | --- | --- |
| 41:41:41:41:41:41 | 192.168.1.1 | pfsense-box | |
| 42:42:42:42:42:42 | 192.168.1.2 | USW-Flex-Mini-Main | |
| 43:43:43:43:43:43 | 192.168.1.10 | omv-nas | omv.local |
| 44:44:44:44:44:44 | 192.168.1.100 | win10-pc | devpc.local | 
| 45:45:45:45:45:45 | 192.168.1.101 | ubunti-ha | ubuntu.ha | 

Please make sure to remove all default data that I have shown for example only and leave first line which has header

Please make to have correct MAC address, IP address is in the range of your interface configuration and hostname shouldn't have space or any special character!

Please make sure that csv file should not have any formatting except comma seperator, if you want you can have extra blank line(s) in-between for more redability/grouping


# How to import devices to have static IPs?
1. Make sure you have python (>3) has installed
2. Copy all files from this repo or clone it
3. Update static-ips.csv file with your devices details
4. Run command like this:
    ~~~
    python main.py
5. It will create a new file called static-map.xml which will look like this: (Note: This file has minimal information to create static IP entry in pfsense and I have verified it works!)
    ~~~
    <staticmap><mac>41:41:41:41:41:41</mac><ipaddr>192.168.1.1</ipaddr><hostname></hostname><descr><![CDATA[pfsense-wan]]></descr></staticmap><staticmap><mac>42:42:42:42:42:42</mac><ipaddr>192.168.1.2</ipaddr><hostname></hostname><descr><![CDATA[USW-Flex-Mini-Main]]></descr></staticmap><staticmap><mac>43:43:43:43:43:43</mac><ipaddr>192.168.1.10</ipaddr><hostname>omv.local</hostname><descr><![CDATA[omv-nas]]></descr></staticmap><staticmap><mac>44:44:44:44:44:44</mac><ipaddr>192.168.1.100</ipaddr><hostname>devpc.local</hostname><descr><![CDATA[win10-pc]]></descr></staticmap>
6. Now goto pfsense GUI and from the menu Diagnostic select "Backup and Restore" option. From "Backup configuration" section clickn on "Download configuration as xml" button and select the location where you want to copy that file and call it pfsense-dhcp.xml
7. a. Using some editor like notepad++ open that pfsense-dhcp.xml file and search for "staticmap". Now delete all "staticmap" entries 
b. Open python script generated file called "static-map.xml" in editor and select everything from that file and copy to clipboard
c. Goto pfsense-dhcp.xml and paste where you delete all "staticmap" entries and save the file pfsense-dhcp.xml
8. Go back to pfsense GUI and from the menu Diagnostic select "Backup and Restore" and this time from "Resotre Backup" section select <span style="color:red">**"DHCP Server"**</span>. and choose file name "pfsense-dhcp.xml" and click "Restore Configuration"
9. You may have to restart pfsense and then go to menu Status and select "DHCP Leases" option and that should have all your static DHCP device you provided in the static-ips.xml file
