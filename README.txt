P2P FILE SHARING PROJECT
-----------------------------------
P2P File Sharing Project using Python from Zeynep Babür, Şevval Çolak, Esranur Aygün; BAU
This program is a basic Bittorent application. Program has 4 parts : Announcement, Discovery, Upload and Download.
-----------------------------------
Step1 : Discovery and Announcement
1) A shared network connection is a must
2) Run announcement.py to announce the contents that you have
3) Run discovery.py to discover other users' contents
    - A file thats name is 'MyFile' should've appear and the contents that other user announce should be written in that file
-----------------------------------
Step2 : Upload and Download
1) Run uploader.py to upload content to other users

A - Uploading a content
While uploader.py is running, other user should request a content
    - uploader.py should get the content from chunks folder and send to the user
	- For all of the successfully uploaded chunks(can be checked from 'chunks' folder), there should be an entry in 'History' file.

B - Downloading a content  
Run downloader.py to download content from other users
    - Enter a content name to be downloaded from other users
    - downloader.py should detect the users which have the content. 
    - downloader.py should successfully download the wanted content unless there is an unexpected situation.
	- If some parts of downloaded content(chunk) is missing, an error message should be shown and there shouldn't be a png file of that content
	- For all of the successfully downloaded chunks(can be checked from 'chunks' folder), there should be a entry in 'History' file.

