import os
import json
import argparse

if __name__ == "__main__":
    langs = ["cpp", "java", "python", "javascript","csharp","php"]

    parser = argparse.ArgumentParser()
    parser.add_argument("--result_files",nargs="+",required=False)
    parser.add_argument("--out_file",required=False)
    args = parser.parse_args()
    
    results = []

    for r in args.result_files:
        print(r)
        with open(r, "r", encoding="utf-8") as f:            
            results.append(json.load(f))
    
    new_result = {}
    for result in results:
        for key,value in result.items():
            if key not in new_result:
                new_result[key] = {"results":{}}
            for k,v in value["results"].items():
                if v == "CompilationFailed":
                    if k not in new_result[key]["results"]:
                        new_result[key]["results"][k] = v
                if v == "CompilationPassed":
                    if k not in new_result[key]["results"] or new_result[key]["results"][k] == "CompilationFailed":
                        new_result[key]["results"][k] = v
                if v == "AllPassed":
                    if k not in new_result[key]["results"] or new_result[key]["results"][k] == "CompilationFailed" or new_result[key]["results"][k] == "CompilationPassed":
                        new_result[key]["results"][k] = v
    
    for key,value in new_result.items():
        t_num = 0
        a_num = 0
        c_num = 0
        for k,v in value["results"].items():
            t_num += 1
            if v == "CompilationPassed":
                c_num += 1
            if v == "AllPassed":
                c_num += 1
                a_num += 1
        new_result[key]["total"] = t_num
        new_result[key]["correct_num"] = a_num
        new_result[key]["compile_pass_num"] = c_num

    with open(args.out_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(new_result))