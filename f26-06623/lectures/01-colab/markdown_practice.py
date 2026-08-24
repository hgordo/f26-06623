import os
import json
import ipywidgets as widgets
import functools
from IPython.display import Markdown, display

def load_state():
    if os.path.exists("state.json"):
        return json.load(open("state.json"))
    else:
        return {}


def save_state(state):
    with open("state.json", "w") as f:
        f.write(json.dumps(state))


state = load_state()

questions = [
    {

        "question":  "What is the correct way to make text bold in markdown?",
        "answer": ["*text*", "**text**", '<text style="bold">text</text>']
    },
    {
           "question": "What is the correct way to make italics text in markdown?",
        "answer": ["*text*", "**text**", '<text style="italic">text</text>']
    },
    {
        "question": "Which is a level 3 heading in Markdown?",
        "answer": ['#3 heading title', '### headingtitle', '*** heading title']
    },
    {
        'question': r'How do you represent the equation $\int_0^x e^x\,dx$ in Markdown?',
        'answer': [r"$\int_0^x e^x\,dx$",
                  r'¯\_(ツ)_/¯',
                  'int0xex']
    },
    {
     'question': 'What is the syntax for a link in Markdown?',
        'answer': ['[text](url)',
                   '(text)[url]',
                   '[[url]]']              
    }
]


out = widgets.Output()

def on_value_change(change, qid):
    state[qid] = change["new"]
    save_state(state)
    with out:
        print(state)

for i, q in enumerate(questions):
    qid = str(i)
    saved_value = state.get(qid)

    # An answer saved by an older version of the quiz may no longer be an
    # available option. In that case, show the question as unanswered.
    if saved_value not in q["answer"]:
        saved_value = None
       
    display(Markdown(q["question"]))

    choices = widgets.RadioButtons(
        options=q["answer"],
        layout={"width": "max-content"},
        description="Answer:",
        value=saved_value,
    )

    choices.observe(functools.partial(on_value_change, qid=qid), names="value")
    display(choices)
    
        
