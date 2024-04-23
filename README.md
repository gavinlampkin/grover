
## GROUP 14'S README IS LOCATED WITHIN THE /DISCRIMINATION FOLDER, THE ROOT README CONTAINS INFO ON HOW TO GET THE GENERATOR WORKING!

# Grover
##### UPDATE, Sept 17 2019. We got into NeurIPS (camera ready coming soon!) and we've made Grover-Mega publicly available without you needing to fill out the form. You can download it using [download_model.py](download_model.py).

(aka, code for [Defending Against Neural Fake News](https://arxiv.org/abs/1905.12616))

Grover is a model for Neural Fake News -- both generation and detection. However, it probably can also be used for other generation tasks. 

Visit our project page at [rowanzellers.com/grover](https://rowanzellers.com/grover), [the AI2 online demo](https://grover.allenai.org), or read the full paper at [arxiv.org/abs/1905.12616](https://arxiv.org/abs/1905.12616). 

![teaser](https://i.imgur.com/VAGFpBe.png "teaser")

## What's in this repo?

We are releasing the following:
* Code for the Grover generator (in [lm/](lm/)). This involves training the model as a language model across fields.
* Code for the Grover discriminator in [discrimination/](discrimination/). Without much changing, you can run Grover as a discriminator to detect Neural Fake News.
* Code for generating from a Grover model, in [sample/](sample/).
* Code for making your own RealNews dataset in [realnews/](realnews/).
* Model checkpoints freely available online for *all* of the Grover models. For using the RealNews dataset for research, please [submit this form](https://docs.google.com/forms/d/1LMAUeUtHNPXO9koyAIlDpvyKsLSYlrBj3rYhC30a7Ak) and message me on [contact me on Twitter](https://twitter.com/rown) or [through email](https://scr.im/rowan). You will need to use a valid account that has google cloud enabled, otherwise, I won't be able to give you access 😢

Scroll down 👇 for some easy-to-use instructions for setting up Grover to generate news articles.

## Setting up your environment

*NOTE*: If you just care about making your own RealNews dataset, you will need to set up your environment separately just for that, using an AWS machine (see [realnews/](realnews/).)

There are a few ways you can run Grover:
* **Generation mode (inference)**. This requires a GPU because I wasn't able to get top-p sampling, or caching of transformer hidden states, to work on a TPU.
* **LM Validation mode (perplexity)**. This could be run on a GPU or a TPU, but I've only tested this with TPU inference.
* **LM Training mode**. This requires a large TPU pod.
* **Discrimination mode (training)**. This requires a TPU pod.
* **Discrimination mode (inference)**. This could be run on a GPU or a TPU, but I've only tested this with TPU inference.

**NOTE**: You might be able to get things to work using different hardware. However, it might be a lot of work engineering wise and I don't recommend it if possible. Please don't contact me with requests like this, as there's not much help I can give you.

I used Python3.6 for everything. Usually I set it up using the following commands:
```
curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p ~/conda && \
     rm ~/miniconda.sh && \
     ~/conda/bin/conda install -y python=3.6
```
Then `pip install -r requirements-gpu.txt` if you're installing on a GPU, or `pip install requirements-tpu.txt` for TPU.

Misc notes/tips:
* If you have a lot of projects on your machine, you might want to use an anaconda environment to handle them all. Use `conda create -n grover python=3.6` to create an environment named `grover`. To enter the environment use `source activate grover`. To leave use `source deactivate`.
* I'm using tensorflow `1.13.1` which requires Cuda `10.0`. You'll need to install that from the nvidia website. I usually install it into `/usr/local/cuda-10.0/`, so you will need to run `export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64` so tensorflow knows where to find it. 
* I always have my pythonpath as the root directory. While in the `grover` directory, run `export PYTHONPATH=$(pwd)` to set it.

## Quickstart: setting up Grover for generation!

1. Set up your environment. Here's the easy way, assuming anaconda is installed: `conda create -y -n grover python=3.6 && source activate grover && pip install -r requirements-gpu.txt`
2. Download the model using `python download_model.py base`
3. Now generate: `PYTHONPATH=$(pwd) python sample/contextual_generate.py -model_config_fn lm/configs/base.json -model_ckpt models/base/model.ckpt -metadata_fn sample/april2019_set_mini.jsonl -out_fn april2019_set_mini_out.jsonl`

Congrats! You can view the generations, conditioned on the domain/headline/date/authors, in `april2019_set_mini_out.jsonl`.

## FAQ: What's the deal with the release of Grover?

Our core position is that [it is important to release possibly-dangerous models to researchers](https://thegradient.pub/why-we-released-grover/). At the same time, we believe Grover-Mega isn't particularly useful to anyone who isn't doing research in this area, particularly as [we have an online web demo available](https://grover.allenai.org/) and the model is computationally expensive. We previously were a bit stricter and limited initial use of Grover-Mega to researchers. Now that several months have passed since we put the paper on arxiv, and since several other large-scale language models have been publicly released, we figured that there is little harm in fully releasing Grover-Mega.

### Bibtex

```
@inproceedings{zellers2019grover,
    title={Defending Against Neural Fake News},
    author={Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
    booktitle={Advances in Neural Information Processing Systems 32},
    year={2019} 
}

@misc{huang2023faking,
      title={Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation}, 
      author={Kung-Hsiang Huang and Kathleen McKeown and Preslav Nakov and Yejin Choi and Heng Ji},
      year={2023},
      eprint={2203.05386},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

@misc{keskar2019ctrl,
      title={CTRL: A Conditional Transformer Language Model for Controllable Generation}, 
      author={Nitish Shirish Keskar and Bryan McCann and Lav R. Varshney and Caiming Xiong and Richard Socher},
      year={2019},
      eprint={1909.05858},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
### Other Scholarly Sources 

* [Priror Research](https://arxiv.org/abs/1909.05858)

Summary: While existing large-scale language models demonstrate promising text generation capabilities, the generated texts can be difficult to control for users who may want to fine-tune specific features or parameters. To bridge the gap, we introduce CTRL, a 1.63-billion-parameter conditional transformer language model. This model was designed to be conditioned on an additional input of control codes responsible for the style of generated text, content features, or specific task-aligned behavior. We designed the model in a way that enforces control codes to similarly occur in tandem with raw text structure: this maintains the benefits of unsupervised learning while offering explicit control over text construction. The automatic prediction ability over large swaths of the dataset given a sequence of text is allowed for the selection of raw text via CTRL’s control codes. 

* [Contemporary Work](https://arxiv.org/abs/2203.05386)

Summary: While recent work has shown that fake news generated by neural models can be effectively detected, these results cannot be readily transferred to an effective detection of human-written disinformation. This is because there is a notable gap between the human and machine-generated artifacts in this domain, manifested in significant stylistic differences and in significantly different underlying intent. We thus propose a new framework for generating training examples that specifically adds the types of bias present in the known human-authored propaganda. We do it by self-critical sequence training, guided by natural language inference to ensure the final validity of the generated articles, while incorporating the bias principles. In total, we generate a new dataset, PROPANEWS, consisting of 2,256 examples, which we make publicly available for further use. Our experimental results show that fake news detectors trained on PROPANEWS achieve 3.62–7.69% F1 rating improvement when exposed to human-written disinformation on two public datasets.