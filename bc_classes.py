class PendingBlock:
    def __init__(self, id, view):
        self.id = str(id)
        self.view = int(view)
        self.voted = False
        
class BlockChain:
    def __init__(self):
        self.block_chain = []
        self.next_view = 1 # positive integer

    def accept_new_block(self, id, view):
        # only add a new block if its id is unique
        if view != self.next_view:
            return False
        if id in self.block_chain:
            return False
        self.block_chain.append(id)
        self.next_view += 1
        return True
    
    def get_next_view(self):
        return self.next_view
    
    # def check_repeat_id(self, id):
    #     print(id in self.block_chain)
    #     return id in self.block_chain
    

class PendingBlockArray:
    def __init__(self):
        self.pending_blocks = []
        self.len_pending_blocks = 0

    def append(self, block):
        if isinstance(block, PendingBlock):
            # Find the correct position to insert the new pending block to keep the list sorted
            index = self._find_insertion_index(block)
            self.pending_blocks.insert(index, block)
            self.len_pending_blocks += 1
        else:
            raise TypeError("Only block instances can be appended")

    def _find_insertion_index(self, block):
        """Uses binary search to find the insertion index for the new block."""
        low, high = 0, self.len_pending_blocks
        while low < high:
            mid = (low + high) // 2
            if self.pending_blocks[mid].view < block.view:
                low = mid + 1
            else:
                high = mid
        return low

    def process_vote(self, block_id):
        # Find the index for the block_id
        # Mark that block as voted
        # ignore invalid votes
        # if there are blocks with identical ids in the array
        #   just vote the one with min view
        index = 0
        length = len(self.pending_blocks)
        while index < length:
            if self.pending_blocks[index].id == block_id:
                self.pending_blocks[index].voted = True
                # print("updated index")
                return
            index += 1
        # print("vote id not exist")
            
    
    # accept all blocks that satisfies the condition
    def check_blockchain_addition(self, next_view):
        if (self.len_pending_blocks > 0 and \
                self.pending_blocks[0].view == next_view):
            block = self.pending_blocks[0]
            self.pending_blocks.pop(0)
            self.len_pending_blocks -= 1
            # print("this part is reached")
            return block
        return ""