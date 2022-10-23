# Caldecott Classifier

This is a repo to demonstrate classifying book covers (specifically the
[Caldecott Medal](https://en.wikipedia.org/wiki/Caldecott_Medal) by the
colors of their covers based on some pre-trained data.

To replicate this analysis run the scripts in this order:

1 - `get_covers.py` - downloads images of each book cover from Wikpedia
2 - `build_model.py` - Uses [Tensorflow](https://www.tensorflow.org/) to
build a matrix of likely colors based on pre-trained color data
3 - `classify_covers.py` - Classify the Caldecott Medal winners book
covers based on the model built in the prior step.
4 - `make_figure.py` - Uses [Seaborn](https://seaborn.pydata.org/) to
create the following figure of book colors by year:

![caldecott_colors.png]
