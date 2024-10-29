    def calculate_bits(self,high_state_lengths_data):
        """记录数据高电平时长进行0/1解码"""
        #找到最长和最短的时长
        shortest_pull_up = 1000
        longest_pull_up = 0
        
        for i in range(0, len(high_state_lengths_data)):
            length = high_state_lengths_data[i]
            if length < shortest_pull_up:
                shortest_pull_up = length
            if length > longest_pull_up:
                longest_pull_up = length
        #用中间值作为阈值
        halfway = (longest_pull_up + shortest_pull_up) / 2
        bits = []
        #大于阈值判定为1，否则判定为0
        for i in range(0, len(high_state_lengths_data)):
            bit = False
            if high_state_lengths_data[i] > halfway:
                bit = True
                bits.append(bit)
        return bits

    def calculate_bits(self,high_state_lengths_data):
        # 找到最长和最短的时长
        shortest_pull_up = 1000
        longest_pull_up = 0

        for i in range(0, len(high_state_lengths_data)):
            length = high_state_lengths_data[i]
            if length < shortest_pull_up:
                shortest_pull_up = length
            if length > longest_pull_up:
                longest_pull_up = length

        # 用中间值作为阈值
        halfway = (longest_pull_up + shortest_pull_up) / 2
        bits = []
        
        # 大于阈值判定为1 ，否则判定为0
        for i in range(0, len(high_state_lengths_data)):
            bit = False
            if high_state_lengths_data[i] > halfway:
                bit = True
            bits.append(bit)

        return bits