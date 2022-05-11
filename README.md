# imagenet-utils

A repository containing helpful utility scripts and serialised data for the Imagenet dataset

## Wordnet Mappings
The `utils.py` script contains methods to easily map between imagenet class labels and their corresponding synsets (eg. tights <--> n03710637).

## Wikipedia Summaries
The file `wikipedia_contexts_by_imagenet_class.pickle` contains a dictionary mapping imagenet class names to their corresponding summaries from wikipedia. The script `create_wikipedia_knowledge.py` can be used to generate this file.
