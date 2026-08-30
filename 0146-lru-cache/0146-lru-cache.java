class LRUCache {
    class Node{
        int key;
        int value;
        Node(int key,int value){
            this.key=key;
            this.value=value;
        }
    }
    int capacity;
    ArrayList<Node> cache;
    public LRUCache(int capacity) {
        this.capacity=capacity;
        cache=new ArrayList<>();
    }
    
    public int get(int key) {
        for(int i=0;i<cache.size();i++){
            if(cache.get(i).key==key){
                Node node=cache.remove(i);
                cache.add(0,node);
                return node.value;
            }
        }
        return -1;
        
    }
    
    public void put(int key, int value) {
        for(int i=0;i<cache.size();i++){
            if(cache.get(i).key==key){
                Node node=cache.remove(i);
                node.value=value;
                cache.add(0,node);
                return;
            }
        }
        Node node=new Node(key,value);
        cache.add(0,node);
        if(cache.size()>capacity){
            cache.remove(cache.size()-1);
        }

        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */