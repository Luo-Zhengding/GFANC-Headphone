# GFANC-Headphone
This repository contains the code for the paper "**Deep Learning-Based Generative Fixed-Filter Active Noise Control: Transferability and Implementation**," published in the **Mechanical Systems and Signal Processing** journal. The paper link is [Paper Link](https://www.sciencedirect.com/science/article/abs/pii/S0888327025009082)

This is a collaborative research work between the Digital Signal Processing Lab at Nanyang Technological University, Northwestern Polytechnical University, and National University of Singapore.

## Research Background
The **deep learning-based Generative Fixed-Filter Active Noise Control (GFANC)** method can generate suitable control filters for different noise types, achieving faster response and better noise reduction than conventional approaches. However, its transferability and practical performance have not yet been fully validated. In this paper, the deep learning-based GFANC method is implemented in an Active Noise Control (ANC) headphone. A theoretical explanation of GFANC’s transferability is also provided.

## GFANC Framework
<p align="center">
  <img src="https://github.com/user-attachments/assets/3956e3cf-4f58-4e02-b338-3341937d1b89" width="600"><br>
  The framework of the deep learning-based GFANC method.
</p>

<br>

- The **dual-rate** structure allows GFANC to leverage the learning capabilities of the CNN to systematically enhance noise control performance while ensuring delayless noise reduction.
- The co-processor employs a lightweight CNN to automatically generate a weight vector for each frame of noise data.
- By calculating the inner product of this weight vector and sub control filters, a new control filter is generated and subsequently used for real-time noise control at the sampling rate.

## Transferability of GFANC
The CNN model and sub control filters in GFANC can operate independently, allowing the pre-trained CNN to be seamlessly transferred across different GFANC systems. When transferring the deep learning-based GFANC method to a new acoustic environment, only the sub control filters—which are determined by the specific acoustic paths—need to be updated. This approach significantly reduces the effort and cost associated with retraining the CNN model, thereby facilitating broader practical implementation.

## Headphone Implementation of GFANC
<p align="center">
  <img src="https://github.com/user-attachments/assets/c64f081a-c6aa-42c3-90a1-282e3363c612" width="600"><br>
  Overall implementation diagram of the GFANC method in an ANC headphone.
</p>

<br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/77d93a69-efef-4c95-bd0f-4095e663988d" width="250"> 
  <img src="https://github.com/user-attachments/assets/cf21e9b7-d30c-4da7-a721-bc0fd871ba0f" width="600">
  <br>
  Hardware setup of the headphone experimental system.
</p>

- In this system, the co-processor is a laptop equipped with Intel(R) Core(TM) i7-10870H CPU, which runs the trained CNN to predict the weight vector for the incoming noise.
- Simultaneously, an embedded PXI processing unit (NI PXIe-8135) with a pre-amplifier, an I/O unit, and an output amplifier serves as the real-time controller to perform immediate noise control.
- If the relative error between the predicted weight vector and the current weight vector exceeds a threshold, the laptop transmits the predicted weight vector to the PXI processing unit via UDP.
