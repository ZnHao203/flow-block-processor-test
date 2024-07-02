# flow-block-processor-test

<h1> Setup Basic client & server</h1>
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

<h1>Tests</h1>
<p> Here's a brief explanation of the tests:</p>
<ul>
    <li>example_trivial.json: a basic use case</li>
    <li>example_repeats.json: handle repeated ids</li>
    <li>example_wrong_format.json: handle wrong input formats</li>
    <li>example_out_of_order.json: handle out-of-order inputs</li>
</ul>