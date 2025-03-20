from gen_py.superNode.SuperNode import Client  # Correct import for superNode
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
import sys
def main():
    transport = TSocket.TSocket("128.101.34.26", 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Client(protocol)

    transport.open()  # Connect to the server

    port_number = int(sys.argv[1]) # Dummy port for now from the command line to show it works and stores the port 
    join_id = client.request_join(port_number)
    print(f"Join Request ID: {join_id}")


    success = client.confirm_join() # Confirming join
    print(f"Join Confirmed: {success}")

    selected_node = client.get_node() # Getting the Random IP and Port
    print(f"Randomly Selected Node: {selected_node}")

    transport.close()  # Close connection

if __name__ == "__main__":
    main()
