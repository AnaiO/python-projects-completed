import nmap

scanner = nmap.PortScanner()

print("Welcome")
print("<----------------->")

ip_addr = input("Please enter the ip address you want to scan\n")
print("the ip address scanned is: ", ip_addr)

print("What type of scan do you want to execute: ")
choice = input("""
                  1) SYN SCAN
                  2) UDP SCAN
                  3) Comprehensive scan\n
              """)

print("the scan is: ")

if choice == '1':
  print(scanner.scan(ip_addr, '1-1024', '-v -sS'))
  print("Etat de la connexion: ", scanner[ip_addr].state())
  print("Tous les protocoles: ", scanner[ip_addr].all_protocols())
  print("Etat de la connexion: ", scanner[ip_addr]['tcp'].keys())

elif choice == '2':
  print(scanner.scan(ip_addr, '1-1024', '-v -sS'))

elif choice == '3':
  print(scanner.scan(ip_addr, '1-1024', '-v -sS sV sC -A -O'))

elif choice >= '4':
  print("Please provide a valid choice")

print("Etat de la connexion: ", scanner[ip_addr].state())
print("Tous les protocoles: ", scanner[ip_addr].all_protocols())
print("Liste des ports tcp: ", scanner[ip_addr]['tcp'].keys())