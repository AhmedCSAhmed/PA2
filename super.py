import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "gen_py"))

from gen_py.superNode.SuperNode import Processor  # Correct import for superNode
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from gen_py.superNode.ttypes import NodeTuple
import random



class superNodeHandler:
    def __init__(self):
        self.activeNodes = []
        self.records = []
        self.port = None
        self.maxNodes = 10
        self.pendingJoin = None
        self.ip = 'csel-kh1260-03.cselabs.umn.edu' # hard coded this for now i need to set the port dymaically in the confirm_join by refrencing the compute.txt
        
        # Spin up diffferent machine in it currently works
    
    def request_join(self, portNum):
        # Need to cross refecne portNum with compute.txt in here and check before hand if the portNum is stored there and take that IP and store it as well
        try:
            if self.pendingJoin == None and self.maxNodes >= 1:
                self.maxNodes-=1
                self.pendingJoin = self.maxNodes
                self.port = portNum       
                print("REQUESTING TO JOIN!!!")
                return self.pendingJoin
            
        except:
            print("ERROR CANNOT REQUEST TO JOIN PENDING NODE IN PROGRESS")
            return -1 # On failure the key is -1 always check this
    
    
    
    # GOAL OF THIS FUNCTION IS TO ADD THE IP AND PORT TO THE ADDRESS LIST 
    def confirm_join(self):
        # Should only call this function in Compute when All nodes in the Chord network have had 
        # all existing nodes have had their finger tables, predecessors, and successors updated
   
        if self.pendingJoin is not None:
            self.activeNodes.append(self.pendingJoin)
            self.pendingJoin = None
            self.records.append((self.port, self.ip))
            self.port = None
            print("SUCUESS PENDING NODE JOINED!!")
            return True
        
        else:
            print("ERROR Pending Node could not join ")
            return False
    
    

    def get_node(self):
        # THIS RETURNS THE IP AND THE PORT OF AN ACTIVE COMPUTE NODE
        
        # This function only needs to be called once by each node and client instance.
        
        
        
        # I need change this to a try / except block
        if len(self.activeNodes) == 0:
            return KeyError("ERROR NO ACTIVE NODES")
        randomNode = random.randint(0, len(self.records)-1)
        tp1 = self.records[randomNode]
        return NodeTuple(ip=tp1[1], portNum=tp1[0])
        
        
    
            
if __name__ == '__main__':
    handler = superNodeHandler()
    processor = Processor(handler)
    transport = TSocket.TServerSocket(host="0.0.0.0", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)    
    print("Starting the SuperNode Thrift server on port 9090...")
    server.serve()
    print("DYING")

   
        
        
        
        
        
    
    
    
    