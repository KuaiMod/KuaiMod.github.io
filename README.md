# VLM as Policy: Common-Law Content Moderation Framework for Short Video Platform

<!-- ![MathQA](https://img.shields.io/badge/Task-MathQA-red) 
![Mathematical Reasoning](https://img.shields.io/badge/Task-Mathematical_Reasoning-red) 
![Multi-Modal](https://img.shields.io/badge/Task-Multi--Modal-red) 
![ScienceQA](https://img.shields.io/badge/Dataset-MathVista-blue)  
![Claude-4](https://img.shields.io/badge/Model-Claude--2-green) 
![ChatGPT](https://img.shields.io/badge/Model-ChatGPT-green) 
![GPT-4](https://img.shields.io/badge/Model-GPT--4-green) 
![Gemini](https://img.shields.io/badge/Model-Gemini-green)
![GPT-4V](https://img.shields.io/badge/Model-GPT--4V-green) -->

<p align="center">
    <img src="assets/kuaimod_logo.png" width="40%"> <br>
  Logo of <b>KuaiMod</b>. 
  <br>
</p>

##  Introduction of Kuaimod
<p align="center">
    <img src="assets/intro_v2.jpg" width="60%"> <br>
  A visualization about three moderation paradigms: Manual, traditional AI-assisted and our <b>KuaiMod</b> paradigm. 
  <br>
</p>

Code for the Paper "[VLM as Policy: Common-Law Content Moderation Framework for Short Video Platform]()".

For more details, please refer to the project page with dataset exploration and visualization tools: [https://kuaimod.github.io/](https://kuaimod.github.io/).


[[Webpage](https://kuaimod.github.io/)] [[Visualization](https://kuaimod.github.io/visualization.html)] [[Github]](https://github.com/KuaiMod/KuaiMod.github.io)



## Data Visualization

🎰 You can explore the dataset in an interactive way [here](https://kuaimod.github.io/visualization.html).

;<iframe src="https://kuaimod.github.io/visualization.html" width="100%" height="800px"></iframe>


;<iframe src="https://kuaimod.github.io/rolling.html" width="100%" height="500px"></iframe>

<p align="center">
    <img src="assets/bili.png" width="50%"> <br>
  Distribution for the examples. 
  <br>
</p>


##  Implementation details of Kuaimod

<p align="center">
    <img src="assets/stage1_v2.png" width="100%"> <br> 
  <br>"Offline adaptation stage of KuaiMod: We post-train the YuanQi-7B with state-transition format data. After SFT and DPO training, KuaiMod is transformed into a video moderator to provide online services. ".
</p>


<!-- <details>
<summary>Click to expand/collapse the visualization page screenshot.</summary>
<img src="https://raw.githubusercontent.com/lupantech/MathVista/main/assets/data_visualizer.png" style="zoom:40%;" />
</details> -->

<p align="center">
    <img src="assets/stage2_v2.png" width="100%"> <br>
  <br>"Online deployment stage of KuaiMod: The initially trained KuaiMod model is deployed into Kuaimod as a moderation agent. KuaiMod interacts with the online environment and iteratively refines its policy with user feedback in the RL manner.".
</p>

##  Performance

### Offline Experiments

<p align="center">
    <img src="assets/offline.png" width="100%"> <br>
  <br>"Performance of Various Moderation Methods on the KuaiMod Benchmark. We categorize the moderation methods into <b>Binary Classification</b> and <b>Multi-class Classification</b>. The binary classification only determines whether a video is violative or not, while the multi-class classification requires the model to directly classify the video into its respective category. Optimal and sub-optimal performance is denoted in bold and underlined fonts, respectively.".
</p>

### Online Experiments
<p align="center">
    <img src="assets/online.png" width="60%"> <br>
  <br>"KuaiMod's online A/B test results for comprehensive ecosystem governance on Kuaishou NEBULA and Featured.".
</p>
