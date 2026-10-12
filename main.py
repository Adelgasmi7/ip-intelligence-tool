import ipaddress
import requests

def display_report(ip_data):
    print("\n" + "=" * 38)
    print("       IP INTELLIGENCE REPORT")
    print("=" * 38) 
    
    print(f"{'IP Address':<15} {ip_data.get("ip")}")
    print(f"{'Country':<15} {ip_data.get("country")}")
    print(f"{'City':<15} {ip_data.get("city")}")
    print(f"{'ISP':<15} {ip_data["connection"]["isp"]}")
    print(f"{'ASN':<15} {ip_data["connection"]["asn"]}")
    
    print()
    print("Lookup Status: SUCCESS")
    print("=" * 38) 

def lookup_ip(ip_addr):
    response= requests.get(f"https://ipwho.is/{ip_addr}",
            timeout=10)
    response.raise_for_status()
    result = response.json()
    return result


ip_addr= input("Enter the IP address: ")

try:
    ipaddress.ip_address(ip_addr)

    ip_data = lookup_ip(ip_addr)

    if ip_data["success"]:
      display_report(ip_data)   
    else:
        print ("Lookup failed")
    
except ValueError as e:
    print(f"Invalid IP address {e}")

except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")