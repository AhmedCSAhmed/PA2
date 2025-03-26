import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "gen_py"))

from gen_py.compute import Compute 
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer 


class ComputeHandler:
    """
    Assuming that Finger Table is already implemented 
    """
    def __init__(self):
        pass
    
    
    def put_data(self, filename): 
        pass
    
    
    def get_model(self, filename):
        pass
    
    
    def fix_fingers(self):
        """
        Need to use Key + 2 ^(i-1) % the Ring to recompute the start node for each 
        
        On each fingerTabke recompute the ith fingertables Start posotion then find where the start key is in the 
        Chord and Grab it then store it's info inside of the new recomputed entry
        
        
        M is equal to the number of bits used to define the size of the key space Which needs to be used when fixing each i'th finger for the local node 
                
        """            
        pass
     
       
    def print_info(self):
        pass 
    
    
    
    """ 
    Helper I defined in the Thrift file may not need 
    """
    
    def print_info(self):
        pass
     
    
    


def main():
    # transport = TSocket.TSocket("128.101.34.26", 9090)
    # transport = TTransport.TBufferedTransport(transport)
    # protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # client = Client(protocol)

    # transport.open()  # Connect to the server

    # # port_number = int(sys.argv[1]) # Dummy port for now from the command line to show it works and stores the port 
    # join_id = client.request_join(9091)
    # print(f"Join Request ID: {join_id}")


    # success = client.confirm_join() # Confirming join
    # print(f"Join Confirmed: {success}")

    # selected_node = client.get_node() # Getting the Random IP and Port
    # print(f"Randomly Selected Node\nIP: {selected_node.ip}\nport: {selected_node.portNum}")

    # transport.close()  # Close connection
    pass

if __name__ == "__main__":
    main()
