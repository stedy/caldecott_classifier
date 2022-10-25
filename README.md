# Caldecott Classifier

This is a repo to demonstrate classifying book covers (specifically the
winners of the [Caldecott Medal](https://en.wikipedia.org/wiki/Caldecott_Medal)) by the
color compositions of their covers based on some pre-trained data.

To replicate this analysis run the scripts in this order:

1 - `get_covers.py` - downloads images of each book cover from Wikpedia

2 - `build_model.py` - Uses [Tensorflow](https://www.tensorflow.org/) to
build a matrix of likely colors based on pre-trained color data

3 - `classify_covers.py` - Uses the [colorgram](https://github.com/obskyr/colorgram.py) python module to extract color profiles from each cover image and classify each book
cover using the model built in the prior step.

4 - `make_figure.py` - Uses [Seaborn](https://seaborn.pydata.org/) to
create the following figure of book color distributions by year:

![caldecott_colors](https://user-images.githubusercontent.com/345365/197893220-15c38d3f-197c-417e-9cfe-725834687aee.png)
