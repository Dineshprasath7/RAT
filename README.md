Windows RAT
A feature-rich Remote Access Trojan (RAT) designed for Windows systems, enabling comprehensive remote system control and monitoring. This RAT allows users to perform various system, shell, network, keylogging, video, and file management operations remotely.

Features
System Commands
help: Display all available commands.
writein <text>: Write text to the currently opened window.
browser <query>: Open a browser and enter a query.
drives: List all drives of the PC.
cpu_cores: Display the number of CPU cores.
systeminfo (extended): Show detailed system information via cmd.
tasklist: List all system tasks.
localtime: Display the current system time.
curpid: Get the PID of the client's process.
setwallpaper <path>: Set the desktop wallpaper.
exit: Terminate the RAT session.
Shell Commands
pwd: Get the current working directory.
cd <directory>: Change directory.
cd ..: Move up one directory.
dir: List all files in the current directory.
abspath <file>: Get the absolute path of a file.
Network Commands
ipconfig: Display local IP address.
portscan: Perform a port scan on the target machine.
profiles: List all network profiles.
Keylogger Commands
keyscan_start: Start the keylogger.
send_logs: Send captured keystrokes.
stop_keylogger: Stop the keylogger.
Video Commands
screenshare: Start screen sharing of the remote PC.
breakstream: Stop the screen sharing stream.
screenshot: Capture a screenshot of the remote PC.
webcam_snap: Capture a photo using the remote webcam.
File Management Commands
delfile <file>: Delete a file.
editfile <file> <text>: Edit a file by adding text.
createfile <file>: Create a new file.
download <file> <homedir>: Download a file from the remote PC.
upload <file> <path>: Upload a file to the remote PC.
cp <file1> <file2>: Copy a file.
mv <file> <path>: Move a file to a new location.
mkdir <dirname>: Create a new directory.
rmdir <dirname>: Remove a directory.
readfile <file>: Read and display the content of a file.
How to Use
Installation: Deploy the RAT on the target Windows machine.
Running: Start the RAT to initiate a remote session.
Commands: Use the available commands to control and monitor the target system remotely.
