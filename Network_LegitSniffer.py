from scapy.all import sniff


def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        proto = packet["IP"].proto

        output = f"[SCAPY-CAPTURE] Proto: {proto} | {src_ip} -> {dst_ip}"
        print(f"\033[92m{output}\033[0m")


def main():
    print("--- KIRA SCAPY SNIFFER ACTIVE ---")
    print("--- Press CTRL+C to stop ---")

    try:
        sniff(prn=packet_callback, store=0)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()