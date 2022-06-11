require './linked_list'

def reverse(head)
    # no need to reverse if head is null 
    # or there is only 1 node.
    return head if !head or !head.next 
  
    # Initializing 'list_to_do' marker
    list_to_do = head.next
  
    # Initializing 'reversed_list' marker which is already pointed at head
    reversed_list = head
    reversed_list.next = nil
    
    # Reversing the list
    while list_to_do 
      temp = list_to_do
      list_to_do = list_to_do.next
      
      # Set the current node (temp) as the head of the reversed list
      temp.next = reversed_list
      reversed_list = temp
    end
  
    return reversed_list
end


# Main

v = [[29, 23, 82, 11, 4, 3, 21], [59, 7, -3, 21, 14, 30, 120]]

v.length.times do |i|
  obj1 = LinkedList.new()
  # The CreateLinkedList function will convert our vector to a Linked list
  list_head_1 = obj1.create_linked_list(v[i])
  # Displaying original linked list
  print (i + 1).to_s, ". Unsorted list:\t"
  obj1.display_linkedlist()
  # Reversing the created linked list
  obj2 = LinkedList.new()
  obj2.head = reverse(obj1.head)
  print "\n   Reversed list:\t"
  # Displaying modified  reversed linked list
  obj2.display_linkedlist()
  print "\n-------------------------------------------------------------------------------------------------------\n"
end