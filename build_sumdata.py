import json
from utils.util import load_json_line_by_line
instruct2 = """
"Based on your previous analysis, summarize the causal relationship between Event 1 and Event 2 using your reasoning from earlier steps. Conclude the nature of their relationship by choosing one of the following options:
1. 'Cause' if your analysis determined that Event 1 causes Event 2.
2. 'Caused by' if your analysis found that Event 1 is caused by Event 2.
3. 'None' if your analysis concluded there is no causal relationship between Event 1 and Event 2.
Your summary should clearly state the final conclusion derived from your analysis, succinctly encapsulating the reasoning process that led to this determination."
"""
instruct1 ="Based on your previous analysis, what is the causal relationship between Event 1 and Event 2. answer with one of below option:1.cause 2.caused by 3.no causal relationship"
instruct="now, summarize your answer. what is the causal relationship between event1 and event2? your answer should be 1.cause 2.caused by 3.none"
with open("./data/ECI2.json","r",encoding="utf-8") as f:
    data = json.load(f)
p = load_json_line_by_line("./output\ECIhardprompt\generated_predictions1.jsonl")
sum_data = []
for i,d in enumerate(data):
    if i==100:break
    sum_data.append({"instruction":instruct1,"input":"","output":d["output"],"history":[[d["instruction"]+d["input"],p[i]["predict"]]]})
with open("./data/ECI_sum.json","w",encoding="utf-8") as f1:
    json.dump(sum_data,f1)
