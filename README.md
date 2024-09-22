# flow-block-processor-test
<p> This is a demonstration of a basic blockchain-like setup. </p>

<h2> Setup Basic client & server</h2>
<p>Python version: 3.12</p>
<p>Environment: windows</p>
<p>Command:</p>
<ul>
    <li>terminal A: $ python server.py</li>
    <li>terminal B: $ python client.py [path to input json file]</li>
</ul>
<p>For input json files, it should contain a list of dict objects, either in the format of a vote or a block, as specified in the Flow-Block-Processor.pdf file.</p>
<h1>Special Cases & assumptions </h1>
<p> The blocks inside the accepted blockchain have their unique ids. But the pending blocks may contain blocks with same id, a block is only accepted if its id is unique in the accepted blockchain.</p>
<p> Repeated votes or repeated ids are not announced. The program only outputs accepted block info.</p>
<p> Since votes don't contain view field, if there are blocks with identical ids in the pending block array, we just vote the one with min view.</p>

<h1>Server Intro</h1>
<p> There are two major arrays - block_array and pending_block_array.
Block_array contains the id of all accepted blocks, sorted in consequtive view orders. 
Pending_block_array has the received blocks that are not accepted. They could be (1)not voted or (2) voted but waiting for all blocks with a smaller view to be accepted.</p>

<h1>Tests</h1>
<h2>Json test files</h2>
<p> Here's a brief explanation of the tests:</p>
<ul>
    <li>example_trivial.json: a basic use case</li>
    <li>example_repeats.json: handle repeated ids</li>
    <li>example_wrong_format.json: handle wrong input formats</li>
    <li>example_out_of_order.json: handle out-of-order inputs</li>
    <li>example_concurrency_b/v.json: handle concurrent requests, used with client_concurrency.py</li>
</ul>

<h2>Python client</h2>
<p>There are two client files, client.py and client_concurrency.py</p>
<p>To run client.py: $ python client.py [path to input json file]</p>
<p>To run client_concurrency.py: $ python client_concurrency.py</p>
<p>Client concurrency demonstrates a use case with 2 threads sending votes/blocks.</p>

<h2>Improvements</h2>
<p>Due to the time limit, I haven't fully completed the concurrency feature. The default ThreadingHttpServer from Python is not efficient enough. It creates a thread for each request - I think it's not the best solution for this program. The program works with small number of concurrent client programs, but with a larger thread number there are higher delay. </p>
<p>Some of my thoughts and ideas for potential improvements are</p>
<ul>
    <li> Two ports and two threads. Just use one thread for handling votes and another for handling block info. The server could listen on two ports for the two types of request.</li>
    <li> Two locks: one lock for block_array and another for pending_block_array. Even there are many threads, the recourse sharing would be better with two locks.</li>
    <li> A verification program: I use test case generater to generate json input files, but it's nice to have a verification program to examine the accepted blocks. Then I don't need to manually check the outputs, and I can leave the console for debugging the (pending) block arrays. </li>
</ul>