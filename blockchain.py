import array

# global variable definition
# block_chain = []
# next_view = 0



class Block:
    def __init__(self, id, view):
        self.id = str(id)
        self.view = int(view)

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
        self.block_chain.append(Block(id, view))
        self.next_view += 1
    
    def get_next_view(self):
        return self.next_view
    

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
        index = 0
        length = len(self.pending_blocks)
        while index < length:
            if self.pending_blocks[index].id == block_id:
                self.pending_blocks[index].voted = True
                print("updated index")
                return
            index += 1
        print("vote id not exist")
            
    
    # accept all blocks that satisfies the condition
    def check_blockchain_addition(self, next_view):
        if (self.len_pending_blocks > 0 and \
                self.pending_blocks[0].view == next_view):
            block = self.pending_blocks[0]
            self.pending_blocks.pop(0)
            self.len_pending_blocks -= 1
            print("this part is reached")
            return block
        return ""

pending_block_array = PendingBlockArray()
block_array = BlockChain()

# update blockchain, and output accepted block info      
def accept_block(id, view):
    block_array.accept_new_block(id, view)
    print("NEW BLOCK ACCEPTED: id {}, view {}".format(id, view))

# add a new pending block
def add_pending_block(id, view):
    pending_block = PendingBlock(id, view)
    pending_block_array.append(pending_block)

# process a new vote and adds all possible pending blocks to the blockchain
def process_vote(id):
    print("process_vote", id)
    pending_block_array.process_vote(id)
    while (True):
        next_view = block_array.get_next_view()
        print("next view expected is ", next_view)
        block = pending_block_array.check_blockchain_addition(next_view)
        print(block)
        if block != "":
            accept_block(block.id, block.view)
            print("found one")
        else:
            print("done")
            break

