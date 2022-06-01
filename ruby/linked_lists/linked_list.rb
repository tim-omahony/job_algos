require './linked_list_node'

class LinkedList
    attr_accessor :head
    
    # initialize will initialize the data members of LinkedList
    def initialize(param=nil)
        @head = param
    end

    # insert_at_head method will insert an integer element at head of a linked list.
    def insert_at_head(data)
        insert_node_at_head(LinkedListNode.new(data))
    end

    # insert_node_at_head method will insert a LinkedListNode at head of a linked list.
    def insert_node_at_head(node)
        if @head
            node.next = @head
            @head = node    
        else
            @head = node
        end
    end

    # insert_at_tail method will insert an integer element at tail of a linked list.
    def insert_at_tail(data)
        insert_node_at_tail(LinkedListNode.new(data))
    end

    # insert_node_at_tail method will insert a LinkedListNode at tail of a linked list.
    def insert_node_at_tail(node)
        if @head
            temp = @head
            temp = temp.next while temp.next 
            temp.next = node    
        else
            @head = node
        end
    end
    # create_linked_list method will create the linked list using the given 
    # integer array with the help of InsertAthead method. 
    def create_linked_list(lst)
        list_head = nil
        lst.reverse.each { |x| list_head = insert_at_head(x) }
    end
    # display_linkedlist method will display the elements of linked list.
    def display_linkedlist()
        print "["
        temp = @head
        while temp
            print temp.data.to_s
            temp = temp.next
            print ", " if temp
        end
        print "]"
    end
end