# svg [![Build Status](https://travis-ci.com/maxgodfrey2004/svg.svg?branch=master)](https://travis-ci.com/maxgodfrey2004/svg) [![Coverage Status](https://coveralls.io/repos/github/maxgodfrey2004/svg/badge.svg?branch=master)](https://coveralls.io/github/maxgodfrey2004/svg?branch=master)

Create Scalable Vector Graphics in Python.

Please note that this project is completely unmaintained. There are many better alternatives with greater functionality.

## Background

I participated in the University of New South Wales' ProgComp some time in June (2019) with some mates, and my team was fortunate enough to qualify for the finals in Sydney having placed 4th out of 181 teams. Every year, the finals have an image processing/generation task. This year, we had to generate Scalable Vector Graphics* (SVGs); and we were allowed to use any modules during the contest which we had written before, or during the contest. More specifically, our programs had to be capable of animating certain aspects of the SVGs. It therefore seemed logical to write a library which could programmatically generate SVGs with all necessary `animate` and `animateTransform` tags.

Unfortunately though, we were not told about the image processing task until the week before the competition - with the finals being held on the 9th of September. As such, this was an incredibly hasty project being written over the course of four days, so the code is not the best. In fact, when generating SVGs, some very non-standard stuff gets, done with Python's keyword arguments (any kwargs you pass to the programmatic representation of an XML tag wind up in the XML - this was done to save time during the competition).

As a consequence of all this, you should definitely not use my SVG library in your projects. I am also not maintaining this repository any more because there are many better alternative libraries. With that in mind though, if my team happens to make finals again next year (2020), and the image task is still SVG related, there is a good chance that I will come back to this repository and spruce it up a bit.
