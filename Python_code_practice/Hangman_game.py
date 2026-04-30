from collections import Counter 
from genericpath import sameopenfile
import random as rd

from shap import SamplingExplainer
sample_words=" Counter is a subclass of Python’s dict from the collections module. It is mainly used to count the frequency of elements in an iterable (like lists, strings or tuples) or from a mapping (dictionary). It provides a clean and efficient way to tally items without writing extra loops and comes with helpful built-in methods."
sample_words=sample_words.split()

print(sample_words)
