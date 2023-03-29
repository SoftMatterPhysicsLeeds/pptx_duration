## What is this? 

Have you ever sat through a pre-recorded Powerpoint presentation (3P) and wondered
when it would end? Would you like to put a 3P in the bin immediately if it is
longer that the 'maximum time' limit set in the candidate brief? Have you ever
made a 3P and wondered whether it would annoy the interviewers because of its
length? 

## pptx_duration

Pre-recorded Powerpoint presentations do not automatically come with a 'timer'
and so it isn't immediately obvious how long a recorded presentation is. This
simple Python script unzips the .pptx and determines the runtime for you. 

## Usage

This package isn't on PyPI yet (could be...) and so best is to build your own
wheel and then pipx install into a local environment (pipx -
https://github.com/pypa/pipx - allows the script to be run without 'python'
before it and installs itself, and its dependencies, in
it's own environment).

```
> git clone https://github.com/danlindleybaker/pptx_duration
> cd pptx_duration
> python -m build
...
> cd dist
> pipx install .\pptx_duration-0.0.1-py3-none-any.whl
> pptx_duration PATH_TO_PPTX

Total Time = 0:10:00 

```
