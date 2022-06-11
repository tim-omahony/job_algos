class LinkedListNode
  attr_accessor :data, :next, :arbitrary
  
  def initialize(data)
    @data = data
    @next = nil
    @arbitrary = nil
  end
end