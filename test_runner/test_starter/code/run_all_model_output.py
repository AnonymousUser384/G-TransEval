import os
import subprocess
import json

if __name__ == "__main__":
    langs = ["cpp", "java","java_2", "python","csharp","javascript"]
    suffix = {"cpp":"cc","java":"java","java_2":"java","python":"py","javascript":"js","csharp":"cs","csharp_2":"cs"}
    levels  = ["l1","l2","l3","l4"]

    # files = ["cpp2cs","cpp2java","cpp2js","cpp2py",
    # "cs2cpp","cs2java","cs2js","cs2py",
    # "java2cpp","java2cs","java2js","java2py",
    # "js2cpp","js2cs","js2java","js2py",
    # "py2cpp","py2java","py2cs","py2js"
    # ]

    # files = ["cpp2java","cs2java","js2java","py2java",
    # "java2cpp","java2cs","java2js","java2py",
    # ]

    files = ["java2cs"]

    result_name = "simple-copy"

    for filename in files:
        with open(fr"..\..\test_target\{result_name}\{filename}.txt","r",encoding="utf-8") as f:
            codes = []
            for line in f:
                codes.append(line)
        codes_levels = []
        codes_levels.append(codes[:125])
        codes_levels.append(codes[125:250])
        codes_levels.append(codes[250:375])
        codes_levels.append(codes[375:])
        for level, codes_level in enumerate(codes_levels):
            level += 1
            path = fr"..\..\test_target\{result_name}\l{level}"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(fr"..\..\test_target\{result_name}\l{level}\{filename}.txt","w",encoding="utf-8") as f:
                for line in codes_level:
                    f.write(line)

    files_lang = {"cpp2cs":["csharp","csharp_2"],"cpp2java":["java","java_2"],"cpp2js":["javascript"],"cpp2py":["python"],
    "cs2cpp":["cpp"],"cs2java":["java","java_2"],"cs2js":["javascript"],"cs2py":["python"],
    "java2cpp":["cpp"],"java2cs":["csharp","csharp_2"],"java2js":["javascript"],"java2py":["python"],
    "js2cpp":["cpp"],"js2cs":["csharp","csharp_2"],"js2java":["java","java_2"],"js2py":["python"],
    "py2cpp":["cpp"],"py2java":["java","java_2"],"py2cs":["csharp","csharp_2"],"py2js":["javascript"]}

    for filename in files:
        for level in levels:
            for lang in files_lang[filename]:
                print(f"running {lang} test for {filename} {level}:",flush = True)
                params = ["python","run.py", "--gen_template", "--gen_test", "--run_test"]
                # params = ["python","run.py", "--gen_template", "--gen_test"]
                params += ["--lang", lang]
                params += ["--unit_test_file",fr"..\..\dataset\config\{level}.json"]
                params += ["--test_file",fr"..\..\test_target\{result_name}\{level}\{filename}.txt"]
                if len(files_lang[filename]) > 1:
                    params += ["--out_name", fr"{filename}_{lang}"]
                else:
                    params += ["--out_name", fr"{filename}"]
                proc = subprocess.run(params)
            if len(files_lang[filename]) > 1:
                params = ["python","merge_test.py","--result_files"]
                for lang in files_lang[filename]:
                    params += [fr"..\..\test_result\{level}_{filename}_{lang}.json"]
                params += ["--out_file", fr"..\..\test_result\{level}_{filename}.json"]
                proc = subprocess.Popen(params)