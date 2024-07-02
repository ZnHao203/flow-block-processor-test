import os
import sys
import signal
import json
import time
import threading

from bc_classes import PendingBlockArray, BlockChain, PendingBlock

# lock = threading.Lock() # use a lock for any function calls that modifies an array
"""
There are two major arrays - block_array and pending_block_array.
Block_array contains the id of all accepted blocks, sorted in consequtive view orders. 
Pending_block_array has the received blocks that are not accepted. 
They could be (1)not voted or (2) voted but waiting for all blocks with a smaller view to be accepted.
"""
pending_block_array = PendingBlockArray()
block_array = BlockChain()

# update blockchain, and output accepted block info      
def accept_block(id, view):
    # global lock

    # only accept blocks with unique id
    accepted = block_array.accept_new_block(id, view)
        
    if accepted:
        print("NEW BLOCK ACCEPTED: id {}, view {}".format(id, view))

# add a new pending block
def add_pending_block(id, view):
    # global lock

    pending_block = PendingBlock(id, view)

    # with lock:
        # print("got lock add_pending_block")
    pending_block_array.append(pending_block)
    # print("return lock add_pending_block")

# process a new vote and adds all possible pending blocks to the blockchain
def process_vote(id):
    # print("process_vote", id)
    # global lock

    # with lock:
    # print("got lock process_vote")

    pending_block_array.process_vote(id)

    while (True):
        next_view = block_array.get_next_view()
        # print("next view expected is ", next_view)

        block = pending_block_array.check_blockchain_addition(next_view)

        # print(block)
        if block != "":
            accept_block(block.id, block.view)
            # print("found one")
        else:
            # print("done")
            break
    # print("return lock process_vote")
    

