# Event Score Generator
***a python script / command line toy which generates instructions for situation performance art (an event score) based on user input***
## What is an event score?
Alison Knowles, who was a pioneer of practice-based artistic movement Fluxus, defines an event score as "a one or two line recipe for action". Essentially these are short instructions for performance art which is inspired by or directly amplifies activity & behavior from everyday life. 

## How is the computer generating these?
In this case, the computer is *attempting* to generate event scores making use of an english language module called spaCy, and it's language tokenization and tagging features, along with python library tracery to define grammar and re-fashion token words and phrases into new structure. The texts processed with these tools are a combination of instructional and self-help literature from long ago sources on Project Gutenburg - you can view the exact un-processed texts from within the sourceTexts directory. 

## How can I use computer to generate some event scores?
1. Clone this repository & install dependencies as below (assuming you already have python installed)
```
pip install spacy tracery
python -m spacy download en_core_web_md
```

2. Run the code with an expected input follower - this can be any noun or the word "surprise" for a random noun.
```
python esg.py NOUN
```
  for example:
  ```
  python esg.py fire
  ```
  would give you an output tailored to the word house like so:

  > **Morning for Duty**
 
  > Morning: Yield of most duty
 
  > Late Morning: Be that morning on morning
 
  > Afternoon: Know duties
 
  > Evening: Reach about two hours with morning
 
  > Night: Be for eight hours in less duty

  
  ![screenshot of command line output text generation](https://cdn.discordapp.com/attachments/1083420545246306365/1189406759085948989/Screenshot_from_2023-12-26_22-16-37.png?ex=659e0c5d&is=658b975d&hm=eaa733290534a6dae58ba6c61f6d55005a3238709b08b83c543581ad8f9902c8&)

  or 
  ```
  python esg.py surprise
  ```
  would give you an output tailored to a random noun like this:

  ![screenshot of command line output text generation](https://media.discordapp.net/attachments/1083420545246306365/1189407921302409298/Screenshot_from_2023-12-26_22-21-19.png?ex=659e0d72&is=658b9872&hm=5afe8167b5913df50048409b17b6b449c195f4daa3dac9dc8cb3ed65709541ae&=&format=webp&quality=lossless&width=1482&height=851)

## Next steps:
- address speed / try to lighten the load with a smaller spaCY module or less source texts
- play with structre and randomness a bit with the tracery grammer + other spaCy tokens
- implement flask to push this to web
- create a requirements.txt with dependencies
- maaaybe experiment with a conda environment
