# discrimination

This folder contains code for the discrimination experiments.

`run_discrimination.py` can be used to train or evaluate a model for discrimination.

# Dependencies

Anaconda is needed and can be downloaded at: `https://docs.nvidia.com/cuda/cuda-installation-guide-linux/`

Set up your environment. Here's the easy way, `conda create -y -n grover python=3.6 && source activate grover && pip install -r requirements-gpu.txt`

Make sure to pip install the `requirements-gpu.txt`

# How to use `run_discrimination.py`
```
python3 run_discrimination.py --input_data= input.json --output_dir= /outputdir/ --do_train=True/False --config_file=/home/grover/lm/configs/...
```
# Input Data

Download a Grover dataset on your own from the root directory by running `python3 download_model.py base/medium/mega` or use the tableParser.

Grover uses a specific formatting for their input files in regards to the discriminator, you can use the tool provided under the discrimination directory to generate Grover-specific JSON files form Excel spreadsheets.
Using the tool is very easy! Just format your Excel file in the following way:

Column Headers: [article, domain, title, date, authors, ind30k, url, label(human/machine), orig_split, split, random_score]

Fill out your Excel spreadsheet with the specified data and save to the same directory as the tableParse file and run the following command:
```
$ ./tableParse.py -i input.xlsx out.json
```
# Discrimination checkpoints
Here are links to the discrimination checkpoints. You'll need to use google cloud storage to download these.

**NOTE**: These checkpoints were trained on 5000 examples from a specific Grover generator, with a specific nucleus sampling top-p setting. As a result, these aren't necessarily the best discrimination checkpoints, nor are they the most general. The reason we used this experimental setup is outlined [in the paper](https://arxiv.org/abs/1905.12616) -- we assumed limited access to the generator. We did [later experiments](https://medium.com/ai2-blog/counteracting-neural-disinformation-with-grover-6cf6690d463b) and found that if you assume, say, 100k examples from a generator, you'll do much better (up to around 97% accuracy).

In other words, if you want to mimic my experimental setup, but with your own generator, you'd also need to train your own discriminator from scratch. Alternatively, if you want a really good discriminator against my checkpoints for whatever reason, you'd also probably want to train your own discriminator from scratch.

Medium trained on medium, top-p=0.96:
```
gs://grover-models/discrimination/generator=medium~discriminator=grover~discsize=medium~dataset=p=0.96/model.ckpt-1562.data-00000-of-00001
gs://grover-models/discrimination/generator=medium~discriminator=grover~discsize=medium~dataset=p=0.96/model.ckpt-1562.index
gs://grover-models/discrimination/generator=medium~discriminator=grover~discsize=medium~dataset=p=0.96/model.ckpt-1562.meta
```

Mega trained on mega, top-p=0.94:
```
gs://grover-models/discrimination/generator=mega~discriminator=grover~discsize=mega~dataset=p=0.94/model.ckpt-1562.data-00000-of-00001
gs://grover-models/discrimination/generator=mega~discriminator=grover~discsize=mega~dataset=p=0.94/model.ckpt-1562.index
gs://grover-models/discrimination/generator=mega~discriminator=grover~discsize=mega~dataset=p=0.94/model.ckpt-1562.meta
```
