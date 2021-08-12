import paramiko
import time
import getpass


username = input("Username:") or "v_rono"
password = getpass.getpass() or "router_1"
 
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for x in range(1,6):
    ssh_client.connect(hostname=f"10.10.10.{x}", username=username, password=password)

    print(f"Success login to 10.10.10.{x}")
    conn = ssh_client.invoke_shell()

    conn.send("conf t\n")
    conn.send("int lo0\n")
    conn.send(f"ip add 10.1.1.{x} 255.255.255.255\n")
    time.sleep(1)

    output = conn.recv(65535).decode()
    print(output)

    ssh_client.close()

#run python3 paramiko_router.py in the ubuntu server
#configuring multiple routers at once