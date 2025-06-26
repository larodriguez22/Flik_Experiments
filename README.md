# Flik Empirical Study

This repository contains all the information related to the empirical study for the Flik debugger for Reinforcement Learning programs.

---

## Contents

1. [Evaluation](./Evaluation) contains all the programs to evaluate during the study (GridWorld, Rooms, Driving Assistant)
2. [Guides](./Guides) contains the guides and evaluation forms for the study
3. [Results](./Results) contains all the results for the study

## Release

Flik and the associated experimetns are relseased within a Docker container to facilitate use and assure library compliance.

To use Flik from Docker:

#### Option 1: Play with docker

Use the ``docker pull`` command to download the docker image. And start running it on your computer or run it in play with docker page. To be able to run it in play with docker page, create a new account and add a new instance (this might take a while, but is for free and on the web, so you don’t need to install docker).

```docker pull lrodriguez22/py-flik-debugger:latest```

Then you can use Flik executing the following command:
```docker run -it lrodriguez22/py-flik-debugger```

#### Option 2: download tar
Download the docker container from this docker container.
Once you have downloaded the following .zip. Open a terminal and make sure you go to the path you download the .zip, then type:

```docker load -i py-flik-debugger.tar```

This should take some minutes to complete. Once it has finished downloading, run the docker container with the following command:

```docker run -it py-flik-debugger```

## Participation

If you want to participate in the evaluation of Flik feel free to download and use Flik following the guides for the evaluation contained in this repository. Make sure to fill in the form at the end of the experiments.

Thanks for your cooperation.
