struct tuple {
    1: string ip,
    2: i32 portNum,
}

struct Weights {
    1: list<list<double>> W,
    2: list<list<double>> V,
    3: bool error
}

service Compute{
    oneway void put_data(1:string filename),
    Weights get_model(1:string filename),
    void fix_fingers(),
    void print_info(),
    i32 nearest_Node(1:i32 key)
}