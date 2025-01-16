---
title: "Lartpc reinforcement learning"
categories:
 - posts
tags:
  - project
  - posts
excerpt: "Reinforcement learning in service of physics. With extra OpneAI gym sauce."
last_modified_at: 2021-03-21T12:34:19+02:00
---

![](https://i.imgur.com/IyswEwy.gif)

## lartpc2D

[github.com/mmajewsk/lartpc2D](https://github.com/mmajewsk/lartpc2D g)

The lartpc2D project focuses on applying reinforcement learning to solve problems in high energy physics, specifically using deep Q-learning. The project aims to model the behavior of particles in a Liquid Argon Time Projection Chamber (LArTPC) detector. Here are some key points:

Objective: To use reinforcement learning to simulate particle interactions within a LArTPC detector.
Approach:
An agent navigates through a 2D grid representing the detector, with the ability to move in 8 directions.
The agent’s visible frame consists of a 3x3 window of pixels, which it uses to classify and map the environment.
The agent iteratively categorizes pixels and updates a blank canvas with the detected classes.
Advantages:
This method closely mimics the actual detection process.
It allows for iterative and parallel processing.
The approach can be extended to include time dimensions and multiple agents.
Implementation:
The project uses datasets from deeplearnphysics.org.
The basic implementation involves deep Q-learning with two inputs and two outputs1.

## gym-lartpc2d

[github.com/mmajewsk/gym-lartpc2d](https://github.com/mmajewsk/gym-lartpc2d)

The gym-lartpc2d project is an extension of the lartpc2D project, designed to integrate with OpenAI’s Gym environment. This allows for standardized reinforcement learning experiments and easier benchmarking. Key aspects include:

Objective: To provide a Gym-compatible environment for reinforcement learning experiments on LArTPC data.
Features:
Integration with OpenAI Gym for standardized RL experiments.
Customizable environment settings to simulate different detector conditions.
Support for various RL algorithms to test and compare performance.
Usage:
Researchers can use this environment to train and evaluate RL models on LArTPC data.
The environment is designed to be flexible and extendable for different research needs2.
Feel free to explore the repositories for more detailed information and instructions! If you have any specific questions about these projects, let me know.