# # /*
# # UserPingsPerFrequency
# # When booting the Intercom messenger on any website we make a request to the "ping" endpoint with the user credentials. We want to analyse the number of requests per user to this endpoint in select periods of time. These periods are partitioned into smaller chunks based on a certain frequency (minute/hour/day).
# # 
# # You have to design and implement the following API:
# # Class: PingFrequency
# # Function: void recordPing(<string> userId, <integer> Time)
# # Function: List<Integer> getUserPingsPerFrequency(<string> userId, <string> freq, <integer> startTime, <integer> endTime)
# # 
# # Example:
# # 
# # [user_id, timestamp(seconds)]
# # """
# # ["user_1", 5]
# # ["user_2", 15]
# # ["user_2", 20]
# # ["user_1", 90]
# # ["user_3", 100]
# # ["user_1", 110]
# # ["user_3", 120]
# # ["user_3", 170]
# # ["user_2", 2500]
# # ["user_3", 3600]
# # ["user_3", 3800]
# # """
# # INPUT - getUserPingsPerFrequency("user_1", "minute", 0, 150)
# # OUTPUT - [1, 2, 0]
# # Explanation: This is partitioned into [0-59, 60-119, 120-150] => Within the 0-59 window, the user pinged once, and within the 60-119 window, the user pinged twice in that window. They made no request in the last window, leading to final result of: [1, 2, 0]
# # 
# # INPUT - getUserPingsPerFrequency("user_3", "hour", 10, 4000)
# # OUTPUT - [4, 1]
# # Explanation: This is partitioned into [10-3609, 3610-4000] => Within the 10-3609 window, the user pinged 4 times, and within the 3610-400 window, they made pinged once, leading to the final result of: [4, 1]
# # 
# #  */
# 

## Ruby solution
# class PingFrequency
#   attr_accessor(:pings)

#   def initialize
#     @pings = Hash.new {|h, k| h[k] = [] }
#   end

#   def read_ping(ping)
#     @pings[ping[0]] << ping[1]
#   end

#   def get_ping_frequency(user_id, frequency, start_time, end_time)
#     user_pings = @pings[user_id]
#     freq = frequency_map[frequency]
#     windows = Array.new((end_time % freq) / 10, 0)
#     user_pings.each do |ping|
#       idx = (ping - start_time) / freq
#       windows[idx] += 1 unless idx > windows.size
#     end
#     windows
#   end

#   private

#   def frequency_map
#     { 'hour' => 3600, 'minute' => 60, 'second' => 1 }
#   end
# end

# pf = PingFrequency.new
# pf.read_ping(["user_1", 5])
# pf.read_ping(["user_2", 15])
# pf.read_ping(["user_2", 20])
# pf.read_ping(["user_1", 90])
# pf.read_ping(["user_3", 100])
# pf.read_ping(["user_1", 110])
# pf.read_ping(["user_3", 120])
# pf.read_ping(["user_3", 170])
# pf.read_ping(["user_2", 2500])
# pf.read_ping(["user_3", 3600])
# pf.read_ping(["user_3", 3800])

# p pf.get_ping_frequency("user_2", "minute", 0, 150)
