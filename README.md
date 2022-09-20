# ATexPro Light

This document is about helping users install and use ATexPro Light, which stands for Afiniti Text Preprocessor Light version. The initial version of it is 0.1.0. They can also leverage this package along with ADAIR as will be explained.

## How to install and run it on the server

We packaged this ATexPro light into a single wheel file with the models thereof (i.e. 1. Sentence Transformer, 2. spaCy word2vec vectors, 3. NLTK stopwrods). In order to leverage this package, you additionally need only one external .tar.gz, which is for sentence transformer (with the version 1.2.0). To use this package, you need to install the required files via the following commands for the ADAIR docker on the AI server (http://10.36.25.93/):

- %pip install --user /home/jovyan/work/nlp_common/bilge.sipal/NLP_team_only/apro_lightv3/sentence-transformers-1.2.0.tar.gz

- %pip install --user /home/jovyan/work/nlp_common/cem.aydin/NLP_team_only/atexpro_light-0.1.0-py3-none-any.whl

These items above involving the use of the sentence-transformer and .whl files can be updated with respect to the path of this file, for example, for the AT&T server. For the docker base-note-book on the AI server, it suffices to install the following package only:

- %pip install --user /home/jovyan/work/nlp_common/cem.aydin/NLP_team_only/atexpro_light-0.1.0-py3-none-any.whl

The CUDA might not work for the ADAIR docker on the AI server. After installing these, one has to have folders as in apro_light_version_3 or the relevant folder from which the code is going to be called. One has to configure full paths with respect to the location of their folders as in this folder. Then one can run the jupyter notebook (*.ipynb). In the end, the .csv files will be generated and will be located in the output folder.

Relative paths are adapted for this ATexPro light version repo differently from ADAIR. That is, the code can run smoothly for both Linux (e.g. AI server) and Windows (e.g. your local computer). We also made the code easy to use in the sense that the config parameters can also be updated in the jupyter notebook on the AI or AT&T server as True or False as follows:

```
config['feat_ext'].char = False
config['feat_ext'].word = True
config['feat_ext'].word3 = True
config['feat_ext'].pretrained_w2v = True
config['feat_ext'].transformer = True
```

## How to run it from within your local computer

The main code for ATexPro light on BitBucket (https://code.afiniti.com/projects/DATA/repos/nlp/browse?at=refs%2Fheads%2Fatex_pro_light) can also be pulled and be run on one's local computer by creating a virtual environment on PyCharm in the first place, for which we use Python 3.8.2. All the dependencies are stated in the requirements.txt file in the docs folder. However, as mentioned above, the creation of a virtual environment is NOT needed for the servers. 

## Credits

Code was written by Bilge Sipal Sert (bilge.sipal@afiniti.com) and Cem Rifki Aydin (cem.aydin@afiniti.com).
