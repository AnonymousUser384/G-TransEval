import os
import json
import argparse

from gen_test_template import gen_test_template
from gen_test_file import gen_test_file,gen_test_file_no_format
from run_test_file import run_test_file
from utils import suffix, TestResult

if __name__ == "__main__":
    langs = ["cpp", "java","java_2", "python", "javascript","csharp","csharp_2"]    

    parser = argparse.ArgumentParser()
    parser.add_argument("--gen_template",action="store_true",required=False)
    parser.add_argument("--gen_test",action="store_true",required=False)
    parser.add_argument("--run_test",action="store_true",required=False)
    parser.add_argument("--unit_test_file",required=False)
    parser.add_argument("--lang",required=False)
    parser.add_argument("--test_file",required=False)
    parser.add_argument("--out_name",required=False)
    parser.add_argument("--delimiter",required=False)
    args = parser.parse_args()

    unit_test_file = f"../../config/human_eval_x.json"
    if args.unit_test_file:
        unit_test_file = args.unit_test_file
    with open(unit_test_file, "r", encoding="utf-8") as f:
        cfg_json = json.load(f)
    dataset_name = cfg_json["name"]
    questions = cfg_json["questions"]
    l = [question["name"] for question in questions]
    
    if args.lang:
        langs = [args.lang]

    question_names = []    
    for i in range(len(questions)):
        question_names.append('%04d'%i+"-"+questions[i]["name"])

    if args.gen_template:
        for lang in langs:
            for question,name in zip(questions,question_names):
                gen_test_template(lang,dataset_name,question,name)
    
    if args.gen_test:
        for lang in langs:
            if not args.test_file:
                test_file = "../../target_file/human_eval_x_gold/target"+suffix(lang)
            else:
                test_file = args.test_file
            codes = []
            with open(test_file, "r", encoding="utf-8") as f:
                code = ""
                for line in f:
                    print(line)
                    if not args.delimiter:
                        codes.append(line)
                    else:
                        if line[:len(args.delimiter)] != args.delimiter:
                            code += line
                        else:
                            codes.append(code)
                            code = ""
            if not args.delimiter:
                for i in range(len(codes)):
                    gen_test_file(lang, dataset_name,question_names[i], codes[i])
            else:
                for i in range(len(codes)):
                    gen_test_file_no_format(lang, dataset_name,question_names[i], codes[i])

    if args.run_test:
        result = {}
        for lang in langs:
            lang1 = lang
            if lang == "java_2":
                lang1 = "java"
            if lang == "csharp_2":
                lang1 = "csharp"
            result[lang1] = {}
            result[lang1]["results"] = {}
            for question_name in question_names:
                ret = run_test_file(lang, dataset_name, question_name)
                result[lang1]["results"][question_name] = ret.name
            result[lang1]["total"] = 0
            result[lang1]["correct_num"] = 0
            result[lang1]["compile_pass_num"] = 0
            for value in result[lang1]["results"].values():
                result[lang1]["total"] += 1
                if value == "AllPassed":
                    result[lang1]["correct_num"] += 1
                    result[lang1]["compile_pass_num"] += 1
                elif value == "CompilationPassed":
                    result[lang1]["compile_pass_num"] += 1

        if not os.path.exists("../../test_result/"):
            os.makedirs("../../test_result/")
        st = "result"
        if args.out_name:
            st = args.out_name
        with open(f"../../test_result/{dataset_name}_{st}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(result))
