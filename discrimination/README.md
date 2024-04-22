# CS 4371 Group Project
> Our Team was look initally looking to introduce a new dataset to feed the dicriminator, but we shifted gears to make the discriminator more accessible with the introduction of tableParse.py. 


## Table of Contents
* [Team](#team)
* [Discrimination](#discrimination)
* [Dependencies](#dependencies)
* [How to Use](#how-to-use-run_discriminationpy)
* [Input Data](#input-data)
* [Discrimination Checkpoints](#discrimination-checkpoints)
* [Scholarly Papers](#scholarly-papers)

## Team

We are a team of Texas State University students researching neural fake news for our CS 4371 group project. Our Team consists of:

* Christopher B Pearson
* Gavin Wright Lampkin
* John Yamamoto
* Quetzin Luis Nahm Pimentel
* Luis Herrera

## discrimination

This folder contains code for the discrimination experiments.

`run_discrimination.py` can be used to train or evaluate a model for discrimination.

## Dependencies

Anaconda is needed and can be downloaded at: `https://docs.nvidia.com/cuda/cuda-installation-guide-linux/`

Set up your environment. Here's the easy way, `conda create -y -n grover python=3.6 && source activate grover && pip install -r requirements-gpu.txt`

## Input dataset

Download a Grover dataset on your own from the root directory by running `python3 download_model.py base/medium/mega` or use the tableParser.

Grover uses a specific formatting for their input files in regards to the discriminator, you can use the tool provided under the discrimination directory to generate Grover-specific JSON files form Excel spreadsheets.
Using the tool is very easy! Just format your Excel file in the following way:

Column Headers: [article, domain, title, date, authors, ind30k, url, label(human/machine), orig_split, split, random_score]


Fill out your Excel spreadsheet with the specified data and save to the same directory as the tableParse file and run the following command:
```
$ ./tableParse.py -i Grover_Excel_Data.xls output_file_name.json
```


## How to use `run_discrimination.py`
```
python3 run_discrimination.py --input_data= input.json --output_dir= /outputdir/ --do_train=True/False --config_file=/home/grover/lm/configs/...
```

## Output

Grover outputs a Loss function that is improved apon with multiple trials, you can find more about these results here: https://machinelearningmastery.com/loss-functions-in-tensorflow/


## Discrimination checkpoints
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
## Scholarly Papers

* [_Truth of Varying Shades: Analyzing Language in Fake News and Political Fact-Checking_](https://aclanthology.org/D17-1317) (Rashkin et al., EMNLP 2017) was presented at the 2017 Conference on Empirical Mathods in Natural Language Processing in Copenhagen, Denmark. It examined a multitude of online news sources and public statements and examined if the truth could be distinguished from different types of fake new (such as propaganda, satire, and hoaxes). It found that certain lexical features can be seen to help identify the difference between reliable and non-reliable sources online based on PolitiFact.com using their 6-point scale to determine factuality. Zellers and his team furthered this research by training Grover to identify neural fake news, and found a very high success rate in flagging misinformation generated by Grover itself, out performing some of the industries best discriminators such as Bert.  


* [_Faking Fake News for Real Fake News Detection: Propaganda-Loaded Training Data Generation._](https://arxiv.org/abs/2203.05386)
(Huang, Kung-Hsiang, et al. arXiv.Org, 15 May 2023) This scholarly paper addresses a significant challenge in detecting fake news generated by neural models—the difficulty in effectively identifying human-written disinformation due to the notable gap between machine-generated and human-authored content. The authors demonstrate an innovative approach using PROPANEWS, a new training dataset informed by human-authored propaganda styles, to improve fake news detection. They show that detectors trained on PROPANEWS achieve a 3.62–7.69% increase in F1 score for detecting human-written disinformation on two public datasets, leveraging advancements from models like GROVER and RoBERTa."


