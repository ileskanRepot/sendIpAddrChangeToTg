import asyncio
from sendTGMsg import sendIP
from getIP import hasIpChanged

def main():
    ip = hasIpChanged()
    if ip is not None:
        asyncio.run(sendIP(ip))

if __name__ == "__main__":
    main()
