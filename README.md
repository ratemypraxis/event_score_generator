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

  > **Grasp in Fire**
  >
  > Dawn: Be in full fire
  >
  > Late Morning: Know twelve o’clock with grasp
  >
  > Afternoon: Take fires
  >
  > Evening: Determine six thirty pm of grasp
  >
  > Night: Remembrance for a few paltry hours in longer fire


  or 
  
  ```
  python esg.py surprise
  ```

  would give you an output tailored to a random noun like this:

  > **Morning for Duty**
  > 
  > Morning: Yield of most duty
  >
  > Late Morning: Be that morning on morning
  >
  > Afternoon: Know duties
  >
  > Evening: Reach about two hours with morning
  >
  > Night: Be for eight hours in less duty

## Next steps:
- address speed / try to lighten the load with a smaller spaCY module or less source texts
- play with structre and randomness a bit with the tracery grammer + other spaCy tokens
- implement flask to push this to web
- create a requirements.txt with dependencies
- maaaybe experiment with a conda environment
