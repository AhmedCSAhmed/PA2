struct NodeTuple {
    1: string ip,
    2: i32 portNum 
}


service SuperNode{
    i32 request_join(1:i32 portNum),
    bool confirm_join(),
    NodeTuple get_node()
}